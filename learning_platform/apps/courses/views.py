from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/course_list.html', {'courses': courses})
