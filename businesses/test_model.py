from django.test import TestCase
from django.forms import ValidationError
from django.db.utils import IntegrityError

from businesses.models import Business
from owners.models import User

class BusinessModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create(username = "username")
        cls.valid_business_data = {"name": "valid name"}
        cls.wrong_business_data = {"name": "a name that's far too big for a business"}
        cls.expected_keys = {
            "_state",
            "id",
            "name",
            "owner_id",
        }

    def test_create_a_valid_business(self):
        business = Business(name = self.valid_business_data["name"], owner = self.user)
        business_keys = set(vars(business).keys())

        self.assertEqual( business.name, self.valid_business_data["name"])
        self.assertEqual( business.owner, self.user)
        self.assertSetEqual(self.expected_keys, business_keys)

    def test_create_an_invalid_business(self):
        with self.assertRaises(ValidationError):
            business = Business(name = self.wrong_business_data["name"], owner = self.user)  
            business.full_clean()

    def test_create_without_owner(self):
        with self.assertRaises(ValidationError):
            business = Business(name = self.wrong_business_data["name"])  
            business.full_clean()

    def test_business_name_uniqueness(self):
        with self.assertRaises(IntegrityError):
            business = Business.objects.create(name = self.valid_business_data["name"], owner = self.user)
            business.full_clean()
            business_same_name = Business.objects.create(name = self.valid_business_data["name"], owner = self.user)
            business_same_name.full_clean()

    def test_N_to_1_relation_with_owner(self):
        business_1 = Business.objects.create(name = self.valid_business_data["name"], owner = self.user)
        business_2 = Business.objects.create(name = "original name", owner = self.user)

        self.assertEqual(business_1.owner_id, business_2.owner_id)

