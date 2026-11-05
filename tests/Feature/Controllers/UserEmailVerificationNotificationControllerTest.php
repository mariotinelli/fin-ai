<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Notifications\VerifyEmail;
use Illuminate\Contracts\Mail\Factory;
use Illuminate\Contracts\Mail\Mailer;
use Illuminate\Notifications\Events\NotificationSent;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Exceptions;
use Illuminate\Support\Facades\Notification;
use Symfony\Component\Mailer\Exception\TransportException;

it('renders verify email page', function (): void {
    $user = User::factory()->create([
        'email_verified_at' => null,
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('home')
        ->get(route('verification.notice'));

    $response->assertOk()
        ->assertInertia(fn ($page) => $page
            ->component('user-email-verification-notification/create')
            ->has('status'));
});

it('redirects verified users to dashboard', function (): void {
    $user = User::factory()->create([
        'email_verified_at' => now(),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('home')
        ->get(route('verification.notice'));

    $response->assertRedirectToRoute('dashboard');
});

it('may send verification notification', function (): void {
    Notification::fake();

    $user = User::factory()->create([
        'email_verified_at' => null,
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('verification.notice')
        ->post(route('verification.send'));

    $response->assertRedirectToRoute('verification.notice')
        ->assertSessionHas('status', 'verification-link-sent');

    Notification::assertSentTo($user, VerifyEmail::class);
    expect($user->fresh()->email_verified_at)->toBeNull();
    $this->get(route('dashboard'))->assertRedirectToRoute('verification.notice');
});

it('redirects verified users when sending notification', function (): void {
    Notification::fake();

    $user = User::factory()->create([
        'email_verified_at' => now(),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('verification.notice')
        ->post(route('verification.send'));

    $response->assertRedirectToRoute('dashboard');

    Notification::assertNothingSent();
});

it('shows a retry error without success when transport fails and allows resending after recovery', function (): void {
    $user = User::factory()->unverified()->create();
    Exceptions::fake();
    Event::fake([NotificationSent::class]);
    $exception = new TransportException('smtp://private-host: secret transport failure');
    $mailer = Mockery::mock(Mailer::class);
    $mailer->shouldReceive('send')->once()->andThrow($exception);
    $this->mock(Factory::class)->shouldReceive('mailer')->once()->with(null)->andReturn($mailer);

    $this->actingAs($user)->withSession(['status' => 'verification-link-sent'])
        ->fromRoute('verification.notice')->post(route('verification.send'))
        ->assertRedirectToRoute('verification.notice')
        ->assertSessionHasErrors([
            'email' => 'Não foi possível enviar seu e-mail de confirmação. Tente novamente.',
        ])
        ->assertSessionMissing('status');

    Exceptions::assertReported(fn (TransportException $reported): bool => $reported === $exception);
    Event::assertNotDispatched(NotificationSent::class);
    $this->withCookie(config('session.cookie'), session()->getId())
        ->get(route('verification.notice'))->assertOk()->assertInertia(fn ($page) => $page
        ->component('user-email-verification-notification/create')
        ->where('errors.email', 'Não foi possível enviar seu e-mail de confirmação. Tente novamente.')
        ->where('status', null));

    Notification::fake();

    $this->fromRoute('verification.notice')->post(route('verification.send'))
        ->assertRedirectToRoute('verification.notice')
        ->assertSessionHasNoErrors()
        ->assertSessionHas('status', 'verification-link-sent');

    Notification::assertSentToOnce($user, VerifyEmail::class);
    $this->get(route('verification.notice'))->assertOk()->assertInertia(fn ($page) => $page
        ->where('status', 'verification-link-sent'));
    expect($user->fresh()->email_verified_at)->toBeNull();
    $this->get(route('dashboard'))->assertRedirectToRoute('verification.notice');
});
