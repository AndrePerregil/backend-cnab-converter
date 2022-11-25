from django.db import models

class Transaction(models.Model):
    date = models.DateField()
    value = models.DecimalField(max_digits=52, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card_details = models.CharField(max_length=12)
    time = models.TimeField()
    
    transaction_type = models.ForeignKey(
        "transaction_types.Transaction_type",
        on_delete = models.CASCADE,
        blank = False,
        null = False,
        related_name="transactions_of_this_type"
    )
    
    business = models.ForeignKey(
        "businesses.Business",
        on_delete = models.CASCADE,
        blank = False,
        null = False,
        related_name = "related_transactions"
    )

