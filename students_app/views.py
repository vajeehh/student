from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm,StudentForm
from .models import Student
 
# Create your views here.
class students_list(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/list.html"

def Home(request):
    title={'title':'Home Page'}
    return render(request,'home.html',title)

def create_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('/')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    return render(request, 'registration/create.html', {'user_form': user_form, 'student_form': student_form})

def studentlist(request):
    students=Student.objects.all()
    return render(request,'registration/list.html',{'students':students})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.user.delete()
    return redirect('list') 





   