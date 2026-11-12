<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Vite;
use Pest\Browser\Playwright\Client;
use Tests\TestCase;

pest()->extend(TestCase::class)->use(RefreshDatabase::class)->in(__DIR__);

it('captura configurações com estado real', function (string $surface, string $state, string $theme, int $width, int $height): void {
    config(['inertia.ssr.enabled' => false]);
    Vite::useHotFile(__DIR__.'/no-hot-file');
    $factory = User::factory()->withoutTwoFactor();
    if (in_array($state, ['unverified', 'resent'], true)) {
        $factory = $factory->unverified();
    }
    $user = $factory->create(['name' => 'Pessoa de teste', 'email' => 'pessoa@example.test']);
    $this->actingAs($user);
    $route = match ($surface) {
        'password' => 'password.edit',
        'appearance' => 'appearance.edit',
        default => 'user-profile.edit',
    };
    $expected = match ($surface) {
        'password' => 'Update password',
        'appearance' => 'Appearance settings',
        default => 'Profile information',
    };
    $page = visit(route($route))->resize($width, $height);
    $page->script("localStorage.setItem('appearance', '$theme')");
    $page->refresh()->assertSee($expected);
    if ($state === 'system') {
        $guid = new ReflectionProperty($page->page(), 'guid')->getValue($page->page());
        assert(is_string($guid));
        iterator_to_array(Client::instance()->execute($guid, 'emulateMedia', ['colorScheme' => $theme]));
        $page->click('System')->assertScript('localStorage.getItem("appearance")', 'system');
    } elseif ($surface === 'appearance') {
        $page->click($theme === 'dark' ? 'Dark' : 'Light');
    }
    if ($surface === 'deletion') {
        $page->click('@delete-user-button')->assertVisible('[role=dialog]');
    }
    $focus = match ($surface) {
        'password' => '#current_password',
        'appearance' => 'button[aria-pressed=true]',
        'deletion' => '[role=dialog] input',
        default => '#name',
    };
    $button = match ($surface) {
        'password' => '@update-password-button',
        'deletion' => '@confirm-delete-user-button',
        default => '@update-profile-button',
    };
    $held = $state === 'processing';
    try {
        if ($held) {
            $page->script(<<<'JS'
(() => {
    window.captureSend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function(body) {
        window.captureHeld = {xhr: this, body};
    };
})()
JS);
        }
        if ($surface === 'profile' && in_array($state, ['error', 'success', 'processing'], true)) {
            if ($state === 'error') {
                User::factory()->create(['email' => 'ocupado@example.test']);
                $page->fill('email', 'ocupado@example.test');
            }
            $page->fill('name', 'Nome atualizado')->click($button);
            if ($state === 'error') {
                $page->assertSee(__('validation.unique', ['attribute' => 'email']))->assertValue('email', 'ocupado@example.test');
            } elseif ($state === 'success') {
                $page->assertSee('Profile updated.');
                expect($user->fresh()->name)->toBe('Nome atualizado');
            }
        } elseif ($surface === 'password' && $state !== 'default') {
            $page->fill('current_password', $state === 'error' ? 'incorreta' : 'password')
                ->fill('password', 'Nova-Senha-123!')
                ->fill('password_confirmation', $state === 'error' ? 'Diferente-123!' : 'Nova-Senha-123!')
                ->click($button);
            if ($state === 'error') {
                $page->assertSee(__('validation.current_password'))
                    ->assertSee(__('validation.confirmed', ['attribute' => 'password']))
                    ->assertScript('document.activeElement.id', 'current_password');
            } elseif ($state === 'success') {
                $page->assertSee('Password updated.')->assertValue('password', '');
            }
        } elseif ($surface === 'deletion' && $state !== 'default') {
            $page->fill('password', $state === 'error' ? 'incorreta' : 'password')->click($button);
            if ($state === 'error') {
                $page->assertSee(__('validation.current_password'))->assertScript('document.activeElement.id', 'password');
            }
        } elseif ($state === 'resent') {
            $page->click('Click here to resend the verification email.')
                ->assertSee('A new verification link has been sent to your email address.');
        } elseif ($state === 'unverified') {
            $page->assertSee('Your email address is unverified.');
        }
        if ($held) {
            $page->assertScript('Boolean(window.captureHeld)', true)
                ->assertScript('document.querySelector("[data-test='.mb_ltrim($button, '@').']").disabled', true);
        }
        if (in_array($state, ['default', 'system'], true)) {
            $page->keys($focus, 'Shift+Tab')->keys(':focus', 'Tab')
                ->assertScript('document.activeElement.matches('.json_encode($focus, JSON_THROW_ON_ERROR).')', true)
                ->assertScript('document.activeElement.matches(":focus-visible")', true);
        }
        if ($state === 'hover') {
            $page->hover($button);
        }
        $page->assertSee($expected)->assertPathIs(parse_url(route($route), PHP_URL_PATH))
            ->assertScript('document.documentElement.style.colorScheme', $theme)
            ->assertScript('document.documentElement.scrollWidth <= innerWidth', true)
            ->assertNoJavaScriptErrors();
        $name = "$surface-$state-$theme-{$width}x$height.png";
        $page->screenshot(filename: getenv('RALPH_SCREENSHOT_PREFIX').'/'.$name);
        $entry = [
            'path' => getenv('RALPH_EVIDENCE_DIR').'/'.$name,
            'screen' => match ($surface) {
                'profile' => 'perfil', 'password' => 'senha', 'appearance' => 'aparência', default => 'exclusão'
            },
            'state' => match ($state) {
                'default' => 'padrão com foco', 'error' => 'erro', 'success' => 'sucesso', 'processing' => 'processamento', 'unverified' => 'e-mail não verificado', 'resent' => 'reenvio confirmado', 'system' => 'sistema selecionado', default => 'hover em salvar'
            },
            'viewport' => "$width x $height",
            'theme' => $theme,
            'reference' => 'docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md — CSS .panel, h1, .btn, inputs, dialog e :focus-visible; adaptação de configurações em planning.md, Arquitetura',
        ];
        file_put_contents(getenv('RALPH_EVIDENCE_DIR').'/captures.jsonl', json_encode($entry, JSON_THROW_ON_ERROR | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES).PHP_EOL, FILE_APPEND);
        $this->assertAuthenticatedAs($user);
    } finally {
        if ($held) {
            $page->script('XMLHttpRequest.prototype.send = window.captureSend; if (window.captureHeld) { window.captureHeld.xhr.abort(); window.captureHeld.xhr.onabort?.(); }');
        }
    }
})->with(json_decode(file_get_contents(getenv('RALPH_CAPTURE_MATRIX')), true, flags: JSON_THROW_ON_ERROR));
