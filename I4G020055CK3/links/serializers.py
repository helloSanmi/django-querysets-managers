from dataclasses import field
from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.Serializer):
    
    class Meta:
        model = Link
        fields = "__all__"