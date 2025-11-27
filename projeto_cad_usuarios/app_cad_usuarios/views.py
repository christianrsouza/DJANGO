from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvando os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os usuarios ja cadastrados em uma nova pagina
    # colocar dentro de um dicionarios
    usuarios = {
        'usuarios': Usuario.objects.all()

    }
    #retornar os dados para pagina de usuarios
    return render (request,'usuarios/usuarios.html',usuarios)