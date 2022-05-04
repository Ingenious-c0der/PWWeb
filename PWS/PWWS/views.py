from pathlib import Path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView , CreateView , View , FormView , DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate , login 
from .forms import LoginForm , UploadFileForm
from django.shortcuts import render,redirect
from .utils import extended_func
from .models import UploadFile 
import datetime

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm 
    success_url = reverse_lazy("PWWS:upload_file")
    def form_valid(self,form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        print(uname,pword)
        user = authenticate(username = uname,password = pword)
        if user is not None:
            login(self.request,user)
        else:
            form.add_error(None,"Invalid username or password")
        return super().form_valid(form)

class UploadFileView(FormView):
    template_name = "upload_file.html"
    form_class = UploadFileForm
    success_url = reverse_lazy("PWWS:download_file")
    def form_valid(self,form):
  
        file = form.cleaned_data["file"]
        if file.name.endswith(".csv") :
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            print(start_date,end_date)
            document = UploadFile.objects.create(file=file,start_date=start_date,end_date=end_date)
            document.save()
            x = extended_func(datetime.date(2022,2,22),datetime.date(2022,5,22),file.name)
            print(x)
            if x == 0:
                return redirect("PWWS:download_file")
        return(HttpResponseRedirect("Failed Please try again"))
            


class DownloadFileView(TemplateView):
    template_name = "download_file.html"


    



