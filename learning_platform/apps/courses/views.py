# courses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from apps.students.models import Enrollment


def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # If the user is authenticated, check if they're already enrolled.
    if request.user.is_authenticated:
        student = request.user.student
        if Enrollment.objects.filter(student=student, course=course).exists():
            # Redirect enrolled students to the full course content view.
            return redirect('courses:course_content', course_id=course.id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def course_content(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = request.user.student
    # Ensure student is enrolled before allowing access to content.
    if not Enrollment.objects.filter(student=student, course=course).exists():
        return redirect('courses:course_detail', course_id=course.id)
    return render(request, 'courses/course_content.html', {'course': course})

@login_required
def purchase_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = request.user.student
    if request.method == 'POST':
        # In a later stage you will integrate Stripe payment logic here.
        # For now, we assume payment is successful.
        Enrollment.objects.get_or_create(student=student, course=course)
        return redirect('courses:course_content', course_id=course.id)
    # Render a placeholder payment page.
    return render(request, 'courses/payment.html', {'course': course})
