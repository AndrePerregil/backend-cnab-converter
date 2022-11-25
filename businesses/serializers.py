from businesses.models import Business
from rest_framework import serializers

from owners.serializers import UserSerializer

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = [
            "id",
            "name",
        ]
        read_only_fields = [
            "id"
        ]
