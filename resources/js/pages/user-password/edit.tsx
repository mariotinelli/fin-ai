import { Form, Head } from '@inertiajs/react';
import { useRef } from 'react';
import UserPasswordController from '@/actions/App/Http/Controllers/UserPasswordController';
import InputError from '@/components/input-error';
import PasswordInput from '@/components/password-input';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import AppLayout from '@/layouts/app-layout';
import SettingsLayout from '@/layouts/settings/layout';
import { edit } from '@/routes/password';
import type { BreadcrumbItem } from '@/types';

const breadcrumbs: BreadcrumbItem[] = [
    {
        title: 'Password settings',
        href: edit().url,
    },
];

type Props = {
    passwordRules: string;
};

export default function Password({ passwordRules }: Props) {
    const passwordInput = useRef<HTMLInputElement>(null);
    const currentPasswordInput = useRef<HTMLInputElement>(null);

    return (
        <>
            <Head title="Password settings" />

            <div className="space-y-6 rounded-2xl border bg-card p-4 text-card-foreground sm:p-6">
                <header className="space-y-1">
                    <h2 className="text-xl font-semibold">Update password</h2>
                    <p className="text-sm text-muted-foreground">
                        Ensure your account is using a long, random password to
                        stay secure
                    </p>
                </header>

                <Form
                    {...UserPasswordController.update.form()}
                    options={{
                        preserveScroll: true,
                    }}
                    resetOnError={[
                        'password',
                        'password_confirmation',
                        'current_password',
                    ]}
                    resetOnSuccess
                    onError={(errors) => {
                        if (errors.password) {
                            passwordInput.current?.focus();
                        }

                        if (errors.current_password) {
                            currentPasswordInput.current?.focus();
                        }
                    }}
                    className="space-y-6"
                >
                    {({ errors, processing }) => (
                        <>
                            <div className="grid gap-2">
                                <Label htmlFor="current_password">
                                    Current password
                                </Label>

                                <PasswordInput
                                    id="current_password"
                                    ref={currentPasswordInput}
                                    name="current_password"
                                    className="block w-full"
                                    autoComplete="current-password"
                                    placeholder="Current password"
                                />

                                <InputError message={errors.current_password} />
                            </div>

                            <div className="grid gap-2">
                                <Label htmlFor="password">New password</Label>

                                <PasswordInput
                                    id="password"
                                    ref={passwordInput}
                                    name="password"
                                    passwordrules={passwordRules}
                                    className="block w-full"
                                    autoComplete="new-password"
                                    placeholder="New password"
                                />

                                <InputError message={errors.password} />
                            </div>

                            <div className="grid gap-2">
                                <Label htmlFor="password_confirmation">
                                    Confirm password
                                </Label>

                                <PasswordInput
                                    id="password_confirmation"
                                    name="password_confirmation"
                                    passwordrules={passwordRules}
                                    className="block w-full"
                                    autoComplete="new-password"
                                    placeholder="Confirm password"
                                />

                                <InputError
                                    message={errors.password_confirmation}
                                />
                            </div>

                            <div className="flex flex-wrap items-center gap-4 border-t pt-6">
                                <Button
                                    disabled={processing}
                                    data-test="update-password-button"
                                >
                                    Save password
                                </Button>
                            </div>
                        </>
                    )}
                </Form>
            </div>
        </>
    );
}

Password.layout = [
    [AppLayout, { breadcrumbs }],
    [SettingsLayout, { finai: true }],
];
