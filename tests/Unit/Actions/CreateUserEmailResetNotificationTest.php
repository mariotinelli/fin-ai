<?php

declare(strict_types=1);

use App\Actions\CreateUserEmailResetNotification;
use App\Models\User;
use Illuminate\Auth\Events\PasswordResetLinkSent;
use Illuminate\Auth\Notifications\ResetPassword;
use Illuminate\Contracts\Mail\Factory;
use Illuminate\Contracts\Mail\Mailer;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Notification;
use Illuminate\Support\Facades\Password;
use Symfony\Component\Mailer\Exception\TransportException;

it('may send password reset notification', function (): void {
    Notification::fake();
    Event::fake([PasswordResetLinkSent::class]);

    $user = User::factory()->create([
        'email' => 'test@example.com',
    ]);

    $action = resolve(CreateUserEmailResetNotification::class);

    $status = $action->handle(['email' => $user->email]);

    expect($status)->toBe(Password::RESET_LINK_SENT);

    Notification::assertSentTo($user, ResetPassword::class);
    Event::assertDispatchedTimes(PasswordResetLinkSent::class, 1);
    Event::assertDispatched(PasswordResetLinkSent::class, fn (PasswordResetLinkSent $event): bool => $event->user->is($user));
});

it('returns throttled status when too many attempts', function (): void {
    Notification::fake();
    $user = User::factory()->create([
        'email' => 'test@example.com',
    ]);

    $action = resolve(CreateUserEmailResetNotification::class);

    // Send multiple reset requests to trigger throttling
    $action->handle(['email' => $user->email]);

    $token = Notification::sent($user, ResetPassword::class)->sole()->token;

    $status = $action->handle(['email' => $user->email]);

    expect($status)->toBe(Password::RESET_THROTTLED);
    expect(Password::tokenExists($user, $token))->toBeTrue();
    Notification::assertSentToTimes($user, ResetPassword::class, 1);
});

it('returns invalid user status for non-existent email', function (): void {
    Notification::fake();
    $user = User::factory()->create();
    $token = Password::createToken($user);
    $action = resolve(CreateUserEmailResetNotification::class);

    $status = $action->handle(['email' => 'nonexistent@example.com']);

    expect($status)->toBe(Password::INVALID_USER);
    expect(Password::tokenExists($user, $token))->toBeTrue();
    Notification::assertNothingSent();
});

it('removes only the failed delivery token and propagates the exception without a success event', function (): void {
    $user = User::factory()->create();
    $otherUser = User::factory()->create();
    $otherToken = Password::createToken($otherUser);
    Event::fake([PasswordResetLinkSent::class]);
    $exception = new TransportException('Transport unavailable');
    $mailer = Mockery::mock(Mailer::class);
    $mailer->shouldReceive('send')->once()->andThrow($exception);
    $this->mock(Factory::class)->shouldReceive('mailer')->once()->with(null)->andReturn($mailer);

    expect(fn () => resolve(CreateUserEmailResetNotification::class)->handle(['email' => $user->email]))
        ->toThrow($exception);

    $this->assertDatabaseMissing('password_reset_tokens', ['email' => $user->email]);
    expect(Password::tokenExists($otherUser, $otherToken))->toBeTrue();
    Event::assertNotDispatched(PasswordResetLinkSent::class);
});
