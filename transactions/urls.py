from django.urls import path
from transactions import views

urlpatterns = [
    path(
        "data/",
        views.UploadCNABView.as_view(),
    ),
    path(
        "upload/",
        views.upload
    ),
]