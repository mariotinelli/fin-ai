<?php

declare(strict_types=1);

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Validation\Rules\Password;

final class AppServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        //
    }

    public function boot(): void
    {
        Password::defaults(fn (): Password => Password::min(12)
            ->max(255)
            ->letters()
            ->mixedCase()
            ->numbers()
            ->symbols()
            ->uncompromised());
    }
}
