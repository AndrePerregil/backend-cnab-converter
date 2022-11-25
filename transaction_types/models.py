from django.db import models

class Transaction_categories(models.TextChoices):
    DEBIT = "debit"
    TICKET = "ticket"
    FINANCING = "financing"
    CREDIT = "credit"
    LOAN_INCOME = "loan"
    SALE = "sale"
    TRANSFER_TED = "express tranfer"
    TRANFER_POD = "standard tranfer"
    RENT = "rent"

class Transaction_nature(models.TextChoices):
    INCOME = "income"
    EXPENSE = "expense"

class Transaction_type (models.Model):
    type = models.CharField(choices = Transaction_categories.choices, max_length=17, unique=True)
    nature = models.CharField(choices = Transaction_nature.choices, max_length=7)