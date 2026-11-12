import { Form, Head } from '@inertiajs/react';
import { useRef } from 'react';
import UserPasswordController from '@/actions/App/Http/Controllers/UserPasswordController';
import FormField from '@/components/form-field';
import PasswordInput from '@/components/password-input';
import SettingsSection from '@/components/settings-section';
import { Button } from '@/components/ui/button';
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

            <SettingsSection
                title="Update password"
                description="Ensure your account is using a long, random password to stay secure"
            >
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
                            <FormField
                                id="current_password"
                                label="Current password"
                                error={errors.current_password}
                            >
                                <PasswordInput
                                    id="current_password"
                                    ref={currentPasswordInput}
                                    name="current_password"
                                    className="block w-full"
                                    autoComplete="current-password"
                                    placeholder="Current password"
                                />
                            </FormField>

                            <FormField
                                id="password"
                                label="New password"
                                error={errors.password}
                            >
                                <PasswordInput
                                    id="password"
                                    ref={passwordInput}
                                    name="password"
                                    passwordrules={passwordRules}
                                    className="block w-full"
                                    autoComplete="new-password"
                                    placeholder="New password"
                                />
                            </FormField>

                            <FormField
                                id="password_confirmation"
                                label="Confirm password"
                                error={errors.password_confirmation}
                            >
                                <PasswordInput
                                    id="password_confirmation"
                                    name="password_confirmation"
                                    passwordrules={passwordRules}
                                    className="block w-full"
                                    autoComplete="new-password"
                                    placeholder="Confirm password"
                                />
                            </FormField>

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
            </SettingsSection>
        </>
    );
}

Password.layout = [
    [AppLayout, { breadcrumbs }],
    [SettingsLayout, { finai: true }],
];
