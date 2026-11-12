<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Notifications\VerifyEmail;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Notification;

it('preserva os dados inválidos do perfil e permite reenviar a verificação', function (): void {
    Notification::fake();
    $user = User::factory()->unverified()->withoutTwoFactor()->create();
    User::factory()->create(['email' => 'ocupado@example.test']);
    $this->actingAs($user);

    $page = visit(route('user-profile.edit'));
    $page->fill('name', 'Nome preservado')->fill('email', 'ocupado@example.test')
        ->click('@update-profile-button')->assertSee(__('validation.unique', ['attribute' => 'email']))
        ->assertValue('name', 'Nome preservado')->assertValue('email', 'ocupado@example.test')
        ->click('Click here to resend the verification email.')
        ->assertSee('A new verification link has been sent to your email address.')
        ->assertPathIs('/settings/profile')->assertNoJavaScriptErrors();

    expect($user->fresh()->email)->toBe($user->email);
    Notification::assertSentTo($user, VerifyEmail::class);
});

it('mantém foco e limpa as senhas após erro e sucesso', function (): void {
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user);
    $page = visit(route('password.edit'));

    $page->fill('current_password', 'incorreta')->fill('password', 'Nova-Senha-123!')
        ->fill('password_confirmation', 'Nova-Senha-123!')->click('@update-password-button')
        ->assertSee(__('validation.current_password'))
        ->assertScript('document.activeElement.id', 'current_password')
        ->assertValue('current_password', '')->assertValue('password', '')
        ->fill('current_password', 'password')->fill('password', 'Nova-Senha-123!')
        ->fill('password_confirmation', 'Diferente-123!')->click('@update-password-button')
        ->assertSee(__('validation.confirmed', ['attribute' => 'password']))
        ->assertScript('document.activeElement.id', 'password');
    expect(Hash::check('password', $user->fresh()->password))->toBeTrue();

    $page->fill('current_password', 'password')->fill('password', 'Nova-Senha-123!')
        ->fill('password_confirmation', 'Nova-Senha-123!')->click('@update-password-button')
        ->assertSee('Password updated.')->assertValue('current_password', '')
        ->assertValue('password', '')->assertValue('password_confirmation', '')
        ->assertNoJavaScriptErrors();
    expect(Hash::check('Nova-Senha-123!', $user->fresh()->password))->toBeTrue();
});

it('preserva conta e sessão ao errar a senha e fechar a confirmação', function (string $close): void {
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user);
    $page = visit(route('user-profile.edit'));

    $page->click('@delete-user-button')->fill('password', 'incorreta')
        ->click('@confirm-delete-user-button')->assertSee(__('validation.current_password'))
        ->assertScript('document.activeElement.id', 'password');
    for ($index = 0; $index < 6; $index++) {
        $page->keys(':focus', 'Tab')
            ->assertScript('document.querySelector("[role=dialog]").contains(document.activeElement)', true);
    }

    if ($close === 'Escape') {
        $page->keys('[role=dialog] input', 'Escape');
    } else {
        $page->click($close);
    }

    $page->assertMissing('[role=dialog]')
        ->assertScript('document.activeElement.dataset.test', 'delete-user-button')
        ->click('@delete-user-button')->assertValue('password', '')
        ->assertNoJavaScriptErrors();
    $this->assertModelExists($user);
    $this->assertAuthenticatedAs($user);
})->with(['Cancel', 'Close', 'Escape']);

it('mantém as consumidoras irmãs e seus destinos de configuração', function (): void {
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user)->session(['auth.password_confirmed_at' => time()]);
    $page = visit(route('user-profile.edit'));

    $page->click('Two-Factor Auth')->assertSee('Two-factor authentication')
        ->assertNoJavaScriptErrors()->click('Passkeys')->assertSee('Add passkey')
        ->assertNoJavaScriptErrors()->click('Password')->assertSee('Update password')
        ->assertNoJavaScriptErrors();
});
