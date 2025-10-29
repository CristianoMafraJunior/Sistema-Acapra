from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.utils.html import format_html
from acapra.models import FormularioAdocao


def AprovarFormulario(request, formulario_id):
    formulario = get_object_or_404(FormularioAdocao, id=formulario_id)

    animal = formulario.animal
    animal.status_adocao = "A"  # Adotado
    animal.save()
    formulario.processado = True
    formulario.save()
    adotante = formulario.user

    if adotante and adotante.email:
        send_mail(
            subject="🎉 Adoção Aprovada!",
            message=(
                f"Olá {adotante.nome},\n\n"
                f"Temos uma ótima notícia!\n\n"
                f"Sua adoção do animal '{animal.nome}' foi aprovada. "
                "A equipe da ONG entrará em contato para combinar os próximos passos "
                "e formalizar a entrega.\n\n"
                "Obrigado por escolher adotar e mudar uma vida 🐾\n"
                "Equipe Acapra"
            ),
            from_email=None,
            recipient_list=[adotante.email],
            fail_silently=False,
            html_message=format_html(
                """
                <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                    <h2 style="color: #6B21A8; font-size: 20px; margin: 0 0 10px;">🎉 Adoção Aprovada!</h2>
                    <p style="font-size: 15px; color: #333; line-height: 1.5;">
                        Olá <strong>{nome}</strong>,<br><br>
                        Temos uma ótima notícia! Sua adoção do animal
                        <strong>{animal}</strong> foi <strong>aprovada</strong> 🐶💜
                    </p>

                    <p style="font-size: 15px; color: #333; line-height: 1.5;">
                        A equipe da Acapra vai entrar em contato para combinar retirada / entrega
                        e finalizar os próximos passos (documento de responsabilidade, orientações de adaptação, etc.).
                    </p>

                    <div style="background:#f5f5f5; border-radius:8px; padding:12px 16px; margin:20px 0;">
                        <p style="margin:0; font-size:14px; color:#555;">
                            <strong>Animal:</strong> {animal}<br>
                            <strong>Espécie:</strong> {especie}<br>
                            <strong>Idade:</strong> {idade} anos<br>
                        </p>
                    </div>

                    <p style="font-size: 14px; color: #555; line-height: 1.5;">
                        Obrigado por escolher <strong>adotar</strong> e não comprar. ❤️<br>
                        Você mudou uma vida hoje.
                    </p>

                    <hr style="margin: 24px 0; border: none; border-top: 1px solid #ddd;"/>

                    <p style="font-size: 12px; color: #888; line-height: 1.4; margin:0;">
                        Este e-mail foi enviado automaticamente pelo sistema Acapra.
                    </p>
                </div>
                """,
                nome=adotante.nome,
                animal=animal.nome,
                especie=animal.especie,
                idade=animal.idade,
            ),
        )
    return redirect("FormulariosAdmin")
