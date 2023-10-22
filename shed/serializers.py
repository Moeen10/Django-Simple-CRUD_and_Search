from rest_framework import serializers
from .models import Shed_registration

class ShedRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shed_registration
        fields = '__all__'
