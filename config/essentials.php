<?php

declare(strict_types=1);

use NunoMaduro\Essentials\Configurables\SetDefaultPassword;
use NunoMaduro\Essentials\Configurables\Unguard;

return [
    SetDefaultPassword::class => false,
    Unguard::class => true,
];
