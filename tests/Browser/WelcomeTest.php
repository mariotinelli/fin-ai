<?php

declare(strict_types=1);

it('has welcome page', function (): void {
    $page = visit('/');

    $page->assertSee('Laravel')
        ->assertVisible('[aria-label="FinAI"]')
        ->assertSee("Let's get started")
        ->assertSee('Documentation')
        ->assertSee('Laracasts')
        ->assertSee('Deploy now')
        ->assertSee('Log in')
        ->assertSee('Register')
        ->assertNoJavaScriptErrors();
});
