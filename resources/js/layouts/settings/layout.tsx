import { Link } from '@inertiajs/react';
import type { PropsWithChildren } from 'react';
import Heading from '@/components/heading';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';
import { useCurrentUrl } from '@/hooks/use-current-url';
import { cn, toUrl } from '@/lib/utils';
import { edit as editAppearance } from '@/routes/appearance';
import { edit as editPassword } from '@/routes/password';
import { show as showTwoFactor } from '@/routes/two-factor';
import { index as indexPasskeys } from '@/routes/user-passkey';
import { edit } from '@/routes/user-profile';
import type { NavItem } from '@/types';

const sidebarNavItems: NavItem[] = [
    {
        title: 'Profile',
        href: edit(),
        icon: null,
    },
    {
        title: 'Password',
        href: editPassword(),
        icon: null,
    },
    {
        title: 'Two-Factor Auth',
        href: showTwoFactor(),
        icon: null,
    },
    {
        title: 'Passkeys',
        href: indexPasskeys(),
        icon: null,
    },
    {
        title: 'Appearance',
        href: editAppearance(),
        icon: null,
    },
];

export default function SettingsLayout({
    children,
    finai = false,
}: PropsWithChildren<{ finai?: boolean }>) {
    const { isCurrentOrParentUrl } = useCurrentUrl();

    // When server-side rendering, we only render the layout on the client...
    if (typeof window === 'undefined') {
        return null;
    }

    return (
        <div
            className={
                finai
                    ? 'mx-auto w-full max-w-[1440px] px-4 py-8 sm:px-8'
                    : 'px-4 py-6'
            }
        >
            {finai ? (
                <header className="mb-8 space-y-2">
                    <h1 className="font-serif text-[clamp(32px,3vw,40px)] leading-[1.2] font-normal tracking-[-1px]">
                        Settings
                    </h1>
                    <p className="text-muted-foreground">
                        Manage your profile and account settings
                    </p>
                </header>
            ) : (
                <Heading
                    title="Settings"
                    description="Manage your profile and account settings"
                />
            )}

            <div
                className={
                    finai
                        ? 'flex min-w-0 flex-col gap-8 lg:flex-row'
                        : 'flex flex-col lg:flex-row lg:space-x-12'
                }
            >
                <aside
                    className={
                        finai
                            ? 'w-full shrink-0 lg:w-48'
                            : 'w-full max-w-xl lg:w-48'
                    }
                >
                    <nav
                        className="flex flex-col space-y-1 space-x-0"
                        aria-label="Settings"
                    >
                        {sidebarNavItems.map((item, index) => (
                            <Button
                                key={`${toUrl(item.href)}-${index}`}
                                size="sm"
                                variant="ghost"
                                asChild
                                className={cn(
                                    'w-full justify-start',
                                    finai && 'min-h-12 px-4 text-base',
                                    {
                                        'bg-muted':
                                            !finai &&
                                            isCurrentOrParentUrl(item.href),
                                        'bg-accent text-primary':
                                            finai &&
                                            isCurrentOrParentUrl(item.href),
                                    },
                                )}
                            >
                                <Link
                                    href={item.href}
                                    aria-current={
                                        finai && isCurrentOrParentUrl(item.href)
                                            ? 'page'
                                            : undefined
                                    }
                                >
                                    {item.icon && (
                                        <item.icon className="h-4 w-4" />
                                    )}
                                    {item.title}
                                </Link>
                            </Button>
                        ))}
                    </nav>
                </aside>

                {!finai && <Separator className="my-6 lg:hidden" />}

                <div
                    className={finai ? 'min-w-0 flex-1' : 'flex-1 md:max-w-2xl'}
                >
                    <section
                        className={
                            finai
                                ? 'max-w-3xl space-y-6'
                                : 'max-w-xl space-y-12'
                        }
                    >
                        {children}
                    </section>
                </div>
            </div>
        </div>
    );
}
