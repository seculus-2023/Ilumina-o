
# Register your models here.
from django.contrib import admin
from .models import Poste
from .models import Usuario

admin.site.register(Poste)
admin.site.register(Usuario)