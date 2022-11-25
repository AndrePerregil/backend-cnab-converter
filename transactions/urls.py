from django.urls import path
from transactions import views

urlpatterns = [
    path(
        "upload/",
        views.UploadCNABView.as_view(),
    )
]