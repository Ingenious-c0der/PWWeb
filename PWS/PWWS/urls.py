from django.urls import path 
from .views import LoginView,UploadFileView,DownloadFileView
from django.conf import settings
from django.conf.urls.static import static
app_name = "PWWS"
urlpatterns = [
    path('login/',LoginView.as_view(),name = "login"),
    path('upload_file/',UploadFileView.as_view(),name = "upload_file"),
    path('download_file/',DownloadFileView.as_view(),name = "download_file"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
