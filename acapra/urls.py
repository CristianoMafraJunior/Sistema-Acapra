from django.urls import path
from .views import (
    Home,
    LoginAdmin,
    DashboardAdmin,
    Cadastrar,
    FormulariosAdmin,
    AdocoesAdmin,
    CadastroAnimaisAdmin,
    LoginUser,
    FormularioAdocao,
    AnimaisDisponiveis,
    EditarAnimal,
    ExcluirFoto,
)


urlpatterns = [
    path("", Home, name="Home"),
    path("login_admin/", LoginAdmin, name="LoginAdmin"),
    path("dashboard_admin/", DashboardAdmin, name="DashboardAdmin"),
    path("cadastrar/", Cadastrar, name="Cadastrar"),
    path("admin_formularios/", FormulariosAdmin, name="FormulariosAdmin"),
    path("admin_adocoes/", AdocoesAdmin, name="AdocoesAdmin"),
    path("admin_cadastro_animais", CadastroAnimaisAdmin, name="CadastroAnimaisAdmin"),
    path("login_user/", LoginUser, name="LoginUser"),
    path("formulario_adocao/", FormularioAdocao, name="FormularioAdocao"),
    path("animais_disponiveis/", AnimaisDisponiveis, name="AnimaisDisponiveis"),
    path("animal/<int:animal_id>/editar/", EditarAnimal, name="EditarAnimal"),
    path("foto/<int:foto_id>/excluir/", ExcluirFoto, name="ExcluirFoto"),
]
