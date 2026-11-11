import { Link } from '@inertiajs/react';
import type { ComponentProps } from 'react';
import { cn } from '@/lib/utils';

type Props = ComponentProps<typeof Link>;

export default function TextLink({
    className = '',
    children,
    ...props
}: Props) {
    return (
        <Link
            className={cn(
                'rounded-sm text-primary underline decoration-primary/40 underline-offset-4 transition-colors duration-200 ease-out hover:decoration-current focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-ring',
                className,
            )}
            {...props}
        >
            {children}
        </Link>
    );
}
