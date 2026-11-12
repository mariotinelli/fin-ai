<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Notifications\ResetPassword;
use Illuminate\Auth\Notifications\VerifyEmail;
use Illuminate\Support\Facades\Notification;

it('mantém o percurso público e as ações do login por teclado', function (): void {
    $page = visit(route('home'))->resize(360, 800);

    $page->click('Log in')->assertSee('Log in to your account')
        ->assertSee('Sign in with a passkey')->assertNoJavaScriptErrors();
    $page->fill('email', 'pessoa@example.com')->keys('#email', 'Tab')
        ->assertScript('document.activeElement.id', 'password')
        ->keys('#password', 'Tab')
        ->assertScript('document.activeElement.id', 'remember')
        ->keys('#remember', 'Tab')
        ->assertScript('document.activeElement.dataset.test', 'login-button');
    $page->click('[aria-label="Show password"]')->assertAttribute('#password', 'type', 'text')
        ->click('[aria-label="Hide password"]')->assertAttribute('#password', 'type', 'password')
        ->click('Forgot password?')->assertSee('Forgot password')
        ->click('log in')->assertSee('Log in to your account')
        ->click('Sign up')->assertSee('Create an account')
        ->click('[aria-label="FinAI — início"]')->assertPathIs('/')
        ->click('Register')->assertSee('Create an account')
        ->assertNoJavaScriptErrors()
        ->assertScript('document.documentElement.scrollWidth <= innerWidth', true);
});

it('apresenta erro, processamento real e sucesso genérico na recuperação', function (): void {
    Notification::fake();
    $user = User::factory()->withoutTwoFactor()->create();
    $page = visit(route('password.request'));

    $page->click('@email-password-reset-link-button')
        ->assertSee(__('validation.required', ['attribute' => 'email']))
        ->fill('email', $user->email);
    $page->script(<<<'JS'
() => {
    const send = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function(body) {
        const xhr = this;
        window.releaseAccessRequest = () => {
            XMLHttpRequest.prototype.send = send;
            send.call(xhr, body);
            delete window.releaseAccessRequest;
        };
    };
}
JS);
    try {
        $page->click('@email-password-reset-link-button')
            ->assertDisabled('@email-password-reset-link-button')
            ->assertVisible('button .animate-spin')
            ->assertScript('typeof window.releaseAccessRequest', 'function')
            ->assertNoJavaScriptErrors();
    } finally {
        $page->script('() => window.releaseAccessRequest?.()');
    }

    $page->assertSee('A reset link will be sent if the account exists.')
        ->assertEnabled('@email-password-reset-link-button')
        ->assertNoJavaScriptErrors();
    Notification::assertSentTo($user, ResetPassword::class);
});

it('mantém reenvio e saída no aviso de verificação', function (): void {
    Notification::fake();
    $user = User::factory()->unverified()->withoutTwoFactor()->create();
    $this->actingAs($user);
    $page = visit(route('verification.notice'));

    $page->click('Resend verification email')
        ->assertSee('A new verification link has been sent')
        ->assertNoJavaScriptErrors()
        ->click('Log out')->assertPathIs('/')
        ->navigate(route('verification.notice'))->assertPathIs('/login')
        ->assertSee('Log in to your account')->assertNoJavaScriptErrors();

    $this->assertGuest();
    Notification::assertSentTo($user, VerifyEmail::class);
});

it('preserva sistema e escolha explícita entre inicial e acesso', function (string $mode, string $expected): void {
    $page = visit(route('home'))->inDarkMode();
    $page->script("localStorage.setItem('appearance', '$mode')");

    $page->refresh()->assertScript('document.documentElement.style.colorScheme', $expected)
        ->click('Log in')->assertSee('Log in to your account')
        ->assertScript('document.documentElement.style.colorScheme', $expected)
        ->click('Sign up')->assertSee('Create an account')
        ->assertScript('localStorage.getItem("appearance")', $mode)
        ->assertScript('document.documentElement.style.colorScheme', $expected)
        ->click('[aria-label="FinAI — início"]')->assertPathIs('/')
        ->assertScript('document.documentElement.style.colorScheme', $expected)
        ->assertNoJavaScriptErrors();
})->with([
    'sistema escuro' => ['system', 'dark'],
    'claro explícito em dispositivo escuro' => ['light', 'light'],
]);
