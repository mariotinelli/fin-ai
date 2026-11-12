import { Link } from '@inertiajs/react';
import { BookOpen, FolderGit2, LayoutGrid } from 'lucide-react';
import { useSyncExternalStore } from 'react';
import AppLogo from '@/components/app-logo';
import { NavFooter } from '@/components/nav-footer';
import { NavMain } from '@/components/nav-main';
import { NavUser } from '@/components/nav-user';
import { useSidebar } from '@/components/ui/sidebar';
import { dashboard } from '@/routes';
import type { NavItem } from '@/types';

const mainNavItems: NavItem[] = [
    {
        title: 'Dashboard',
        href: dashboard(),
        icon: LayoutGrid,
    },
];

const footerNavItems: NavItem[] = [
    {
        title: 'Repository',
        href: 'https://github.com/laravel/react-starter-kit',
        icon: FolderGit2,
    },
    {
        title: 'Documentation',
        href: 'https://laravel.com/docs/starter-kits#react',
        icon: BookOpen,
    },
];

const desktopQuery =
    typeof window === 'undefined'
        ? undefined
        : window.matchMedia('(min-width: 1024px)');

function subscribeDesktop(callback: () => void) {
    desktopQuery?.addEventListener('change', callback);
    return () => desktopQuery?.removeEventListener('change', callback);
}

function isDesktop() {
    return desktopQuery?.matches ?? false;
}

function serverDesktop() {
    return false;
}

export function AppSidebar() {
    const { state } = useSidebar();
    const desktop = useSyncExternalStore(
        subscribeDesktop,
        isDesktop,
        serverDesktop,
    );

    return (
        <aside
            className="finai-navigation group bg-sidebar text-sidebar-foreground"
            data-collapsible={
                desktop && state === 'collapsed' ? 'icon' : undefined
            }
        >
            <Link
                href={dashboard()}
                prefetch
                aria-label="FinAI - Dashboard"
                className="finai-brand flex items-center gap-2 rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring"
            >
                <AppLogo />
            </Link>
            <nav aria-label="Principal" className="finai-primary">
                <NavMain items={mainNavItems} />
            </nav>
            <div className="finai-navigation-footer">
                <nav aria-label="Links externos" className="finai-external">
                    <NavFooter items={footerNavItems} className="p-0" />
                </nav>
                <div className="finai-user min-w-0">
                    <NavUser />
                </div>
            </div>
        </aside>
    );
}
