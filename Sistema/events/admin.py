from django.contrib import admin
from .models import Eventos
from rest_framework.authtoken.models import Token

admin.site.register(Eventos)
