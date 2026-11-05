<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Access\AuthorizationException;
use Illuminate\Auth\Events\Verified;
use Illuminate\Auth\Notifications\VerifyEmail;
use Illuminate\Routing\Exceptions\InvalidSignatureException;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Notification;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\URL;

it('may verify email', function (): void {
    Event::fake([Verified::class]);
    $user = User::factory()->create([
        'email_verified_at' => null,
    ]);

    $verificationUrl = URL::temporarySignedRoute(
        'verification.verify',
        now()->addMinutes(60),
        ['id' => $user->getKey(), 'hash' => sha1((string) $user->email)]
    );

    $response = $this->actingAs($user)
        ->fromRoute('verification.notice')
        ->get($verificationUrl);

    expect($user->refresh()->hasVerifiedEmail())->toBeTrue();

    $response->assertRedirect(route('dashboard', absolute: false).'?verified=1');

    $verifiedAt = $user->email_verified_at;
    $this->get(route('dashboard'))->assertOk();
    $this->travel(1)->minutes();
    $this->get($verificationUrl)->assertRedirect(route('dashboard', absolute: false).'?verified=1');
    expect($user->refresh()->email_verified_at)->toEqual($verifiedAt);
    Event::assertDispatchedTimes(Verified::class, 1);
});

it('redirects to dashboard if already verified', function (): void {
    $user = User::factory()->create([
        'email_verified_at' => now(),
    ]);

    $verificationUrl = URL::temporarySignedRoute(
        'verification.verify',
        now()->addMinutes(60),
        ['id' => $user->getKey(), 'hash' => sha1((string) $user->email)]
    );

    $response = $this->actingAs($user)
        ->fromRoute('verification.notice')
        ->get($verificationUrl);

    $response->assertRedirect(route('dashboard', absolute: false).'?verified=1');

    expect($user->refresh()->hasVerifiedEmail())->toBeTrue();
    $this->get(route('dashboard'))->assertOk();
});

it('offers a new link without verifying either account when the link is refused', function (string $reason): void {
    Notification::fake();
    Event::fake([Verified::class]);
    $user = User::factory()->unverified()->create();
    $otherUser = User::factory()->unverified()->create();
    $parameters = ['id' => $user->getKey(), 'hash' => sha1((string) $user->email)];
    $invalidUrl = match ($reason) {
        'unsigned' => route('verification.verify', $parameters),
        'tampered' => URL::temporarySignedRoute('verification.verify', now()->addHour(), $parameters).'&signature=invalid',
        'expired' => URL::temporarySignedRoute('verification.verify', now()->addMinute(), $parameters),
        'other account' => URL::temporarySignedRoute('verification.verify', now()->addHour(), [
            'id' => $otherUser->getKey(), 'hash' => sha1((string) $otherUser->email),
        ]),
        'wrong hash' => URL::temporarySignedRoute('verification.verify', now()->addHour(), [
            'id' => $user->getKey(), 'hash' => sha1((string) $otherUser->email),
        ]),
    };

    $this->travel(2)->minutes();

    $response = $this->actingAs($user)
        ->withSession(['status' => 'verification-link-sent'])
        ->get($invalidUrl);

    $response->assertRedirectToRoute('verification.notice')
        ->assertSessionHasErrors([
            'email' => 'Não foi possível confirmar seu e-mail com este link. Solicite um novo link de confirmação.',
        ])
        ->assertSessionMissing('status');
    $this->withCookie(config('session.cookie'), session()->getId())
        ->get(route('verification.notice'))->assertOk()->assertInertia(fn ($page) => $page
        ->component('user-email-verification-notification/create')
        ->where('errors.email', 'Não foi possível confirmar seu e-mail com este link. Solicite um novo link de confirmação.')
        ->where('status', null));
    $this->get(route('dashboard'))->assertRedirectToRoute('verification.notice');
    expect($user->fresh()->email_verified_at)->toBeNull();
    expect($otherUser->fresh()->email_verified_at)->toBeNull();
    Event::assertNotDispatched(Verified::class);

    $this->fromRoute('verification.notice')->post(route('verification.send'))
        ->assertRedirectToRoute('verification.notice')
        ->assertSessionHas('status', 'verification-link-sent');
    Notification::assertSentToOnce($user, VerifyEmail::class);
    Notification::assertNotSentTo($otherUser, VerifyEmail::class);
    expect($user->fresh()->email_verified_at)->toBeNull();
    $this->get(route('dashboard'))->assertRedirectToRoute('verification.notice');
})->with(['unsigned', 'tampered', 'expired', 'other account', 'wrong hash']);

it('preserves a valid verification destination through login', function (): void {
    $user = User::factory()->unverified()->withoutTwoFactor()->create();
    $verificationUrl = URL::temporarySignedRoute('verification.verify', now()->addHour(), [
        'id' => $user->getKey(), 'hash' => sha1((string) $user->email),
    ]);

    $this->get($verificationUrl)->assertRedirectToRoute('login')
        ->assertSessionHas('url.intended', $verificationUrl);
    $this->assertGuest();
    expect($user->fresh()->email_verified_at)->toBeNull();

    $this->post(route('login.store'), ['email' => $user->email, 'password' => 'password'])
        ->assertRedirect($verificationUrl);
    $this->assertAuthenticatedAs($user);
    expect($user->fresh()->email_verified_at)->toBeNull();
    $this->get($verificationUrl)->assertRedirect(route('dashboard', absolute: false).'?verified=1');
    expect($user->fresh()->hasVerifiedEmail())->toBeTrue();
    $this->get(route('dashboard'))->assertOk();
});

it('preserves forbidden responses outside verification', function (string $exceptionClass): void {
    Route::get('/test-forbidden', fn (): never => throw new $exceptionClass)->middleware('web')->name('test.forbidden');

    $this->get('/test-forbidden')->assertForbidden()->assertSessionHasNoErrors();
})->with([InvalidSignatureException::class, AuthorizationException::class]);

it('preserves unrelated forbidden responses on the verification route', function (): void {
    Route::get('/test-verification-forbidden', fn () => abort(403))->middleware('web')->name('verification.verify');

    $this->get('/test-verification-forbidden')->assertForbidden()->assertSessionHasNoErrors();
});
