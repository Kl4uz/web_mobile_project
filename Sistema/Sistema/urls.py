from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authuser, name='auth-user'),
    path('login', login, name = 'login'),
    path('cadastro', cadastro, name = 'cadastro'),
    path('api/', include('events.urls'), name ='events-home'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

