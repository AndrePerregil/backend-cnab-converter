from django.test import TestCase
from django.forms import ValidationError

from businesses.models import Business
from owners.models import User
from transaction_types.models import Transaction_type
from transactions.models import Transaction

class TransactionModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create(username = "username")
        cls.business = Business.objects.create(name = "original name", owner = cls.user)
        cls.transaction_type = Transaction_type.objects.create(type = "debit", nature = "expense")
        cls.valid_transaction_data = {
            "date": "2022-01-01",
            "value": 100.00,
            "cpf": "09620676017",
            "card_details": "4753****3153",
            "time": "15:34:53",
        }
        cls.expected_keys = {
            "_state",
            "id",
            "date",
            "value",
            "cpf",
            "card_details",
            "time",
            "business_id",
            "transaction_type_id"
        }

    def test_create_valid_transaction(self):
        transaction = Transaction(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = self.valid_transaction_data["date"],
            value = self.valid_transaction_data["value"],
            cpf = self.valid_transaction_data["cpf"],
            card_details = self.valid_transaction_data["card_details"],
            time = self.valid_transaction_data["time"]
        )
        transaction_keys = set(vars(transaction).keys())

        self.assertEqual( transaction.date, self.valid_transaction_data["date"])
        self.assertEqual( transaction.value, self.valid_transaction_data["value"])
        self.assertEqual( transaction.cpf, self.valid_transaction_data["cpf"])
        self.assertEqual( transaction.card_details, self.valid_transaction_data["card_details"])
        self.assertEqual( transaction.time, self.valid_transaction_data["time"])

        self.assertEqual( transaction.business, self.business)
        self.assertEqual( transaction.transaction_type, self.transaction_type)
        self.assertSetEqual(self.expected_keys, transaction_keys)

    def test_create_an_invalid_transaction_date(self):
        with self.assertRaises(ValidationError):
            transaction = Transaction(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = "not a date",
            value = self.valid_transaction_data["value"],
            cpf = self.valid_transaction_data["cpf"],
            card_details = self.valid_transaction_data["card_details"],
            time = self.valid_transaction_data["time"]
            )
            transaction.full_clean()

    def test_create_an_invalid_transaction_value(self):
        with self.assertRaises(ValidationError):
            transaction = Transaction(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = self.valid_transaction_data["date"],
            value = "not a float/decimal",
            cpf = self.valid_transaction_data["cpf"],
            card_details = self.valid_transaction_data["card_details"],
            time = self.valid_transaction_data["time"]
            )
            transaction.full_clean()

    def test_create_an_invalid_transaction_cpf(self):
        with self.assertRaises(ValidationError):
            transaction = Transaction(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = self.valid_transaction_data["date"],
            value = self.valid_transaction_data["value"],
            cpf = self.valid_transaction_data["cpf"]+"too big",
            card_details = self.valid_transaction_data["card_details"],
            time = self.valid_transaction_data["time"]
            )
            transaction.full_clean()

    def test_create_an_invalid_transaction_card(self):
        with self.assertRaises(ValidationError):
            transaction = Transaction(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = self.valid_transaction_data["date"],
            value = self.valid_transaction_data["value"],
            cpf = self.valid_transaction_data["cpf"],
            card_details = self.valid_transaction_data["card_details"] + "too big",
            time = self.valid_transaction_data["time"]
            )
            transaction.full_clean()
    
    def test_create_an_invalid_transaction_time(self):
        with self.assertRaises(ValidationError):
            transaction = Transaction(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = self.valid_transaction_data["date"],
            value = self.valid_transaction_data["value"],
            cpf = self.valid_transaction_data["cpf"],
            card_details = self.valid_transaction_data["card_details"],
            time = "not time"
            )
            transaction.full_clean()

    def test_N_to_1_relation_with_business_and_transaction_type(self):
        transaction_1 = Transaction.objects.create(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = self.valid_transaction_data["date"],
            value = self.valid_transaction_data["value"],
            cpf = self.valid_transaction_data["cpf"],
            card_details = self.valid_transaction_data["card_details"],
            time = self.valid_transaction_data["time"]  
        )
        transaction_2 = Transaction.objects.create(
            business = self.business, 
            transaction_type = self.transaction_type,
            date = "2022-01-01",
            value = 150.00,
            cpf = "09620676017",
            card_details = "4753****3153",
            time = "16:34:53",
        )

        self.assertEqual(transaction_1.business, transaction_2.business)
        self.assertEqual(transaction_1.transaction_type, transaction_2.transaction_type)