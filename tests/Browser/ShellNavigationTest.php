<?php

declare(strict_types=1);

use App\Models\User;

it('preserva a área do painel inferior no tablet com os menus abertos', function (string $theme): void {
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user);

    $page = visit(route('dashboard'))->resize(820, 1180);
    $page->script("localStorage.setItem('appearance', '$theme')");
    $page->refresh()->assertScript('document.documentElement.style.colorScheme', $theme);

    $panelOccupiesAvailableSpace = <<<'JS'
        (() => {
            const panel = document.querySelector('[data-test="dashboard-panel"]').getBoundingClientRect();
            return panel.height > innerHeight / 2;
        })()
        JS;

    $page->assertVisible('@dashboard-panel')
        ->assertScript($panelOccupiesAvailableSpace)
        ->click('@sidebar-menu-button')
        ->assertVisible('[role="menu"]')
        ->assertScript($panelOccupiesAvailableSpace)
        ->keys('[role="menu"]', 'Escape')
        ->keys('@sidebar-menu-button', 'Enter')
        ->keys('[role="menu"]', 'ArrowDown')
        ->assertVisible('[role="menu"]')
        ->assertScript('document.activeElement.getAttribute("role")', 'menuitem')
        ->assertScript($panelOccupiesAvailableSpace)
        ->keys('[role="menu"]', 'Escape')
        ->assertNoJavaScriptErrors();
})->with(['claro' => 'light', 'escuro' => 'dark']);

it('mantém navegação, menu por teclado e saída no shell responsivo', function (int $width, int $height): void {
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user)->withSession(['auth.password_confirmed_at' => time()]);

    $page = visit(route('dashboard'))->resize($width, $height);
    $page->assertVisible('nav[aria-label="Principal"] a[aria-current="page"]')
        ->assertVisible('a[aria-label="Repository"]')
        ->assertVisible('a[aria-label="Documentation"]')
        ->click('@sidebar-menu-button')
        ->assertVisible('[role="menu"]')
        ->assertSee('Settings')
        ->assertSee('Log out')
        ->keys('[role="menu"]', 'Escape')
        ->assertScript('document.activeElement.dataset.test', 'sidebar-menu-button')
        ->keys('@sidebar-menu-button', 'Enter')
        ->keys('[role="menu"]', 'ArrowDown')
        ->assertScript('document.activeElement.getAttribute("role")', 'menuitem')
        ->keys('[role="menu"]', 'Escape')
        ->assertScript('document.activeElement.dataset.test', 'sidebar-menu-button')
        ->click('@sidebar-menu-button')
        ->keys('[role="menuitem"][href="/settings/profile"]', 'Enter')
        ->assertPathIs('/settings/profile')
        ->assertSee('Profile information')
        ->assertAttributeMissing('nav[aria-label="Principal"] a', 'aria-current');

    foreach ([
        'Password' => '/settings/password',
        'Two-Factor Auth' => '/settings/two-factor',
        'Passkeys' => '/settings/passkeys',
        'Appearance' => '/settings/appearance',
        'Profile' => '/settings/profile',
    ] as $label => $path) {
        $page->keys('nav[aria-label="Settings"] a[href="'.$path.'"]', 'Enter')
            ->assertPathIs($path)
            ->assertSee($label)
            ->assertNoJavaScriptErrors();
    }

    $page->click('nav[aria-label="Principal"] a')
        ->assertPathIs('/dashboard')
        ->assertVisible('nav[aria-label="Principal"] a[aria-current="page"]')
        ->click('@sidebar-menu-button')
        ->click('@logout-button')
        ->assertPathIs('/')
        ->navigate(route('dashboard'))
        ->assertPathIs('/login')
        ->assertNoJavaScriptErrors();
})->with([
    'celular' => [390, 844],
    'tablet' => [820, 1180],
    'desktop' => [1366, 768],
]);

it('recupera operações ao recolher e redimensionar a navegação', function (): void {
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user);

    $page = visit(route('dashboard'))->resize(1366, 768);
    $page->click('[data-sidebar="trigger"]')
        ->assertVisible('nav[aria-label="Principal"] a')
        ->assertVisible('a[aria-label="Repository"]')
        ->assertVisible('a[aria-label="Documentation"]')
        ->click('@sidebar-menu-button')
        ->assertSee('Settings')
        ->keys('[role="menu"]', 'Escape')
        ->resize(820, 1180)
        ->refresh()
        ->assertVisible('nav[aria-label="Principal"] a')
        ->click('@sidebar-menu-button')
        ->assertSee('Log out')
        ->keys('[role="menu"]', 'Escape')
        ->resize(390, 844)
        ->click('@sidebar-menu-button')
        ->assertSee('Settings')
        ->keys('[role="menu"]', 'Escape')
        ->resize(1366, 768)
        ->click('[data-sidebar="trigger"]')
        ->click('@sidebar-menu-button')
        ->assertSee('Settings')
        ->keys('[role="menu"]', 'Escape')
        ->assertScript('document.documentElement.scrollWidth <= innerWidth', true)
        ->assertNoJavaScriptErrors();
});
