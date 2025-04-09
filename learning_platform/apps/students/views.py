from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Student
from .forms import StudentSignUpForm
from apps.courses.models import Course
from django.contrib.auth.decorators import login_required



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
    courses = Course.objects.all()

    return render(request, 'students/home.html', {'courses': courses})

@login_required
def dashboard(request):
    # Assuming you have a related_name "enrollments" from enrollment model to user
    # For example: user.enrollments.all()
    return render(request, 'students/dashboard.html')


# def courses(request):
#     courses = Course.objects.all()
#     return render(request, 'students/courses.html', {'courses': courses})
