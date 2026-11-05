<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Notifications\ResetPassword;
use Illuminate\Contracts\Mail\Factory;
use Illuminate\Contracts\Mail\Mailer;
use Illuminate\Support\Facades\Exceptions;
use Illuminate\Support\Facades\Notification;
use Illuminate\Support\Facades\Password;
use Symfony\Component\Mailer\Exception\TransportException;

it('renders forgot password page', function (): void {
    $response = $this->fromRoute('home')
        ->get(route('password.request'));

    $response->assertOk()
        ->assertInertia(fn ($page) => $page
            ->component('user-email-reset-notification/create')
            ->has('status'));
});

it('may send password reset notification', function (): void {
    Notification::fake();

    $user = User::factory()->create([
        'email' => 'test@example.com',
    ]);

    $response = $this->fromRoute('password.request')
        ->post(route('password.email'), [
            'email' => 'test@example.com',
        ]);

    $response->assertRedirectToRoute('password.request')
        ->assertSessionHas('status', 'A reset link will be sent if the account exists.');

    Notification::assertSentTo($user, ResetPassword::class);
});

it('returns generic message for non-existent email', function (): void {
    Notification::fake();

    $response = $this->fromRoute('password.request')
        ->post(route('password.email'), [
            'email' => 'nonexistent@example.com',
        ]);

    $response->assertRedirectToRoute('password.request')
        ->assertSessionHas('status', 'A reset link will be sent if the account exists.');

    Notification::assertNothingSent();
});

it('requires email', function (): void {
    $response = $this->fromRoute('password.request')
        ->post(route('password.email'), []);

    $response->assertRedirectToRoute('password.request')
        ->assertSessionHasErrors('email');
});

it('keeps the same generic confirmation and usable token when throttled', function (): void {
    Notification::fake();
    $user = User::factory()->create();

    $this->fromRoute('password.request')->post(route('password.email'), ['email' => $user->email])
        ->assertSessionHas('status', 'A reset link will be sent if the account exists.')
        ->assertSessionMissing('retryMessage');
    $token = Notification::sent($user, ResetPassword::class)->sole()->token;

    $this->post(route('password.email'), ['email' => $user->email])
        ->assertRedirectToRoute('password.request')
        ->assertSessionHas('status', 'A reset link will be sent if the account exists.')
        ->assertSessionMissing('retryMessage');

    Notification::assertSentToTimes($user, ResetPassword::class, 1);
    expect(Password::tokenExists($user, $token))->toBeTrue();
});

it('reports delivery failure without success and sends a usable link on immediate retry', function (): void {
    $user = User::factory()->create();
    Exceptions::fake();
    $exception = new TransportException('smtp://private-host: secret transport failure');
    $mailer = Mockery::mock(Mailer::class);
    $mailer->shouldReceive('send')->once()->andThrow($exception);
    $this->mock(Factory::class)->shouldReceive('mailer')->once()->with(null)->andReturn($mailer);

    $this->withSession(['status' => 'A reset link will be sent if the account exists.'])
        ->fromRoute('password.request')->post(route('password.email'), ['email' => $user->email])
        ->assertRedirectToRoute('password.request')
        ->assertSessionHas('retryMessage', 'Unable to process your request. Please try again.')
        ->assertSessionMissing('status')
        ->assertSessionHasNoErrors();

    Exceptions::assertReported(fn (TransportException $reported): bool => $reported === $exception);
    $this->assertDatabaseMissing('password_reset_tokens', ['email' => $user->email]);
    $this->withCookie(config('session.cookie'), session()->getId())
        ->get(route('password.request'))->assertOk()->assertInertia(fn ($page) => $page
        ->component('user-email-reset-notification/create')
        ->where('retryMessage', 'Unable to process your request. Please try again.')
        ->where('status', null));

    Notification::fake();
    $this->fromRoute('password.request')->post(route('password.email'), ['email' => $user->email])
        ->assertRedirectToRoute('password.request')
        ->assertSessionHas('status', 'A reset link will be sent if the account exists.')
        ->assertSessionMissing('retryMessage');

    Notification::assertSentToOnce($user, ResetPassword::class);
    $token = Notification::sent($user, ResetPassword::class)->sole()->token;
    expect(Password::tokenExists($user, $token))->toBeTrue();
    $this->get(route('password.request'))->assertOk()->assertInertia(fn ($page) => $page
        ->where('status', 'A reset link will be sent if the account exists.')
        ->where('retryMessage', null));
});

it('requires valid email format', function (): void {
    $response = $this->fromRoute('password.request')
        ->post(route('password.email'), [
            'email' => 'not-an-email',
        ]);

    $response->assertRedirectToRoute('password.request')
        ->assertSessionHasErrors('email');
});

it('redirects authenticated users away from forgot password', function (): void {
    $user = User::factory()->create();

    $response = $this->actingAs($user)
        ->fromRoute('dashboard')
        ->get(route('password.request'));

    $response->assertRedirectToRoute('dashboard');
});
