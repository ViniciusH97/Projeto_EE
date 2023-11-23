
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app import views
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    path('empresas/', empresa ,name='empresas'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('pagconfig/', views.pagconfig, name='pagconfig'),
    path('vagas/', views.pesquisa_vagas, name='vagas'),
    path('admin_site/', views.admin_site, name='admin_site'),
]


