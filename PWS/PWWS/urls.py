from django.urls import path 
from .views import LoginView,UploadFileView,DownloadFileView
app_name = "PWWS"
urlpatterns = [
    path('login/',LoginView.as_view(),name = "login"),
    path('upload_file/',UploadFileView.as_view(),name = "upload_file"),
    path('download_file/',DownloadFileView.as_view(),name = "download_file"),
]
