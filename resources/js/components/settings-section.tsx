import type { PropsWithChildren } from 'react';
import { Card } from '@/components/ui/card';

export default function SettingsSection({
    title,
    description,
    children,
}: PropsWithChildren<{ title: string; description: string }>) {
    return (
        <Card className="block space-y-6 rounded-2xl p-4 shadow-none sm:p-6">
            <header className="space-y-1">
                <h2 className="text-xl font-semibold">{title}</h2>
                <p className="text-sm text-muted-foreground">{description}</p>
            </header>
            {children}
        </Card>
    );
}
