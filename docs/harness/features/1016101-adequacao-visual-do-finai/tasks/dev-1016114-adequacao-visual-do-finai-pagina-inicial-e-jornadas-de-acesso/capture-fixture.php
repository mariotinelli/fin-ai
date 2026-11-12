<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Auth\Notifications\ResetPassword;
use Illuminate\Auth\Notifications\VerifyEmail;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Notification;
use Illuminate\Support\Facades\Password;
use Illuminate\Support\Facades\Vite;
use Pest\Browser\Api\AwaitableWebpage;
use Tests\TestCase;

pest()->extend(TestCase::class)->use(RefreshDatabase::class)->in(__DIR__);

function verifyAccessKeyboard(AwaitableWebpage $page, string $focus): void
{
    $count = $page->script(<<<'JS'
() => {
    window.accessFocusTargets = Array.from(document.querySelectorAll('a[href], button, input:not([type=hidden])'))
        .filter(el => el.tabIndex >= 0 && !el.disabled && el.getClientRects().length && !el.closest('[inert]'));
    window.accessFocusSeen = new Set();
    return window.accessFocusTargets.length;
}
JS);
    expect($count)->toBeGreaterThan(0);
    for ($index = 0; $index < $count * 2 + 2; $index++) {
        $page->page()->keyDown('Tab');
        $page->page()->keyUp('Tab');
        $page->script(<<<'JS'
() => {
    if (window.accessFocusTargets.includes(document.activeElement)) {
        window.accessFocusSeen.add(document.activeElement);
    }
}
JS);
    }
    $page->assertScript('window.accessFocusTargets.every(el => window.accessFocusSeen.has(el))', true);
    $selector = json_encode($focus, JSON_THROW_ON_ERROR);
    $page->script("() => document.querySelector($selector).focus()");
    $page->assertScript("document.activeElement === document.querySelector($selector)", true)
        ->assertScript(<<<'JS'
() => {
    const el = document.activeElement;
    const style = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    return el.matches(':focus-visible') &&
        ((style.outlineStyle !== 'none' && parseFloat(style.outlineWidth) >= 2) || style.boxShadow !== 'none') &&
        rect.left >= 7 && rect.right <= innerWidth - 7;
}
JS, true);
}

function writeAccessCapture(AwaitableWebpage $page, string $screen, string $state, string $theme, int $width, int $height, string $mechanism): void
{
    $page->assertVisible('[aria-label="FinAI"]')->assertNoJavaScriptErrors()
        ->assertScript('document.documentElement.style.colorScheme', $theme)
        ->assertScript('document.documentElement.scrollWidth <= innerWidth', true)
        ->assertScript(<<<'JS'
() => {
    const controls = Array.from(document.querySelectorAll('main a[href], main button, main input:not([type=hidden])'))
        .filter(el => el.getClientRects().length && el.getAttribute('aria-hidden') !== 'true');
    return controls.every(el => {
        el.scrollIntoView({block: 'center'});
        const r = el.getBoundingClientRect();
        return r.left >= 0 && r.right <= innerWidth && r.top >= 0 && r.bottom <= innerHeight;
    });
}
JS, true);
    $page->script('window.scrollTo(0, 0)');
    if (str_starts_with($state, 'hover-')) {
        $target = $state === 'hover-recuperacao' ? 'Forgot password?' : '@login-button';
        $page->hover($target);
        $selector = $state === 'hover-recuperacao' ? 'a[href$="/forgot-password"]' : '[data-test="login-button"]';
        $encodedSelector = json_encode($selector, JSON_THROW_ON_ERROR);
        $page->assertScript('document.querySelector('.$encodedSelector.').matches(":hover")', true);
    }
    $name = $screen.'-'.$state.'-'.$theme.'-'.$width.'x'.$height.'.png';
    $page->screenshot(filename: getenv('RALPH_SCREENSHOT_PREFIX').'/'.$name);
    $entry = [
        'path' => getenv('RALPH_EVIDENCE_DIR').'/'.$name,
        'reference' => 'docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md # .brand, h1, .panel, input, .btn, .notice, .error, :focus-visible; adaptação de acesso em planning.md/Arquitetura',
        'screen' => $screen,
        'state' => $state,
        'viewport' => $width.'x'.$height,
        'theme' => $theme,
        'mechanism' => $mechanism,
    ];
    $json = json_encode($entry, JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
    file_put_contents(getenv('RALPH_EVIDENCE_DIR').'/captures.jsonl', $json.PHP_EOL, FILE_APPEND);
}

it('captura a matriz aprovada de acesso', function (string $screen, string $state, string $theme): void {
    config(['inertia.ssr.enabled' => false]);
    Vite::useHotFile(__DIR__.'/no-hot-file');
    Notification::fake([ResetPassword::class, VerifyEmail::class]);
    $user = null;
    $token = null;
    $parameters = [];
    $mechanism = 'página real; foco e teclado reais no estado padrão';
    $route = match ($screen) {
        'inicial' => 'home',
        'cadastro' => 'register',
        'login' => 'login',
        'recuperacao' => 'password.request',
        'redefinicao' => 'password.reset',
        'verificacao' => 'verification.notice',
    };
    $title = match ($screen) {
        'inicial' => "Let's get started",
        'cadastro' => 'Create an account',
        'login' => 'Log in to your account',
        'recuperacao' => 'Forgot password',
        'redefinicao' => 'Reset password',
        'verificacao' => 'Verify email',
    };
    $focus = match ($screen) {
        'cadastro' => '#name',
        'login', 'recuperacao' => '#email',
        'redefinicao' => '#password',
        'verificacao' => 'main button',
        default => '',
    };
    $submit = match ($screen) {
        'cadastro' => '@register-user-button',
        'login' => '@login-button',
        'recuperacao' => '@email-password-reset-link-button',
        'redefinicao' => '@reset-password-button',
        'verificacao' => 'Resend verification email',
        default => '',
    };
    if ($screen === 'verificacao') {
        $user = User::factory()->unverified()->withoutTwoFactor()->create(['name' => 'Pessoa de teste', 'email' => 'pessoa@example.com']);
        $this->actingAs($user);
    } elseif (($screen === 'inicial' && $state === 'autenticado') || ($screen === 'login' && $state === 'processamento') || $screen === 'redefinicao') {
        $user = User::factory()->withoutTwoFactor()->create(['name' => 'Pessoa de teste', 'email' => 'pessoa@example.com']);
        if ($screen === 'inicial') {
            $this->actingAs($user);
        } elseif ($screen === 'redefinicao') {
            $token = Password::createToken($user);
            $parameters = ['token' => $state === 'token-invalido' ? 'token-de-teste-invalido' : $token, 'email' => $user->email];
        }
    }
    if ($state === 'senha-redefinida') {
        $this->withSession(['status' => __('passwords.reset')]);
        $mechanism = 'sessão de teste com o status real do contrato HTTP de redefinição';
    }
    $url = route($route, $parameters);
    $pending = visit($url);
    $pending = $theme === 'dark' ? $pending->inDarkMode() : $pending->inLightMode();
    $page = $pending->resize(1366, 768);
    $processing = $state === 'processamento';
    $error = in_array($state, ['erro', 'credenciais-invalidas', 'token-invalido'], true);
    $expected = null;

    try {
        $page->assertSee($title)->assertNoJavaScriptErrors();
        if ($processing || $error || in_array($state, ['sucesso', 'reenviado'], true)) {
            $mechanism = $processing ? 'Form real; XHR retido antes do envio e liberado após as capturas; resultado real conferido' : 'solicitação real ao endpoint; mensagem retornada pelo servidor';
            switch ($screen) {
                case 'cadastro':
                    $page->fill('name', 'Pessoa de teste')->fill('email', 'cadastro@example.com')
                        ->fill('password', $error ? 'curta' : 'new-Password-123!')
                        ->fill('password_confirmation', $error ? 'diferente' : 'new-Password-123!');
                    $expected = __('validation.confirmed', ['attribute' => 'password']);
                    break;
                case 'login':
                    $page->fill('email', 'pessoa@example.com')->fill('password', $error ? 'incorreta' : 'password');
                    $expected = __('auth.failed');
                    break;
                case 'recuperacao':
                    $page->fill('email', $error ? '' : 'inexistente@example.com');
                    $expected = $error ? __('validation.required', ['attribute' => 'email']) : 'A reset link will be sent if the account exists.';
                    break;
                case 'redefinicao':
                    $page->fill('password', $state === 'erro' ? 'curta' : 'new-Password-123!')
                        ->fill('password_confirmation', $state === 'erro' ? 'diferente' : 'new-Password-123!');
                    $expected = $state === 'erro' ? __('validation.confirmed', ['attribute' => 'password']) : __('passwords.token');
                    break;
                case 'verificacao':
                    $expected = 'A new verification link has been sent';
                    break;
            }
            if ($processing) {
                $page->script(<<<'JS'
() => {
    const send = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function(body) {
        XMLHttpRequest.prototype.send = send;
        window.releaseAccessRequest = () => {
            delete window.releaseAccessRequest;
            send.call(this, body);
        };
    };
}
JS);
            }
            $page->click($submit);
            if ($processing) {
                $page->assertScript('typeof window.releaseAccessRequest', 'function')
                    ->assertDisabled($submit)->assertVisible('button .animate-spin');
            } else {
                $page->assertSee($expected);
            }
        }
        foreach ([[360, 800], [390, 844], [430, 932], [600, 960], [820, 1180], [1024, 768], [1366, 768], [1440, 900], [1920, 1080]] as [$width, $height]) {
            $page->resize($width, $height)->assertSee($title);
            if ($screen === 'redefinicao') {
                $page->assertScript('/^\/reset-password\/[^/]+$/.test(window.location.pathname)', true);
            } else {
                $path = json_encode(parse_url($url, PHP_URL_PATH) ?: '/', JSON_THROW_ON_ERROR);
                $page->assertScript('window.location.pathname === '.$path, true);
            }
            if ($screen === 'inicial') {
                $page->assertSee($state === 'autenticado' ? 'Dashboard' : 'Log in')
                    ->assertSee('Documentation')->assertSee('Laracasts')->assertSee('Deploy now');
            } else {
                $page->assertSee($submit === 'Resend verification email' ? $submit : match ($screen) {
                    'cadastro' => 'Create account',
                    'login' => 'Log in',
                    'recuperacao' => 'Email password reset link',
                    'redefinicao' => 'Reset password',
                });
                if ($screen === 'login') {
                    $page->assertSee('Remember me')->assertSee('Sign in with a passkey')->assertSee('Forgot password?');
                }
                if ($state === 'padrao') {
                    verifyAccessKeyboard($page, $focus);
                } elseif ($processing) {
                    $page->assertDisabled($submit)->assertVisible('button .animate-spin');
                } elseif ($state === 'senha-redefinida') {
                    $page->assertSee(__('passwords.reset'));
                } else {
                    $page->assertSee($expected);
                }
            }
            writeAccessCapture($page, $screen, $state, $theme, $width, $height, $mechanism);
            if ($screen === 'login' && $state === 'padrao' && $width === 1366) {
                $page->hover('Forgot password?');
                writeAccessCapture($page, $screen, 'hover-recuperacao', $theme, $width, $height, 'hover real no link de recuperação');
                $page->hover('@login-button');
                writeAccessCapture($page, $screen, 'hover-principal', $theme, $width, $height, 'hover real no botão principal');
                $page->hover('main h1:first-of-type');
            }
        }
        if ($processing) {
            $page->script('() => window.releaseAccessRequest()');
            switch ($screen) {
                case 'cadastro':
                    $page->assertPathIs('/verify-email')->assertSee('Verify email');
                    $this->assertDatabaseHas('users', ['email' => 'cadastro@example.com']);
                    $registered = User::query()->where('email', 'cadastro@example.com')->sole();
                    expect(Hash::check('new-Password-123!', $registered->password))->toBeTrue();
                    Notification::assertSentTo($registered, VerifyEmail::class);
                    break;
                case 'login':
                    $page->assertPathIs('/dashboard');
                    $this->assertAuthenticatedAs($user);
                    break;
                case 'recuperacao':
                    $page->assertSee('A reset link will be sent if the account exists.')->assertEnabled($submit);
                    Notification::assertNothingSent();
                    break;
                case 'redefinicao':
                    $page->assertPathIs('/login')->assertSee(__('passwords.reset'));
                    expect(Hash::check('new-Password-123!', $user->fresh()->password))->toBeTrue();
                    break;
                case 'verificacao':
                    $page->assertSee('A new verification link has been sent')->assertEnabled($submit);
                    Notification::assertSentTo($user, VerifyEmail::class);
                    break;
            }
            $page->assertNoJavaScriptErrors();
        } elseif ($screen === 'verificacao' && $state === 'reenviado') {
            Notification::assertSentTo($user, VerifyEmail::class);
        }
    } finally {
        try {
            $page->script('() => window.releaseAccessRequest?.()');
        } finally {
            $page->page()->context()->close();
        }
    }
})->with([
    ['inicial', 'visitante'], ['inicial', 'autenticado'],
    ['cadastro', 'padrao'], ['cadastro', 'erro'], ['cadastro', 'processamento'],
    ['login', 'padrao'], ['login', 'credenciais-invalidas'], ['login', 'processamento'], ['login', 'senha-redefinida'],
    ['recuperacao', 'padrao'], ['recuperacao', 'erro'], ['recuperacao', 'processamento'], ['recuperacao', 'sucesso'],
    ['redefinicao', 'padrao'], ['redefinicao', 'erro'], ['redefinicao', 'token-invalido'], ['redefinicao', 'processamento'],
    ['verificacao', 'padrao'], ['verificacao', 'processamento'], ['verificacao', 'reenviado'],
])->with(['light', 'dark']);
