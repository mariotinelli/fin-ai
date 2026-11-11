import AppLogoIcon from '@/components/app-logo-icon';

export default function AppLogo() {
    return (
        <>
            <div className="flex aspect-square size-8 shrink-0 items-center justify-center rounded-[12px] bg-sidebar-primary text-sidebar-primary-foreground">
                <AppLogoIcon className="size-5" />
            </div>
            <span
                className="ml-1 truncate text-left text-[28px] leading-tight font-bold tracking-[-1px] text-sidebar-foreground"
                role="img"
                aria-label="FinAI"
            >
                fin<span className="font-normal text-sidebar-primary">ai</span>
            </span>
        </>
    );
}
