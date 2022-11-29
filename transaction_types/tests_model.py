from django.test import TestCase
from django.forms import ValidationError
from django.db.utils import IntegrityError

from transaction_types.models import Transaction_type

class TransactionTypesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.trans_type_valid_data = {"type":"debit", "nature":"income"}
        
        """the following are invalid values for their intended fields"""
        cls.trans_type_wrong_data = {"type":"inheritance", "nature": "god_bless"}

        cls.expected_keys = {
            "_state",
            "id",
            "type",
            "nature",
        }


    def test_create_a_transaction_type(self):
        trans_type = Transaction_type(type = self.trans_type_valid_data["type"], nature = self.trans_type_valid_data["nature"])
        trans_type_keys = set(vars(trans_type).keys())

        self.assertEqual( trans_type.type, self.trans_type_valid_data["type"])
        self.assertEqual( trans_type.nature, self.trans_type_valid_data["nature"])
        self.assertSetEqual(self.expected_keys, trans_type_keys)

    def test_create_an_invalid_transaction_type(self):
        with self.assertRaises(ValidationError):
            trans_type = Transaction_type(type = self.trans_type_wrong_data["type"], nature = self.trans_type_valid_data["nature"])
            trans_type.full_clean()

    def test_create_an_invalid_transaction_nature(self):
        with self.assertRaises(ValidationError):
            trans_type = Transaction_type(type = self.trans_type_valid_data["type"], nature = self.trans_type_wrong_data["nature"])
            trans_type.full_clean()

    def test_transaction_type_uniqueness(self):
        with self.assertRaises(IntegrityError):
            first_trans_type = Transaction_type.objects.create(type = self.trans_type_valid_data["type"], nature = self.trans_type_valid_data["nature"])
            first_trans_type.full_clean()
            same_trans_type = Transaction_type.objects.create(type = self.trans_type_valid_data["type"], nature = self.trans_type_valid_data["nature"])
            same_trans_type.full_clean()
