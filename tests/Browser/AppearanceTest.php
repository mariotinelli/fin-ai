<?php

declare(strict_types=1);

use App\Models\User;
use Pest\Browser\Playwright\Client;
use Pest\Browser\Playwright\Page;

function emulateDeviceColorScheme(Page $page, string $colorScheme): void
{
    $guid = new ReflectionProperty($page, 'guid')->getValue($page);

    assert(is_string($guid));

    iterator_to_array(Client::instance()->execute($guid, 'emulateMedia', ['colorScheme' => $colorScheme]));
}

it('mantém a aparência escolhida ao recarregar, mudar o dispositivo e navegar', function (string $mode, string $label, bool $initialDark, bool $deviceDark): void {
    $user = User::factory()->withoutTwoFactor()->create();

    $this->actingAs($user);

    $page = visit(route('appearance.edit'))->inLightMode();
    $renderedDark = <<<'JS'
function() {
    const [r, g, b] = getComputedStyle(document.body).backgroundColor.match(/\d+/g).map(Number);
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) < 128;
}
JS;

    $page->click($label)
        ->assertScript('document.querySelector("button[aria-pressed=true]").textContent.trim()', $label)
        ->assertScript($renderedDark, $initialDark)
        ->assertNoJavaScriptErrors()
        ->refresh()
        ->assertScript('localStorage.getItem("appearance")', $mode)
        ->assertSee($label)
        ->assertScript($renderedDark, $initialDark)
        ->assertNoJavaScriptErrors();

    emulateDeviceColorScheme($page->page(), 'dark');

    $page->assertScript('window.matchMedia("(prefers-color-scheme: dark)").matches', true)
        ->assertScript($renderedDark, $deviceDark)
        ->assertNoJavaScriptErrors()
        ->refresh()
        ->assertScript('localStorage.getItem("appearance")', $mode)
        ->assertScript($renderedDark, $deviceDark)
        ->assertNoJavaScriptErrors();

    emulateDeviceColorScheme($page->page(), 'light');

    $page->assertScript('window.matchMedia("(prefers-color-scheme: dark)").matches', false)
        ->assertScript($renderedDark, $initialDark)
        ->assertNoJavaScriptErrors()
        ->click('Profile')
        ->assertSee('Profile information')
        ->assertScript($renderedDark, $initialDark)
        ->assertNoJavaScriptErrors()
        ->click('Appearance')
        ->assertSee('Appearance settings')
        ->assertScript('localStorage.getItem("appearance")', $mode)
        ->assertScript('document.querySelector("button[aria-pressed=true]").textContent.trim()', $label)
        ->assertScript($renderedDark, $initialDark)
        ->assertNoJavaScriptErrors();
})->with([
    'claro explícito' => ['light', 'Light', false, false],
    'escuro explícito' => ['dark', 'Dark', true, true],
    'acompanhar sistema' => ['system', 'System', false, true],
]);
