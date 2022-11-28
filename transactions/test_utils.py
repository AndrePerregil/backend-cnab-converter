from django.test import TestCase
from utils.decoders import decode_data

class test_file_reading(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.valid_data = "3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       "
        cls.invalid_length = "3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       123123"
        cls.invalid_type = "0201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       "
        cls.invalid_date = "3testtest0000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       "
        cls.invalid_value = "32019030100000not00096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       "
        cls.invalid_cpf = "32019030100000142000962067test4753****3153153453JOÃO MACEDO   BAR DO JOÃO       "
        cls.invalid_time = "3201903010000014200096206760174753****3153notnotJOÃO MACEDO   BAR DO JOÃO       "

        cls.expected_keys = {
            "type", 
            "nature",
            "date", 
            "value",
            "cpf",
            "card",
            "time",
            "owner",
            "business",  
        }

        cls.expected_result = {
            "type":"financing", 
            "nature": "expense",
            "date": "2019-03-01", 
            "value": 142.0,
            "cpf": "09620676017",
            "card": "4753****3153",
            "time": "15:34:53",
            "owner": "JOÃO MACEDO   ",
            "business": "BAR DO JOÃO       "
        }
    
    def test_file_reading_valid_data(self):
        decoded_data = decode_data(self.valid_data)
        decoded_data_keys = set(decoded_data.keys())

        self.assertSetEqual(decoded_data_keys, self.expected_keys)
        
        self.assertEqual(decoded_data["type"], self.expected_result["type"])
        self.assertEqual(decoded_data["nature"], self.expected_result["nature"])
        self.assertEqual(decoded_data["date"], self.expected_result["date"])
        self.assertEqual(decoded_data["value"], self.expected_result["value"])
        self.assertEqual(decoded_data["cpf"], self.expected_result["cpf"])
        self.assertEqual(decoded_data["card"], self.expected_result["card"])
        self.assertEqual(decoded_data["time"], self.expected_result["time"])
        self.assertEqual(decoded_data["owner"], self.expected_result["owner"])
        self.assertEqual(decoded_data["business"], self.expected_result["business"])

    def test_file_reading_invalid_data_length(self):
        decoded_data = decode_data(self.invalid_length)

        self.assertEqual(decoded_data, "not CNAB")

    def test_file_reading_invalid_data_cpf(self):
        decoded_data = decode_data(self.invalid_cpf)

        self.assertEqual(decoded_data, "not CNAB")

    def test_file_reading_invalid_data_date(self):
        decoded_data = decode_data(self.invalid_date)

        self.assertEqual(decoded_data, "not CNAB")

    def test_file_reading_invalid_data_(self):
        decoded_data = decode_data(self.invalid_time)

        self.assertEqual(decoded_data, "not CNAB")

    def test_file_reading_invalid_data_type(self):
        decoded_data = decode_data(self.invalid_type)

        self.assertEqual(decoded_data, "not CNAB")

    def test_file_reading_invalid_data_value(self):
        decoded_data = decode_data(self.invalid_value)

        self.assertEqual(decoded_data, "not CNAB")