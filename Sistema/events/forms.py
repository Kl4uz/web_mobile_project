from django.forms import ModelForm
from .models import Eventos
from django.http import HttpResponse
class EventForm(ModelForm):
    class Meta:
        model = Eventos
        fields = ['name', 'description', 'start_date', 'end_date', 'local', 'price', 'logo']
