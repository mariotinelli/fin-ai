import { Head } from '@inertiajs/react';
import AppearanceTabs from '@/components/appearance-tabs';
import SettingsSection from '@/components/settings-section';
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

            <SettingsSection
                title="Appearance settings"
                description="Update your account's appearance settings"
            >
                <AppearanceTabs />
            </SettingsSection>
        </>
    );
}

Update.layout = [
    [AppLayout, { breadcrumbs }],
    [SettingsLayout, { finai: true }],
];
