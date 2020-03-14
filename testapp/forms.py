from django import forms
from .models import User,Student
from django.contrib.auth.forms import UserCreationForm



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['father_name','mother_name','college_name','std_cell_no','parent_cell_no']


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name', 'password1', 'password2']
