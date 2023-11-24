from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from app.forms import LoginForm
from .models import *
from django.contrib import messages


def pagina_inicial(request):
    ultimas_vagas = Vaga.objects.order_by('-id')[:5]

    return render(request, "pagina_inicial/pagina_inicial.html", {'ultimas_vagas': ultimas_vagas})

def pagina_inicial(request):
    return render(request, "pagina_inicial/pagina_inicial.html")

def empresa(request):
    empresas = {"empresas": Empresa.objects.all()}
    return render(request, "Empresa/empresas.html", empresas)


def cadastro(request):
    return render(request, "cadastro/cadastro.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if user.is_staff:
                    return redirect("admin_site")
                else:
                    messages.success(request, "Login bem-sucedido!")
                    return redirect("pagina_inicial")
            else:
                error_message = "Usuário ou senha incorretos."
                return render(request, "login.html", {"error_message": error_message, "form": form})
    
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def cadastrar_usuario(request):
    if request.method == "POST":
        try:
            tipo_pessoa = request.POST.get("tipoPessoa")
            nome = request.POST.get("nome")
            telefone = request.POST.get("telefonecandidato")
            endereco = request.POST.get("endereco")
            telefonejuridica = request.POST.get("telefoneJuridica")

            if tipo_pessoa == "fisica":
                email = request.POST.get("email")
                candidato = Candidato(
                    nome=nome, telefone=telefone, endereco=endereco, email=email
                )
                candidato.save()

            elif tipo_pessoa == "juridica":
                cnpj = request.POST.get("cnpj")
                razao_social = request.POST.get("razaoSocial")
                segmento = request.POST.get("segmento")
                enderecojuridica = request.POST.get("enderecoJuridica")
                empr = Empresa(
                    nome=razao_social,
                    telefone=telefonejuridica,
                    endereco=enderecojuridica,
                    segmento=segmento,
                    cnpj=cnpj,
                )
                empr.save()
        except IntegrityError as e:
            print(f"IntegrityError: {e}")

    return render(request, "pagina_inicial/pagina_inicial.html")


def pesquisa_vagas(request):
    if 'q' in request.GET:
        query = request.GET['q']
        vagas = Vaga.objects.filter(titulo__icontains=query)
    else:
        vagas = Vaga.objects.all()

    return render(request, 'vagas/vagas.html', {'vagas': vagas})


def pagconfig(request):
    return render(request, "pagconfig/pagconfig.html")

def admin_site(request):
    return render(request, "admin_site/admin_site.html")

def perfil(request):
    return render(request, "perfil/perfil.html")
