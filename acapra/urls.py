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
]
