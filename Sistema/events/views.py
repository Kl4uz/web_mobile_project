from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Eventos
from .forms import EventForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializer import event_serializer

class home(TemplateView):
    template_name = 'events/home.html'

    def post(self, request, *args, **kwargs):

        action_1 = request.POST.get('list')
        action_2 = request.POST.get('create')

        if action_1:
            return redirect('events-list')
        elif action_2:
            return redirect('events-create')


class event_list(LoginRequiredMixin, ListView):
    model = Eventos
    template_name = 'events/events_list.html'

#     def post(self, request):
#         search = request.POST.get('search')
#         events_f = Eventos.objects.all()
        
#         if search:
#             events_f.filter(name__contains = search)
        
#         return redirect('events-search')
        
# class events_search(LoginRequiredMixin, ListView):
    
#     def get(self, request):

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
        

class event_detail(LoginRequiredMixin, DetailView):
    model = Eventos
    template_name = 'events/events_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'events'

class event_create(LoginRequiredMixin, CreateView):
    model = Eventos
    form_class = EventForm
    template_name = 'events/events_form.html'
    context_object_name = 'events'
    success_url = reverse_lazy('events-home')

class API_events(ListAPIView):

    serializer_class = event_serializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Eventos.objects.all()

    # curl -X GET -H "Authorization: Token SEU_TOKEN " http://127.0.0.1:8000/home/api
