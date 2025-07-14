from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .models import Usuario  # Supondo que você tenha um modelo Usuario
from .models import Poste

import json
import logging

# Create your views here.
def index(request):
    return render(request, 'index.html')

def mapa_view(request):
    postes = Poste.objects.all()  # Recupera todos os postes do banco
    return render(request, 'mapa.html', {'postes': postes})

def latitude_view(request):
    return render(request, 'latitude.html')

def qrcode_view(request):
    return render(request, 'qrcode.html')


@csrf_exempt  # Use com cautela; em produção, prefira csrf_protect com token
def registrar_poste(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            poste = Poste(
                numero=data['numero'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                endereco=data['endereco'],
                cidade=data['cidade'],
                estado=data['estado'],
                pais=data['pais'],
                foto=data['foto']  # Salva como base64
            )
            poste.save()
            return JsonResponse({'status': 'success', 'message': 'Poste registrado com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)



logger = logging.getLogger(__name__)


def latitude_view(request):
    postes = Poste.objects.all()
    for poste in postes:
        print(f"Poste {poste.numero}: Latitude={poste.latitude}, Longitude={poste.longitude}")  # Imprime apenas latitude e longitude
    return render(request, 'latitude.html', {'postes': postes})


def login_view(request):
    error_message = None
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        try:
            # Verificar se o usuário existe e está ativo
            usuario_obj = Usuario.objects.get(usuario=usuario, ativo=True)
            
            # Verificar a senha (em produção, use check_password com senhas criptografadas)
            if usuario_obj.senha == senha:  # Isso é apenas para exemplo!
                return redirect('latitude')  # Redireciona para a página latitude
            else:
                error_message = "Senha incorreta"
        except Usuario.DoesNotExist:
            error_message = "Usuário não encontrado ou inativo"
    
    return render(request, 'login.html', {'error_message': error_message})