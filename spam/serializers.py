from rest_framework import serializers
from .models import SpamNumber

class SpamNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamNumber
        fields = ['phone_number', 'spam_count']
