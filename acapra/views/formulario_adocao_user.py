from django.shortcuts import render, redirect, get_object_or_404
from acapra.models import Animal, User
from acapra.forms import FormularioAdocaoForm
from django.core.mail import send_mail
from django.utils.html import format_html


def FormularioAdocaoUser(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    user = None
    user_id = request.session.get("user_id")
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None

    if request.method == "POST":
        form = FormularioAdocaoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivos = request.FILES.getlist("documentos")
            form.save(animal=animal, user=user, arquivos=arquivos)
            send_mail(
                subject="🐾 Formulário de Adoção Recebido!",
                message=(
                    f"Usuário {user.nome if user else 'Anônimo'} "
                    f"solicitou a adoção do animal: {animal.nome}.\n"
                    f"Email do usuário: {user.email if user else 'Não informado'}."
                ),  # Texto simples (fallback)
                from_email=None,
                recipient_list=["cristiano.mafracontanto@gmail.com"],
                fail_silently=False,
                html_message=format_html(
                    """
                    <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                        <h2 style="color: #4CAF50;">🐶 Nova Solicitação de Adoção</h2>
                        <p><strong>Nome do Usuário:</strong> {}</p>
                        <p><strong>Email:</strong> {}</p>
                        <p><strong>Animal Solicitado:</strong> {}</p>
                        <hr style="margin: 20px 0;">
                        <p style="font-size: 0.9em; color: #888;">Este email foi enviado automaticamente pelo sistema Acapra.</p>
                    </div>
                """,
                    user.nome if user else "Anônimo",
                    user.email if user else "Não informado",
                    animal.nome,
                ),
            )
            return redirect("AnimaisDisponiveisUser")
    else:
        form = FormularioAdocaoForm()

    return render(
        request, "acapra/formulario_adocao.html", {"form": form, "animal": animal}
    )
