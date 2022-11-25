from rest_framework import serializers

from transactions.models import Transaction

from transaction_types.serializers import TransactionTypeSerializer
from businesses.serializers import BusinessSerializer

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "cpf",
            "date",
            "time",
            "value",
            "card_details",
        ]
        read_only_fields = [
            "id"
        ]
