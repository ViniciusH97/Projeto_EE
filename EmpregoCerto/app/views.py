from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from .models import *


def pagina_inicial(request):
    return render(request, "pagina_inicial/pagina_inicial.html")

def empresa(request):
    empresas = {"empresas": Empresa.objects.all()}
    return render(request, "Empresa/empresas.html", empresas)


def cadastro(request):
    return render(request, "cadastro/cadastro.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("pagina_inicial")
        else:
            error_message = "Usuário ou senha incorretos ou não cadastrado."
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")


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

    return render(request, "pagina_inicial")


def pesquisa_vagas(request):
    if 'q' in request.GET:
        query = request.GET['q']
        vagas = Vaga.objects.filter(titulo__icontains=query)
    else:
        vagas = Vaga.objects.all()

    return render(request, 'vagas/vagas.html', {'vagas': vagas})


def pagconfig(request):
    return render(request, "pagconfig/pagconfig.html")
