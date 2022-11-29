from forms import UploadForm
from utils.handlers import CNAB_handler, summary_generator
from utils.db_data_parser import db_parser

from django.shortcuts import render  
from django.http import HttpResponse
from rest_framework.views import APIView, Request, Response

from forms import UploadForm

def upload(request):
    if request.method == "POST":
        upload = UploadForm(request.POST, request.FILES)
        if upload.is_valid():
            data = upload.cleaned_data.get("file")
            
            file_data = CNAB_handler(data)
            
            summary = summary_generator()
            data = db_parser(file_data)
            
            return HttpResponse(data)
    else:
        upload_form = UploadForm()
        return render(request, "transactions/form.html", {"form":upload_form})

class UploadCNABView(APIView):
    def post(self, request:Request) -> Response:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.data["file"]

            handle_file = CNAB_handler(data)
            summary = summary_generator()

            return Response({"decoded_file_data":handle_file, "accounts_summary":summary})
        return Response("no file recieved", status=400)
