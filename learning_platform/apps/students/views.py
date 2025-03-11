from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Student
from .forms import StudentSignUpForm


def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, you could create a Student profile here
            Student.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = StudentSignUpForm()
    return render(request, 'students/signup.html', {'form': form})



def home(request):
    return render(request, 'students/home.html')
