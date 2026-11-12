import { Head, Link, usePage } from '@inertiajs/react';
import { ArrowUpRight } from 'lucide-react';
import AppLogo from '@/components/app-logo';
import { Button } from '@/components/ui/button';
import { dashboard, login, register } from '@/routes';

export default function Welcome({
    canRegister = true,
}: {
    canRegister?: boolean;
}) {
    const { auth } = usePage().props;

    return (
        <>
            <Head title="Welcome" />
            <div className="flex min-h-svh flex-col bg-background px-4 py-8 text-foreground sm:px-8 sm:py-12">
                <header className="mx-auto flex w-full max-w-5xl flex-wrap items-center justify-between gap-6">
                    <div className="flex items-center gap-2 [&_svg]:size-6 [&>div]:size-10">
                        <AppLogo />
                    </div>
                    <nav
                        aria-label="Account"
                        className="flex flex-wrap items-center gap-2"
                    >
                        {auth.user ? (
                            <Button asChild>
                                <Link href={dashboard()}>Dashboard</Link>
                            </Button>
                        ) : (
                            <>
                                <Button asChild variant="ghost">
                                    <Link href={login()}>Log in</Link>
                                </Button>
                                {canRegister && (
                                    <Button asChild variant="outline">
                                        <Link href={register()}>Register</Link>
                                    </Button>
                                )}
                            </>
                        )}
                    </nav>
                </header>
                <main className="mx-auto flex w-full max-w-5xl flex-1 items-center py-12 sm:py-16">
                    <section className="grid w-full gap-8 rounded-xl border bg-card p-6 sm:p-8 lg:grid-cols-[1.2fr_1fr] lg:gap-12 lg:p-12">
                        <div className="flex min-w-0 flex-col items-start gap-6">
                            <h1 className="font-serif text-[clamp(32px,3vw,40px)] leading-[1.2] font-normal tracking-[-1px]">
                                Let's get started
                            </h1>
                            <p className="leading-relaxed text-muted-foreground">
                                Laravel has an incredibly rich ecosystem.
                                <br />
                                We suggest starting with the following.
                            </p>
                            <Button asChild>
                                <a
                                    href="https://cloud.laravel.com"
                                    target="_blank"
                                    rel="noreferrer"
                                >
                                    Deploy now{' '}
                                    <ArrowUpRight aria-hidden="true" />
                                </a>
                            </Button>
                        </div>
                        <ul className="flex min-w-0 flex-col justify-center gap-6 border-t pt-8 text-sm leading-relaxed lg:border-t-0 lg:border-l lg:pt-0 lg:pl-12">
                            <li className="flex flex-col items-start gap-2">
                                <span className="text-muted-foreground">
                                    Read the
                                </span>
                                <a
                                    href="https://laravel.com/docs"
                                    target="_blank"
                                    rel="noreferrer"
                                    className="inline-flex min-h-11 items-center gap-2 rounded-md font-semibold text-primary underline decoration-primary/40 underline-offset-4 hover:decoration-current focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-ring"
                                >
                                    Documentation{' '}
                                    <ArrowUpRight
                                        className="size-4"
                                        aria-hidden="true"
                                    />
                                </a>
                            </li>
                            <li className="flex flex-col items-start gap-2">
                                <span className="text-muted-foreground">
                                    Watch video tutorials at
                                </span>
                                <a
                                    href="https://laracasts.com"
                                    target="_blank"
                                    rel="noreferrer"
                                    className="inline-flex min-h-11 items-center gap-2 rounded-md font-semibold text-primary underline decoration-primary/40 underline-offset-4 hover:decoration-current focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-ring"
                                >
                                    Laracasts{' '}
                                    <ArrowUpRight
                                        className="size-4"
                                        aria-hidden="true"
                                    />
                                </a>
                            </li>
                        </ul>
                    </section>
                </main>
            </div>
        </>
    );
}
