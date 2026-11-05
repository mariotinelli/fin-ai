<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Events\Registered;
use Illuminate\Auth\Notifications\VerifyEmail;
use Illuminate\Contracts\Mail\Factory;
use Illuminate\Contracts\Mail\Mailer;
use Illuminate\Contracts\Validation\UncompromisedVerifier;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Exceptions;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Notification;
use Illuminate\Validation\Rules\Password;
use Symfony\Component\Mailer\Exception\TransportException;

it('renders registration page', function (): void {
    $response = $this->fromRoute('home')
        ->get(route('register'));

    $response->assertOk()
        ->assertInertia(fn ($page) => $page
            ->component('user/create')
            ->where('passwordRules', Password::defaults()->toPasswordRulesString()));
});

it('may register a new user', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    Notification::fake();

    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'name' => 'Test User',
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('dashboard');

    $this->assertDatabaseCount('users', 1);

    $user = User::query()->where('email', 'test@example.com')->first();

    expect($user)->not->toBeNull()
        ->and($user->name)->toBe('Test User')
        ->and($user->email)->toBe('test@example.com')
        ->and($user->email_verified_at)->toBeNull()
        ->and(Hash::check('Valid-pass12!', $user->password))->toBeTrue();

    $this->assertAuthenticatedAs($user);

    Notification::assertSentToOnce($user, VerifyEmail::class);

    $this->get(route('dashboard'))->assertRedirectToRoute('verification.notice');
});

it('rolls back registration when mail transport fails and allows retrying the same data', function (): void {
    Exceptions::fake();
    $exception = new TransportException('smtp://private-host: secret transport failure');
    $mailer = Mockery::mock(Mailer::class);
    $mailer->shouldReceive('send')->once()->andThrow($exception);
    $this->mock(Factory::class)->shouldReceive('mailer')->once()->with(null)->andReturn($mailer);
    $this->mock(UncompromisedVerifier::class)->shouldReceive('verify')->twice()->andReturnTrue();

    $data = [
        'name' => 'Test User',
        'email' => 'test@example.com',
        'password' => 'Valid-pass12!',
        'password_confirmation' => 'Valid-pass12!',
    ];

    $this->fromRoute('register')->post(route('register.store'), $data)
        ->assertRedirectToRoute('register')
        ->assertSessionHasErrors([
            'email' => 'We could not send your verification email. Please try registering again.',
        ])
        ->assertSessionMissing('status');

    $this->assertDatabaseEmpty('users');
    $this->assertGuest();
    Exceptions::assertReported(fn (TransportException $reported): bool => $reported === $exception);
    $this->withCookie(config('session.cookie'), session()->getId())
        ->get(route('register'))->assertOk()->assertInertia(fn ($page) => $page
        ->where('errors.email', 'We could not send your verification email. Please try registering again.'));

    Notification::fake();

    $this->fromRoute('register')->post(route('register.store'), $data)
        ->assertRedirectToRoute('dashboard')->assertSessionHasNoErrors();

    $this->assertDatabaseCount('users', 1);
    $user = User::query()->sole();
    expect($user->email_verified_at)->toBeNull();
    $this->assertAuthenticatedAs($user);
    Notification::assertSentToOnce($user, VerifyEmail::class);
    $this->get(route('dashboard'))->assertRedirectToRoute('verification.notice');
});

it('requires name', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('register')
        ->assertSessionHasErrors('name');

    $this->assertDatabaseEmpty('users');
});

it('requires email', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'name' => 'Test User',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('register')
        ->assertSessionHasErrors('email');

    $this->assertDatabaseEmpty('users');
});

it('requires valid email', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'name' => 'Test User',
            'email' => 'not-an-email',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('register')
        ->assertSessionHasErrors('email');

    $this->assertDatabaseEmpty('users');
});

it('requires unique email', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    User::factory()->create(['email' => 'test@example.com']);

    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'name' => 'Test User',
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('register')
        ->assertSessionHasErrors('email');

    $this->assertDatabaseCount('users', 1);
});

it('requires password', function (): void {
    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'name' => 'Test User',
            'email' => 'test@example.com',
        ]);

    $response->assertRedirectToRoute('register')
        ->assertSessionHasErrors('password');

    $this->assertDatabaseEmpty('users');
});

it('requires password confirmation', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'name' => 'Test User',
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
        ]);

    $response->assertRedirectToRoute('register')
        ->assertSessionHasErrors('password');

    $this->assertDatabaseEmpty('users');
});

it('requires matching password confirmation', function (): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')
        ->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])
        ->andReturnTrue();

    $response = $this->fromRoute('register')
        ->post(route('register.store'), [
            'name' => 'Test User',
            'email' => 'test@example.com',
            'password' => 'Valid-pass12!',
            'password_confirmation' => 'different-password',
        ]);

    $response->assertRedirectToRoute('register')
        ->assertSessionHasErrors('password');

    $this->assertDatabaseEmpty('users');
});

it('may delete user account', function (): void {
    $user = User::factory()->create([
        'password' => Hash::make('password'),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('user-profile.edit')
        ->delete(route('user.destroy'), [
            'password' => 'password',
        ]);

    $response->assertRedirectToRoute('home');

    expect($user->fresh())->toBeNull();

    $this->assertGuest();
});

it('requires password to delete account', function (): void {
    $user = User::factory()->create();

    $response = $this->actingAs($user)
        ->fromRoute('user-profile.edit')
        ->delete(route('user.destroy'), []);

    $response->assertRedirectToRoute('user-profile.edit')
        ->assertSessionHasErrors('password');

    expect($user->fresh())->not->toBeNull();
});

it('requires correct password to delete account', function (): void {
    $user = User::factory()->create([
        'password' => Hash::make('password'),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('user-profile.edit')
        ->delete(route('user.destroy'), [
            'password' => 'wrong-password',
        ]);

    $response->assertRedirectToRoute('user-profile.edit')
        ->assertSessionHasErrors('password');

    expect($user->fresh())->not->toBeNull();
});

it('redirects authenticated users away from registration', function (): void {
    $user = User::factory()->create();

    $response = $this->actingAs($user)
        ->fromRoute('dashboard')
        ->get(route('register'));

    $response->assertRedirectToRoute('dashboard');
});

it('requires verified email to delete account', function (): void {
    $user = User::factory()->unverified()->create([
        'password' => Hash::make('password'),
    ]);

    $response = $this->actingAs($user)
        ->fromRoute('user-profile.edit')
        ->delete(route('user.destroy'), [
            'password' => 'password',
        ]);

    $response->assertRedirectToRoute('verification.notice');

    expect($user->fresh())->not->toBeNull();
});

it('rejects passwords outside the registration policy', function (string $password): void {
    Event::fake([Registered::class]);
    $this->mock(UncompromisedVerifier::class)->shouldNotReceive('verify');

    $this->fromRoute('register')->post(route('register.store'), [
        'name' => 'Test User',
        'email' => 'test@example.com',
        'password' => $password,
        'password_confirmation' => $password,
    ])->assertRedirectToRoute('register')->assertSessionHasErrors('password');

    $this->assertDatabaseEmpty('users');
    $this->assertGuest();
    Event::assertNotDispatched(Registered::class);
})->with([
    'below 12 characters' => ['Abcdefgh1!x'],
    'above 255 characters' => [str_repeat('a', 253).'A1!'],
    'without uppercase' => ['abcdefghij1!'],
    'without lowercase' => ['ABCDEFGHIJ1!'],
    'without number' => ['Abcdefghijk!'],
    'without symbol' => ['Abcdefghijk1'],
]);

it('accepts registration passwords at the policy boundaries', function (string $password): void {
    Event::fake([Registered::class]);
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')->once()
        ->with(['value' => $password, 'threshold' => 0])->andReturnTrue();

    $this->fromRoute('register')->post(route('register.store'), [
        'name' => 'Test User',
        'email' => 'test@example.com',
        'password' => $password,
        'password_confirmation' => $password,
    ])->assertRedirectToRoute('dashboard')->assertSessionHasNoErrors();

    $this->assertDatabaseCount('users', 1);
    $user = User::query()->sole();
    expect(Hash::check($password, $user->password))->toBeTrue();
    $this->assertAuthenticatedAs($user);
    Event::assertDispatchedTimes(Registered::class, 1);
})->with([
    '12 characters' => ['Abcdefghij1!'],
    '255 characters' => [str_repeat('a', 252).'A1!'],
]);

it('rejects compromised registration passwords', function (): void {
    Event::fake([Registered::class]);
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])->andReturnFalse();

    $this->fromRoute('register')->post(route('register.store'), [
        'name' => 'Test User',
        'email' => 'test@example.com',
        'password' => 'Valid-pass12!',
        'password_confirmation' => 'Valid-pass12!',
    ])->assertRedirectToRoute('register')->assertSessionHasErrors('password');

    $this->assertDatabaseEmpty('users');
    $this->assertGuest();
    Event::assertNotDispatched(Registered::class);
});

it('rejects registration fields longer than 255 characters', function (string $field, string $value): void {
    $this->mock(UncompromisedVerifier::class)
        ->shouldReceive('verify')->once()
        ->with(['value' => 'Valid-pass12!', 'threshold' => 0])->andReturnTrue();

    $this->fromRoute('register')->post(route('register.store'), [
        'name' => 'Test User',
        'email' => 'test@example.com',
        'password' => 'Valid-pass12!',
        'password_confirmation' => 'Valid-pass12!',
        $field => $value,
    ])->assertRedirectToRoute('register')->assertSessionHasErrors([
        $field => __('validation.max.string', ['attribute' => $field, 'max' => 255]),
    ]);

    $this->assertDatabaseEmpty('users');
})->with([
    'name' => ['name', str_repeat('a', 256)],
    'email' => ['email', str_repeat('a', 64).'@'.str_repeat('b', 63).'.'.str_repeat('c', 63).'.'.str_repeat('d', 61).'.com'],
]);
