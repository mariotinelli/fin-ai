import type { PropsWithChildren } from 'react';
import InputError from '@/components/input-error';
import { Label } from '@/components/ui/label';

export default function FormField({
    id,
    label,
    error,
    hideLabel = false,
    children,
}: PropsWithChildren<{
    id: string;
    label: string;
    error?: string;
    hideLabel?: boolean;
}>) {
    return (
        <div className="grid gap-2">
            <Label htmlFor={id} className={hideLabel ? 'sr-only' : undefined}>
                {label}
            </Label>
            {children}
            <InputError message={error} />
        </div>
    );
}
