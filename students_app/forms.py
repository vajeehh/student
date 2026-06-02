from django import forms
from django.contrib.auth.models import User
from datetime import date
from .models import Student
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }



class StudentForm(forms.ModelForm):
    COURSE_CHOICES = [
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Data Analytics', 'Data Analytics'),
        ('Python Developer', 'Python Developer'),
        ('UI/UX Designer', 'UI/UX Designer'),
    ]

    courses = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Student
        fields = [ 'courses', 'advisor','age']
        widgets = {
        
            'courses': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'}),
            'advisor': forms.Select(attrs={'class': 'form-control'}),
        }

    