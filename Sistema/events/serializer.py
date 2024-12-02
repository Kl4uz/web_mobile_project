from events.models import Eventos
from django.contrib.auth.models import User
from rest_framework import serializers

class event_serializer(serializers.ModelSerializer):

    class Meta:
        model = Eventos
        exclude = []
