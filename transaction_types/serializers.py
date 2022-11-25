from transaction_types.models import Transaction_type
from rest_framework import serializers

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_type
        fields = [
            "id",
            "type",
            "nature",
        ]
        read_only_fields = [
            "id",
        ]