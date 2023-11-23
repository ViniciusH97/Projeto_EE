from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required 
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction

def pagina_inicial(request):
    return render(request, "pagina_inicial/pagina_inicial.html")

def empresa(request):
    empresas = {"empresas": Empresa.objects.all()}
    return render(request, "Empresa/empresas.html", empresas)

def cadastro(request):
    return render(request, "cadastro/cadastro.html")

def login_view(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if user.is_staff:
                    return redirect('admin_site')
                else:
                    return redirect('pagina_inicial')
            else:
                error_message = 'Usuário ou senha incorretos ou não cadastrado.'
                messages.error(request, error_message)  
        else:
            error_message = 'Por favor, corrija os erros no formulário.'
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def cadastrar_usuario(request):
    if request.method == "POST":
        tipo_pessoa = request.POST.get("tipoPessoa")

        if tipo_pessoa == "fisica":
            form = CandidatoForm(request.POST)
        elif tipo_pessoa == "juridica":
            form = EmpresaForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])

                    if tipo_pessoa == "fisica":
                        Candidato.objects.create(usuario=user, **form.cleaned_data)
                    elif tipo_pessoa == "juridica":
                        Empresa.objects.create(usuario=user, **form.cleaned_data)

                    login(request, user)
                    return redirect('pagina_inicial')
            except Exception as e:
                messages.error(request, f"Erro ao cadastrar usuário: {str(e)}")

    return render(request, 'pagina_inicial/pagina_inicial.html', {'form': form})

def pesquisa_vagas(request):
    if 'q' in request.GET:
        query = request.GET['q']
        vagas = Vaga.objects.filter(titulo__icontains=query)
    else:
        vagas = Vaga.objects.all()

    return render(request, 'vagas/vagas.html', {'vagas': vagas})


def pagconfig(request):
    return render(request, "pagconfig/pagconfig.html")

@staff_member_required  
def admin_site(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
    return render(request, "admin/admin_site.html")

