
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Fornecedor,FornecedorForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def about(request):
        return HttpResponse("Hello, this is the about page of the coder app.")


def index(request):
    context = {'fornecedor': Fornecedor.objects.all()}
    return render(request, 'coder/index.html',context)

def detail(request,fornecedor_id):
    context = {'fornecedor': Fornecedor.objects.get(id=fornecedor_id)}
    return render(request, 'coder/detail.html',context)

   
def create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            Fornecedor.objects.create(**form.cleaned_data)
            return redirect('coder:index')
    else:
        form = FornecedorForm()
    return render(request, 'coder/create.html', {'form': form})


def delete(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('coder:index')
    return render(request, 'coder/delete.html', {'fornecedor': fornecedor})



def update(request,fornecedor_id):
     fornecedor = get_object_or_404(Fornecedor,id=fornecedor_id)
     form = FornecedorForm(instance=fornecedor)
     if request.method == 'POST':
          form = FornecedorForm(request.POST, instance=fornecedor)
          if not form.is_valid():
               return render(request, 'coder/update.html', {'form':form, 'fornecedor':fornecedor})     
          else:
               form.save()
          return redirect ('coder:index')
     else:
          return render(request, 'coder/update.html', {'form': form, 'fornecedor':fornecedor})




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/coder/')  # redireciona para /coder/
        else:
            # Você pode enviar mensagem de erro ou reexibir modal com erro
            return render(request, 'index.html', {'login_error': 'Credenciais inválidas'})
    else:
        # Se for GET, apenas redirecione para home ou outra página
        return redirect('/')



def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('/')  # Ou renderizar com erro

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return redirect('/')

        # Cria o usuário
        User.objects.create_user(username=email, email=email, password=senha, first_name=nome)

        messages.success(request, 'Cadastro realizado! Faça o login.')
        return redirect('/')  # Redireciona para página inicial


def home_view(request):
    return render(request, 'index.html')  # ou o nome do seu template
