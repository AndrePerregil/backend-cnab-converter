from owners.models import User
from businesses.models import Business
from transactions.models import Transaction
from transaction_types.models import Transaction_type

from owners.serializers import UserSerializer
from businesses.serializers import BusinessSerializer
from transactions.serializers import TransactionSerializer
from transaction_types.serializers import TransactionTypeSerializer

from utils.forms import UploadFileForm
from utils.decoders import decode_data

import ipdb

from rest_framework.views import APIView, Request, Response, status

class UploadCNABView(APIView): 
    def post(self, request:Request) -> Response:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            content = []
            transactions = []
            data = request.data["file"]
            
            for line in data:
                content.append(decode_data(line.decode("utf-8")))

            for entry in content:
                transaction_types_data = {"type":entry["type"], "nature":entry["nature"]}
                serializer = TransactionTypeSerializer(transaction_types_data)                
                transaction_type, t_created = Transaction_type.objects.get_or_create(**serializer.data)
                if t_created:
                    transaction_type.save()

                owner_data = {"username" : entry["owner"]}
                serializer = UserSerializer(owner_data)
                owner, o_created = User.objects.get_or_create(**serializer.data)
                if o_created:
                    owner.save()

                business_data = {"name":entry["business"], "owner" : owner}
                serializer = BusinessSerializer(business_data)
                business, b_created = Business.objects.get_or_create(**serializer.data, owner=owner)
                if b_created:
                    business.save()

                transaction_data = {
                    "date" : entry["date"], 
                    "value" : entry["value"],
                    "cpf" : entry["cpf"],
                    "card_details" : entry["card"],
                    "time" : entry["time"],
                }
                serializer = TransactionSerializer(transaction_data)
                transaction = Transaction(**serializer.data, transaction_type = transaction_type, business = business)
                transactions.append(transaction)

            Transaction.objects.bulk_create(transactions)

            all_users = User.objects.all()
            summary = []

            for user in all_users:
                user_businesses = Business.objects.filter(owner=user)
                user_businesses_data = []
                user_account_balance = 0
                
                for business in user_businesses:    
                    income_business_transactions = Transaction.objects.filter(business=business).filter(transaction_type__nature = "income")
                    expense_bussiness_transactions = Transaction.objects.filter(business=business).filter(transaction_type__nature = "expense")
                    business_account_balance = 0

                    for transaction in income_business_transactions:
                        business_account_balance += transaction.value
                        user_account_balance += transaction.value

                    for transaction in expense_bussiness_transactions:
                        business_account_balance -= transaction.value
                        user_account_balance -= transaction.value                   
                    
                    user_businesses_data.append({
                        "business_id":business.id,
                        "business_name": business.name,
                        "business_balance": business_account_balance   
                    })

                user_data = {
                    "user_id": user.id,
                    "username": user.username,
                    "total_balance": user_account_balance,
                    "businesses": user_businesses_data
                }

                summary.append(user_data)

            return Response({"decoded_file_data":content, "accounts_summary":summary})
        return Response("no file recieved", status=400)