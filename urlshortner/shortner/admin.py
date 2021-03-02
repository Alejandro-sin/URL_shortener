from django.contrib import admin
# Importo el modelo que quiero crear como base de datos.
from .models import Url


# Register your models here.


# Esto me permtirá resgistrar la clase dentro d ela base de datos.  
admin.site.register(Url)