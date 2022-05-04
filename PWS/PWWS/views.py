from django.shortcuts import render
from django.views.generic import TemplateView , CreateView , View , FormView , DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate , login 
from .forms import LoginForm , UploadFileForm
from django.shortcuts import render,redirect
from .utils import extended_func

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm 
    success_url = reverse_lazy("PWWS:upload_file")
    def form_valid(self,form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username = uname,password = pword)
        if user is not None:
            login(self.request,user)
        else:
            form.add_error(None,"Invalid username or password")
        return super().form_valid(form)


class UploadFileView(TemplateView):
    template_name = "upload_file.html"

    
    def upload_file(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return redirect('/success/url/')
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})


class DownloadFileView(TemplateView):
    template_name = "download_file.html"


    



