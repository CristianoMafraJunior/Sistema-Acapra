from django.urls import path
from .views import (
    Home,
    LoginAdmin,
    CatalogoAdmin,
    Cadastrar,
    FormulariosAdmin,
    AdocoesAdmin,
    CadastroAnimaisAdmin,
    LoginUser,
    FormularioAdocao,
    AnimaisDisponiveis,
    EditarAnimal,
    ExcluirFoto,
    AnimaisDisponiveisUser,
    FormularioAdocaoUser,
    Logout,
)


urlpatterns = [
    path("", Home, name="Home"),
    path("login_admin/", LoginAdmin, name="LoginAdmin"),
    path("catalogo_admin/", CatalogoAdmin, name="CatalogoAdmin"),
    path("cadastrar/", Cadastrar, name="Cadastrar"),
    path("admin_formularios/", FormulariosAdmin, name="FormulariosAdmin"),
    path("admin_adocoes/", AdocoesAdmin, name="AdocoesAdmin"),
    path("admin_cadastro_animais", CadastroAnimaisAdmin, name="CadastroAnimaisAdmin"),
    path("login_user/", LoginUser, name="LoginUser"),
    path("formulario_adocao/", FormularioAdocao, name="FormularioAdocao"),
    path("animais_disponiveis/", AnimaisDisponiveis, name="AnimaisDisponiveis"),
    path("animal/<int:animal_id>/editar/", EditarAnimal, name="EditarAnimal"),
    path("foto/<int:foto_id>/excluir/", ExcluirFoto, name="ExcluirFoto"),
    path(
        "animais_disponiveis_user/",
        AnimaisDisponiveisUser,
        name="AnimaisDisponiveisUser",
    ),
    path(
        "formulario_adocao_user/<int:animal_id>/",
        FormularioAdocaoUser,
        name="FormularioAdocaoUser",
    ),
    path("logout/", Logout, name="Logout"),
]
