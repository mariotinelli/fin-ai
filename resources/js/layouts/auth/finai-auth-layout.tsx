import { Link } from '@inertiajs/react';
import type { PropsWithChildren } from 'react';
import AppLogo from '@/components/app-logo';
import { home } from '@/routes';

export default function FinaiAuthLayout({
    children,
    title,
    description,
}: PropsWithChildren<{ title?: string; description?: string }>) {
    return (
        <div className="flex min-h-svh flex-col items-center justify-center gap-8 bg-background px-4 py-8 text-foreground sm:px-8 sm:py-12">
            <Link
                href={home()}
                aria-label="FinAI — início"
                className="flex items-center gap-2 rounded-md focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-ring [&_svg]:size-6 [&>div]:size-10"
            >
                <AppLogo />
            </Link>
            <main className="w-full max-w-lg rounded-xl border bg-card p-6 text-card-foreground sm:p-8">
                <header className="mb-8 flex flex-col gap-2">
                    <h1 className="font-serif text-[clamp(32px,3vw,40px)] leading-[1.2] font-normal tracking-[-1px]">
                        {title}
                    </h1>
                    <p className="text-sm leading-relaxed text-muted-foreground">
                        {description}
                    </p>
                </header>
                {children}
            </main>
        </div>
    );
}
