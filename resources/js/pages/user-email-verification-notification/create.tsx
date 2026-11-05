import { Form, Head } from '@inertiajs/react';
// Components
import AlertError from '@/components/alert-error';
import TextLink from '@/components/text-link';
import { Button } from '@/components/ui/button';
import { Spinner } from '@/components/ui/spinner';
import AuthLayout from '@/layouts/auth-layout';
import { logout } from '@/routes';
import { send } from '@/routes/verification';

export default function VerifyEmail({ status }: { status?: string }) {
    return (
        <>
            <Head title="Confirmação de e-mail" />

            {status === 'verification-link-sent' && (
                <div className="mb-4 text-center text-sm font-medium text-green-600">
                    Um novo link de confirmação foi enviado para o endereço de
                    e-mail informado durante o cadastro.
                </div>
            )}

            <Form {...send.form()} className="space-y-6 text-center">
                {({ processing, errors }) => (
                    <>
                        {Object.keys(errors).length > 0 && (
                            <AlertError
                                errors={Object.values(errors)}
                                title="Não foi possível concluir a solicitação."
                            />
                        )}

                        <Button disabled={processing} variant="secondary">
                            {processing && <Spinner />}
                            Reenviar e-mail de confirmação
                        </Button>

                        <TextLink
                            href={logout()}
                            className="mx-auto block text-sm"
                        >
                            Sair
                        </TextLink>
                    </>
                )}
            </Form>
        </>
    );
}

VerifyEmail.layout = [
    AuthLayout,
    {
        title: 'Confirme seu e-mail',
        description:
            'Confirme seu endereço de e-mail clicando no link que acabamos de enviar.',
    },
];
