import { Head } from '@inertiajs/react';
import { PlaceholderPattern } from '@/components/ui/placeholder-pattern';
import AppLayout from '@/layouts/app-layout';
import { dashboard } from '@/routes';
import type { BreadcrumbItem } from '@/types';

const breadcrumbs: BreadcrumbItem[] = [
    {
        title: 'Dashboard',
        href: dashboard(),
    },
];

export default function Dashboard() {
    return (
        <>
            <Head title="Dashboard" />
            <div className="flex h-full min-w-0 flex-1 flex-col gap-6 p-4 md:p-6 lg:p-8">
                <div className="grid auto-rows-min gap-4 md:grid-cols-3">
                    <div className="relative aspect-video overflow-hidden rounded-xl border border-border bg-card">
                        <PlaceholderPattern className="absolute inset-0 size-full stroke-primary/15" />
                    </div>
                    <div className="relative aspect-video overflow-hidden rounded-xl border border-border bg-card">
                        <PlaceholderPattern className="absolute inset-0 size-full stroke-primary/15" />
                    </div>
                    <div className="relative aspect-video overflow-hidden rounded-xl border border-border bg-card">
                        <PlaceholderPattern className="absolute inset-0 size-full stroke-primary/15" />
                    </div>
                </div>
                <div className="relative min-h-[100vh] flex-1 overflow-hidden rounded-xl border border-border bg-card md:min-h-min">
                    <PlaceholderPattern className="absolute inset-0 size-full stroke-primary/15" />
                </div>
            </div>
        </>
    );
}

Dashboard.layout = [AppLayout, { breadcrumbs }];
