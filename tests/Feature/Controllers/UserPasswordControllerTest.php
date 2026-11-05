<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Events\PasswordReset;
use Illuminate\Contracts\Validation\UncompromisedVerifier;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Password;
use Illuminate\Validation\Rules\Password as PasswordRule;

it('renders reset password page', function (): void {
    $response = $this->fromRoute('home')
        ->get(route('password.reset', ['token' => 'fake-token']));

    $response->assertOk()
        ->assertInertia(fn ($page) => $page
            ->component('user-password/create')
            ->has('email')
            ->has('token')
            ->where('passwordRules', PasswordRule::defaults()->toPasswordRulesString()));
});

it('may reset password', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    Event::fake([PasswordReset::class]);

    $user = User::factory()->unverified()->withoutTwoFactor()->create([
        'email' => 'test@example.com',
        'password' => 'Previous-pass12!',
    ]);

    $token = Password::createToken($user);

    $response = $this->fromRoute('password.reset', ['token' => $token])
        ->post(route('password.store'), [
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
            'token' => $token,
        ]);

    $response->assertRedirectToRoute('login')
        ->assertSessionHas('status');

    expect(Hash::check('Valid-pass12!', $user->refresh()->password))->toBeTrue()
        ->and($user->email_verified_at)->toBeNull();

    Event::assertDispatched(PasswordReset::class);

    $this->assertGuest();

    $this->fromRoute('login')->post(route('login.store'), [
        'email' => $user->email,
        'password' => 'Previous-pass12!',
    ])->assertRedirectToRoute('login')->assertSessionHasErrors('email');

    $this->assertGuest();

    $this->fromRoute('login')->post(route('login.store'), [
        'email' => $user->email,
        'password' => 'Valid-pass12!',
    ])->assertRedirectToRoute('dashboard');

    $this->assertAuthenticatedAs($user);
    $this->get(route('dashboard'))->assertRedirectToRoute('verification.notice');
    expect($user->refresh()->email_verified_at)->toBeNull();
});

it('fails with invalid token', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $user = User::factory()->create([
        'email' => 'test@example.com',
    ]);

    $response = $this->fromRoute('password.reset', ['token' => 'invalid-token'])
        ->post(route('password.store'), [
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
            'token' => 'invalid-token',
        ]);

    $response->assertRedirect(route('password.reset', ['token' => 'invalid-token']))
        ->assertSessionHasErrors('email');
});

it('fails with non-existent email', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $response = $this->fromRoute('password.reset', ['token' => 'fake-token'])
        ->post(route('password.store'), [
            'email' => 'nonexistent@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
            'token' => 'fake-token',
        ]);

    $response->assertRedirect(route('password.reset', ['token' => 'fake-token']))
        ->assertSessionHasErrors('email');
});

it('requires email', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $user = User::factory()->create();
    $originalHash = $user->password;
    $token = Password::createToken($user);

    $response = $this->fromRoute('password.reset', ['token' => $token])
        ->post(route('password.store'), [
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
            'token' => $token,
        ]);

    $response->assertRedirect(route('password.reset', ['token' => $token]))
        ->assertSessionHasErrors('email');

    expect($user->refresh()->password)->toBe($originalHash);
});

it('requires password', function (): void {
    $user = User::factory()->create(['email' => 'test@example.com']);
    $originalHash = $user->password;
    $token = Password::createToken($user);

    $response = $this->fromRoute('password.reset', ['token' => $token])
        ->post(route('password.store'), [
            'email' => 'test@example.com',
            'token' => $token,
        ]);

    $response->assertRedirect(route('password.reset', ['token' => $token]))
        ->assertSessionHasErrors('password');

    expect($user->refresh()->password)->toBe($originalHash);
});

it('requires password confirmation', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $user = User::factory()->create(['email' => 'test@example.com']);
    $originalHash = $user->password;
    $token = Password::createToken($user);

    $response = $this->fromRoute('password.reset', ['token' => $token])
        ->post(route('password.store'), [
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'token' => $token,
        ]);

    $response->assertRedirect(route('password.reset', ['token' => $token]))
        ->assertSessionHasErrors('password');

    expect($user->refresh()->password)->toBe($originalHash);
});

it('requires matching password confirmation', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $user = User::factory()->create(['email' => 'test@example.com']);
    $originalHash = $user->password;
    $token = Password::createToken($user);

    $response = $this->fromRoute('password.reset', ['token' => $token])
        ->post(route('password.store'), [
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'different-password',
            'token' => $token,
        ]);

    $response->assertRedirect(route('password.reset', ['token' => $token]))
        ->assertSessionHasErrors('password');

    expect($user->refresh()->password)->toBe($originalHash);
});

it('renders edit password page', function (): void {
    $user = User::factory()->create();

    $response = $this->actingAs($user)
        ->fromRoute('dashboard')
        ->get(route('password.edit'));

    $response->assertOk()
        ->assertInertia(fn ($page) => $page
            ->component('user-password/edit')
            ->where('passwordRules', PasswordRule::defaults()->toPasswordRulesString()));
});

it('requires verified email to edit password', function (): void {
    $user = User::factory()->unverified()->create();

    $response = $this->actingAs($user)
        ->fromRoute('dashboard')
        ->get(route('password.edit'));

    $response->assertRedirectToRoute('verification.notice');
});

it('may update password', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $user = User::factory()->create([
        'password' => Hash::make('old-password'),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('password.edit')
        ->put(route('password.update'), [
            'current_password' => 'old-password',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('password.edit')
        ->assertInertiaFlash('toast', ['type' => 'success', 'message' => __('Password updated.')]);

    expect(Hash::check('Valid-pass12!', $user->refresh()->password))->toBeTrue();
});

it('requires current password to update', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $user = User::factory()->create();

    $response = $this->actingAs($user)
        ->fromRoute('password.edit')
        ->put(route('password.update'), [
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('password.edit')
        ->assertSessionHasErrors('current_password');
});

it('requires correct current password to update', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $user = User::factory()->create([
        'password' => Hash::make('old-password'),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('password.edit')
        ->put(route('password.update'), [
            'current_password' => 'wrong-password',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('password.edit')
        ->assertSessionHasErrors('current_password');
});

it('requires new password to update', function (): void {
    $user = User::factory()->create([
        'password' => Hash::make('old-password'),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('password.edit')
        ->put(route('password.update'), [
            'current_password' => 'old-password',
        ]);

    $response->assertRedirectToRoute('password.edit')
        ->assertSessionHasErrors('password');
});

it('redirects authenticated users away from reset password', function (): void {
    $user = User::factory()->create();

    $response = $this->actingAs($user)
        ->fromRoute('dashboard')
        ->get(route('password.reset', ['token' => 'fake-token']));

    $response->assertRedirectToRoute('dashboard');
});

it('rejects passwords outside the reset policy without changing the hash', function (string $password): void {
    $user = User::factory()->create();
    $originalHash = $user->password;
    $token = Password::createToken($user);
    Event::fake([PasswordReset::class]);
    $this->mock(UncompromisedVerifier::class)->shouldNotReceive('verify');

    $this->fromRoute('password.reset', ['token' => $token])->post(route('password.store'), [
        'email' => $user->email,
        'token' => $token,
        'password' => $password,
        'password_confirmation' => $password,
    ])->assertRedirectToRoute('password.reset', ['token' => $token])->assertSessionHasErrors('password');

    expect($user->refresh()->password)->toBe($originalHash);
    $this->assertGuest();
    Event::assertNotDispatched(PasswordReset::class);
})->with([
    'below 12 characters' => ['Abcdefgh1!x'],
    'above 255 characters' => [str_repeat('a', 253).'A1!'],
    'without uppercase' => ['abcdefghij1!'],
    'without lowercase' => ['ABCDEFGHIJ1!'],
    'without number' => ['Abcdefghijk!'],
    'without symbol' => ['Abcdefghijk1'],
]);

it('accepts reset passwords at the policy boundaries', function (string $password): void {
    $user = User::factory()->create();
    $token = Password::createToken($user);
    Event::fake([PasswordReset::class]);
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')->once()
        ->with(['value' => $password, 'threshold' => 0])->andReturnTrue();

    $this->fromRoute('password.reset', ['token' => $token])->post(route('password.store'), [
        'email' => $user->email,
        'token' => $token,
        'password' => $password,
        'password_confirmation' => $password,
    ])->assertRedirectToRoute('login')->assertSessionHasNoErrors();

    expect(Hash::check($password, $user->refresh()->password))->toBeTrue();
    Event::assertDispatchedTimes(PasswordReset::class, 1);
})->with([
    '12 characters' => ['Abcdefghij1!'],
    '255 characters' => [str_repeat('a', 252).'A1!'],
]);

it('rejects compromised reset passwords without changing the hash', function (): void {
    $user = User::factory()->create();
    $originalHash = $user->password;
    $token = Password::createToken($user);
    Event::fake([PasswordReset::class]);
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])->andReturnFalse();

    $this->fromRoute('password.reset', ['token' => $token])->post(route('password.store'), [
        'email' => $user->email,
        'token' => $token,
        'password' => 'Valid-pass12!',
        'password_confirmation' => 'Valid-pass12!',
    ])->assertRedirectToRoute('password.reset', ['token' => $token])->assertSessionHasErrors('password');

    expect($user->refresh()->password)->toBe($originalHash);
    $this->assertGuest();
    Event::assertNotDispatched(PasswordReset::class);
});

it('rejects invalid reset email without changing the hash', function (): void {
    $user = User::factory()->create();
    $originalHash = $user->password;
    $token = Password::createToken($user);
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])->andReturnTrue();

    $this->fromRoute('password.reset', ['token' => $token])->post(route('password.store'), [
        'email' => 'not-an-email',
        'token' => $token,
        'password' => 'Valid-pass12!',
        'password_confirmation' => 'Valid-pass12!',
    ])->assertRedirectToRoute('password.reset', ['token' => $token])->assertSessionHasErrors('email');

    expect($user->refresh()->password)->toBe($originalHash);
});
