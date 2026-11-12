import { Head } from '@inertiajs/react';
import AppearanceTabs from '@/components/appearance-tabs';
import AppLayout from '@/layouts/app-layout';
import SettingsLayout from '@/layouts/settings/layout';
import { edit as editAppearance } from '@/routes/appearance';
import type { BreadcrumbItem } from '@/types';

const breadcrumbs: BreadcrumbItem[] = [
    {
        title: 'Appearance settings',
        href: editAppearance(),
    },
];

export default function Update() {
    return (
        <>
            <Head title="Appearance settings" />

            <div className="space-y-6 rounded-2xl border bg-card p-4 text-card-foreground sm:p-6">
                <header className="space-y-1">
                    <h2 className="text-xl font-semibold">
                        Appearance settings
                    </h2>
                    <p className="text-sm text-muted-foreground">
                        Update your account's appearance settings
                    </p>
                </header>
                <AppearanceTabs />
            </div>
        </>
    );
}

Update.layout = [
    [AppLayout, { breadcrumbs }],
    [SettingsLayout, { finai: true }],
];
