<?php

declare(strict_types=1);

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Vite;
use Tests\TestCase;

pest()->extend(TestCase::class)->use(RefreshDatabase::class)->in(__DIR__);

it('captures an authenticated preflight', function (): void {
    config(['inertia.ssr.enabled' => false]);
    Vite::useHotFile(__DIR__.'/no-hot-file');
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user);
    $page = visit(route('dashboard'))->resize(1366, 768);

    foreach (['light', 'dark'] as $theme) {
        $page->script("localStorage.setItem('appearance', '$theme')");
        $page->refresh()->assertSee('Dashboard')->assertNoJavaScriptErrors()
            ->assertScript('window.location.pathname.endsWith("/dashboard")', true)
            ->assertScript('document.documentElement.style.colorScheme', $theme);
        $page->screenshot(filename: getenv('RALPH_SCREENSHOT_PREFIX').'/preflight-'.$theme);
    }
    $this->assertAuthenticatedAs($user);
});

it('captures the approved missing state', function (string $state): void {
    config(['inertia.ssr.enabled' => false]);
    Vite::useHotFile(__DIR__.'/no-hot-file');
    $positive = false;
    $toggle = false;

    switch ($state) {
        case 'login-positive':
            $this->withSession(['status' => __('passwords.reset')]);
            $route = 'login';
            $expected = __('passwords.reset');
            $positive = true;
            break;
        case 'recovery-positive':
            $this->withSession(['status' => __('passwords.sent')]);
            $route = 'password.request';
            $expected = __('passwords.sent');
            $positive = true;
            break;
        case 'verification-positive':
            $this->actingAs(User::factory()->unverified()->withoutTwoFactor()->create())
                ->withSession(['status' => 'verification-link-sent']);
            $route = 'verification.notice';
            $expected = 'A new verification link has been sent';
            $positive = true;
            break;
        case 'profile-unverified':
        case 'profile-verification-positive':
            $this->actingAs(User::factory()->unverified()->withoutTwoFactor()->create())
                ->withSession(['status' => $state === 'profile-verification-positive' ? 'verification-link-sent' : null]);
            $route = 'user-profile.edit';
            $expected = 'Your email address is unverified.';
            $positive = $state === 'profile-verification-positive';
            break;
        case 'two-factor-authentication-link':
        case 'two-factor-recovery-link':
            $user = User::factory()->create();
            $this->withSession(['login.id' => $user->getKey(), 'login.remember' => false]);
            $route = 'two-factor.login';
            $expected = 'login using a recovery code';
            $toggle = $state === 'two-factor-recovery-link';
            break;
        default:
            throw new InvalidArgumentException('Unsupported evidence state: '.$state);
    }

    $page = visit(route($route));
    $matrix = [[360, 800], [390, 844], [430, 932], [600, 960], [820, 1180], [1024, 768], [1366, 768], [1440, 900], [1920, 1080]];
    foreach (['light', 'dark'] as $theme) {
        $page->script("localStorage.setItem('appearance', '$theme')");
        $page->refresh();
        if ($toggle) {
            $page->click('login using a recovery code');
        }
        foreach ($matrix as [$width, $height]) {
            $page->resize($width, $height)->assertSee($toggle ? 'login using an authentication code' : $expected)
                ->assertNoJavaScriptErrors()
                ->assertScript('document.documentElement.style.colorScheme', $theme)
                ->assertScript('document.documentElement.scrollWidth <= innerWidth');
            if ($positive) {
                $page->assertVisible('.text-positive');
            }
            if (str_starts_with($state, 'profile-')) {
                $page->assertSee('Click here to resend the verification email.');
                if ($positive) {
                    $page->assertSee('A new verification link has been sent to your email address.');
                }
            }
            if (str_starts_with($state, 'two-factor-')) {
                $page->script("Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('login using')).focus()");
            }
            $name = $state.'-'.$theme.'-'.$width.'x'.$height.'.png';
            $page->screenshot(filename: getenv('RALPH_SCREENSHOT_PREFIX').'/'.$name);
            $entry = [
                'path' => getenv('RALPH_EVIDENCE_DIR').'/'.$name,
                'screen' => $route,
                'state' => $state,
                'viewport' => $width.'x'.$height,
                'theme' => $theme,
                'reference' => 'docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md',
            ];
            $json = json_encode($entry, JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES);
            file_put_contents(getenv('RALPH_EVIDENCE_DIR').'/captures.jsonl', $json.PHP_EOL, FILE_APPEND);
            echo $json.PHP_EOL;
        }
    }
})->with([
    'login-positive',
    'recovery-positive',
    'verification-positive',
    'profile-unverified',
    'profile-verification-positive',
    'two-factor-authentication-link',
    'two-factor-recovery-link',
]);
