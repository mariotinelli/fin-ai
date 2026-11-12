import { Form, Head, Link, usePage } from '@inertiajs/react';
import UserProfileController from '@/actions/App/Http/Controllers/UserProfileController';
import DeleteUser from '@/components/delete-user';
import InputError from '@/components/input-error';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import AppLayout from '@/layouts/app-layout';
import SettingsLayout from '@/layouts/settings/layout';
import { edit } from '@/routes/user-profile';
import { send } from '@/routes/verification';
import type { BreadcrumbItem } from '@/types';

const breadcrumbs: BreadcrumbItem[] = [
    {
        title: 'Profile settings',
        href: edit(),
    },
];

export default function Edit({ status }: { status?: string }) {
    const { auth } = usePage().props;

    return (
        <>
            <Head title="Profile settings" />

            <div className="space-y-6 rounded-2xl border bg-card p-4 text-card-foreground sm:p-6">
                <header className="space-y-1">
                    <h2 className="text-xl font-semibold">
                        Profile information
                    </h2>
                    <p className="text-sm text-muted-foreground">
                        Update your name and email address
                    </p>
                </header>

                <Form
                    {...UserProfileController.update.form()}
                    options={{
                        preserveScroll: true,
                    }}
                    className="space-y-6"
                >
                    {({ processing, errors }) => (
                        <>
                            <div className="grid gap-2">
                                <Label htmlFor="name">Name</Label>

                                <Input
                                    id="name"
                                    className="block w-full"
                                    defaultValue={auth.user.name}
                                    name="name"
                                    required
                                    autoComplete="name"
                                    placeholder="Full name"
                                />

                                <InputError message={errors.name} />
                            </div>

                            <div className="grid gap-2">
                                <Label htmlFor="email">Email address</Label>

                                <Input
                                    id="email"
                                    type="email"
                                    className="block w-full"
                                    defaultValue={auth.user.email}
                                    name="email"
                                    required
                                    autoComplete="username"
                                    placeholder="Email address"
                                />

                                <InputError message={errors.email} />
                            </div>

                            {auth.user.email_verified_at === null && (
                                <div className="space-y-2 rounded-lg border bg-accent p-4">
                                    <p className="text-sm text-muted-foreground">
                                        Your email address is unverified.{' '}
                                        <Link
                                            href={send()}
                                            as="button"
                                            className="rounded-sm text-primary underline decoration-primary/40 underline-offset-4 transition-colors duration-200 ease-out hover:decoration-current focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-ring"
                                        >
                                            Click here to resend the
                                            verification email.
                                        </Link>
                                    </p>

                                    {status === 'verification-link-sent' && (
                                        <div className="mt-2 text-sm font-medium text-positive">
                                            A new verification link has been
                                            sent to your email address.
                                        </div>
                                    )}
                                </div>
                            )}

                            <div className="flex flex-wrap items-center gap-4 border-t pt-6">
                                <Button
                                    disabled={processing}
                                    data-test="update-profile-button"
                                >
                                    Save
                                </Button>
                            </div>
                        </>
                    )}
                </Form>
            </div>

            <DeleteUser />
        </>
    );
}

Edit.layout = [
    [AppLayout, { breadcrumbs }],
    [SettingsLayout, { finai: true }],
];
