from django.contrib.auth.models import User
from contactos.models import Person, Group
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('name', 'phone_number', 'direccion', 'user')

class GoupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'description')