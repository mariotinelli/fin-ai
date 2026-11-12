import { AppContent } from '@/components/app-content';
import { AppShell } from '@/components/app-shell';
import { AppSidebar } from '@/components/app-sidebar';
import { AppSidebarHeader } from '@/components/app-sidebar-header';
import type { AppLayoutProps } from '@/types';

export default function AppSidebarLayout({
    children,
    breadcrumbs = [],
}: AppLayoutProps) {
    return (
        <AppShell variant="sidebar">
            <AppSidebar />
            <AppContent variant="sidebar" className="min-w-0">
                <AppSidebarHeader breadcrumbs={breadcrumbs} />
                <div className="mx-auto flex w-full max-w-[1440px] min-w-0 flex-1 flex-col p-8 min-[1440px]:p-12 [@media(767px<width<=1200px)]:p-6 [@media(width<=767px)]:px-4 [@media(width<=767px)]:py-6">
                    {children}
                </div>
            </AppContent>
        </AppShell>
    );
}
