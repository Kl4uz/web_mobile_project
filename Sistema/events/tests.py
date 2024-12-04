from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from .models import Eventos
from django.contrib.auth.models import User

class EventAPITestCase(APITestCase):
    
    def setUp(self):

        # self.user = User.objects.get(username='admin', password='984845587_Lk$')
        # self.token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.event = Eventos.objects.create(
            name = "XII Meia Maratona do Tocantins",
            description = "Promovida pelo Governo do Tocantins, por meio da Secretaria de Estado dos Esportes e Juventude",
            # start_date = "2024-11-27 10:30:00",
            # end_date = "2024-11-27 13:30:00",
            local = "Palmas-TO",
            price = 0,
        )
        self.list_url = reverse('events-list')


    def test_get_event_list(self):
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.json())  # Para confirmar o formato



    def test_create_event(self):

        data = {
            "name": "Evento tesst",
            "description": "Descrição de teste",
            "local": "Local do evento",
            "price": 10
        }
    
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Eventos.objects.count(), 1)

        # response = self.client.get(self.list_url)
        print(response.status_code, response.content)

