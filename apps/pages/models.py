from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Poste(models.Model):
    numero = models.CharField(max_length=50, unique=True, verbose_name="Número do Poste")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    endereco = models.CharField(max_length=255, default="Não disponível", verbose_name="Endereço")
    cidade = models.CharField(max_length=100, default="Não disponível", verbose_name="Cidade")
    estado = models.CharField(max_length=100, default="Não disponível", verbose_name="Estado")
    pais = models.CharField(max_length=100, default="Não disponível", verbose_name="País")
    foto = models.TextField(blank=True, null=True, verbose_name="Foto (Base64)")  # Para armazenar a foto em base64
    defeito = models.BooleanField(default=False, verbose_name="Possui Defeito?")  # Novo campo
    # Alternativa: use ImageField se preferir salvar a foto como arquivo
    # foto = models.ImageField(upload_to='fotos_postes/', blank=True, null=True, verbose_name="Foto")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    

    def __str__(self):
        return f"Poste {self.numero} - {self.cidade}, {self.estado}"

    class Meta:
        verbose_name = "Poste"
        verbose_name_plural = "Postes"

   

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, password=None, **extra_fields):
        if not usuario:
            raise ValueError('O campo usuário é obrigatório')
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(password)  # Criptografa a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password=None, **extra_fields):
        extra_fields.setdefault('ativo', True)
        return self.create_user(usuario, password, **extra_fields)

class Usuario(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)  # Na prática, use PasswordField
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.usuario