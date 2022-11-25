from owners.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
        ]
        read_only_fields = [
            "id",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        model = self.Meta.model
        instance = model.objects.create_user(**validated_data)
        return instance