import { usePage } from '@inertiajs/react';
import { ChevronsUpDown } from 'lucide-react';
import { useRef } from 'react';
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import {
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from '@/components/ui/sidebar';
import { UserInfo } from '@/components/user-info';
import { UserMenuContent } from '@/components/user-menu-content';

export function NavUser() {
    const { auth } = usePage().props;
    const triggerRef = useRef<HTMLButtonElement>(null);

    return (
        <SidebarMenu>
            <SidebarMenuItem>
                <DropdownMenu>
                    <DropdownMenuTrigger asChild ref={triggerRef}>
                        <SidebarMenuButton
                            size="lg"
                            className="group text-sidebar-accent-foreground data-[state=open]:bg-sidebar-accent"
                            data-test="sidebar-menu-button"
                            aria-label={`Menu de ${auth.user.name}`}
                        >
                            <UserInfo user={auth.user} />
                            <ChevronsUpDown className="ml-auto size-4" />
                        </SidebarMenuButton>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent
                        className="w-(--radix-dropdown-menu-trigger-width) max-w-[calc(100vw-32px)] min-w-56 rounded-lg [&_.grid]:min-w-0 [&_[data-slot=dropdown-menu-label]]:overflow-hidden"
                        align="end"
                        side="bottom"
                        onPointerDownOutside={(event) => {
                            const target = event.detail.originalEvent.target;

                            // O botão pode reabrir o menu durante a animação de saída.
                            if (
                                target instanceof Node &&
                                triggerRef.current?.contains(target)
                            ) {
                                event.preventDefault();
                            }
                        }}
                    >
                        <UserMenuContent user={auth.user} />
                    </DropdownMenuContent>
                </DropdownMenu>
            </SidebarMenuItem>
        </SidebarMenu>
    );
}
