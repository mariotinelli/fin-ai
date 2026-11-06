<?php

declare(strict_types=1);

namespace App\Actions;

use Illuminate\Auth\Events\PasswordResetLinkSent;
use Illuminate\Contracts\Auth\CanResetPassword;
use Illuminate\Support\Facades\Password;
use Throwable;

final readonly class CreateUserEmailResetNotification
{
    /**
     * @param  array<string, mixed>  $credentials
     */
    public function handle(array $credentials): string
    {
        $broker = Password::broker();

        return $broker->sendResetLink($credentials, function (CanResetPassword $user, string $token) use ($broker): string {
            try {
                $user->sendPasswordResetNotification($token);
            } catch (Throwable $throwable) {
                $broker->deleteToken($user);

                throw $throwable;
            }

            event(new PasswordResetLinkSent($user));

            return Password::RESET_LINK_SENT;
        });
    }
}
