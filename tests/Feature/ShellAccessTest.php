<?php

declare(strict_types=1);

use App\Models\User;

it('exige login nos destinos do shell para visitantes', function (string $route): void {
    $this->get(route($route))->assertRedirectToRoute('login');
})->with(['dashboard', 'user-profile.edit', 'password.edit', 'appearance.edit', 'two-factor.show', 'user-passkey.index']);

it('preserva verificação de email nos destinos restritos', function (string $route): void {
    $user = User::factory()->unverified()->withoutTwoFactor()->create();
    $this->actingAs($user)->get(route($route))->assertRedirectToRoute('verification.notice');
})->with(['dashboard', 'password.edit', 'appearance.edit', 'two-factor.show']);

it('permite que o usuário não verificado acesse o próprio perfil', function (): void {
    $user = User::factory()->unverified()->withoutTwoFactor()->create();
    $this->actingAs($user)->get(route('user-profile.edit'))->assertOk();
});
