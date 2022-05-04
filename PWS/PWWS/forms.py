from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']
    
        def __init__(self , *args , **kwargs):
            super (LoginForm , self).__init__(*args , **kwargs)

            self.fields["username"].widget.attrs['class'] = 'form-control'
            self.fields["password"].widget.attrs['class'] = 'form-control'


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type': 'date'}))
