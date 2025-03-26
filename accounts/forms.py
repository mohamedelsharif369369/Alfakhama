from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import Profile
from django.contrib.auth.models import User
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Field


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


        #def __init__(self, *args, **kwargs):
            #super(SignupForm, self).__init__(*args, **kwargs)
            #self.helper = FormHelper()
            #self.helper.layout = Layout(
                #Field('username',css_class='form-control w-50'),
                #Field('email',css_class='form-control w-50'),
                #Field('password1',css_class='form-control w-50'),
                #Field('password2',css_class='form-control w-50'),
            #)



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number','address']
