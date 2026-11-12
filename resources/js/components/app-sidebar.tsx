import { Link } from '@inertiajs/react';
import { BookOpen, FolderGit2, LayoutGrid } from 'lucide-react';
import { useSyncExternalStore } from 'react';
import AppLogo from '@/components/app-logo';
import { NavFooter } from '@/components/nav-footer';
import { NavMain } from '@/components/nav-main';
import { NavUser } from '@/components/nav-user';
import { useSidebar } from '@/components/ui/sidebar';
import { cn } from '@/lib/utils';
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
            className={cn(
                'finai-navigation group group/navigation sticky top-0 flex h-svh w-60 flex-[0_0_240px] flex-col gap-12 border-r border-border bg-sidebar px-6 py-8 text-sidebar-foreground',
                '[@media(1023px<width<=1200px)]:w-52 [@media(1023px<width<=1200px)]:flex-[0_0_208px] [@media(1023px<width<=1200px)]:px-4',
                '[@media(width<=1023px)]:static [@media(width<=1023px)]:h-auto [@media(width<=1023px)]:w-full [@media(width<=1023px)]:flex-none [@media(width<=1023px)]:border-r-0 [@media(width<=1023px)]:border-b [@media(width<=1023px)]:py-4',
                '[@media(767px<width<=1023px)]:flex-row [@media(767px<width<=1023px)]:items-center [@media(767px<width<=1023px)]:gap-6',
                '[@media(width<=767px)]:gap-4 [@media(width<=767px)]:px-4',
                'data-[collapsible=icon]:w-20 data-[collapsible=icon]:flex-[0_0_80px] data-[collapsible=icon]:px-6',
            )}
            data-collapsible={
                desktop && state === 'collapsed' ? 'icon' : undefined
            }
        >
            <Link
                href={dashboard()}
                prefetch
                aria-label="FinAI - Dashboard"
                className={cn(
                    'flex items-center gap-2 rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring [&_svg]:size-6 [&>div]:size-10 [&>span]:ml-0',
                    '[@media(width<=767px)]:self-center [@media(width<=767px)]:[&>span]:text-[24px]',
                    'group-data-[collapsible=icon]/navigation:[&>div]:size-8 group-data-[collapsible=icon]/navigation:[&>span]:hidden',
                )}
            >
                <AppLogo />
            </Link>
            <nav
                aria-label="Principal"
                className="[@media(767px<width<=1023px)]:ml-auto"
            >
                <NavMain items={mainNavItems} />
            </nav>
            <div
                className={cn(
                    'mt-auto flex flex-col gap-6',
                    '[@media(width<=1023px)]:mt-0 [@media(width<=1023px)]:min-w-0 [@media(width<=1023px)]:flex-row [@media(width<=1023px)]:items-center [@media(width<=1023px)]:gap-3',
                    '[@media(width<=767px)]:justify-between',
                )}
            >
                <nav aria-label="Links externos">
                    <NavFooter items={footerNavItems} className="p-0" />
                </nav>
                <div
                    className={cn(
                        'min-w-0 border-t border-border pt-6 [&_.grid]:min-w-0',
                        '[@media(width<=1023px)]:border-t-0 [@media(width<=1023px)]:pt-0',
                        '[@media(767px<width<=1023px)]:w-40',
                        '[@media(width<=767px)]:w-[min(208px,calc(100%_-_96px))]',
                    )}
                >
                    <NavUser />
                </div>
            </div>
        </aside>
    );
}
