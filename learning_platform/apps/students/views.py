# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from .models import Student
# from .forms import StudentSignUpForm
# from apps.courses.models import Course
# from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.decorators import login_required
from apps.courses.models import Course

from .models import Student
from .forms import StudentSignUpForm
from .tokens import account_activation_token

def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User remains inactive until email confirmation
            user.save()

            # Extract additional data and create Student
            date_of_birth = form.cleaned_data.get('date_of_birth')
            country = form.cleaned_data.get('country')
            city = form.cleaned_data.get('city')
            domain = form.cleaned_data.get('domain')
            profile_picture = form.cleaned_data.get('profile_picture')
            Student.objects.create(user=user, date_of_birth=date_of_birth, country=country, city=city, domain=domain, profile_picture=profile_picture)

            # Send activation email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('students/acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'noreply@yourdomain.com', [to_email])

            return redirect('activation_sent')
    else:
        form = StudentSignUpForm()
    return render(request, 'students/signup.html', {'form': form})

def activation_sent(request):
    return render(request, 'students/activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'students/activation_invalid.html')















# def signup(request):
#     if request.method == 'POST':
#         form = StudentSignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Optionally, you could create a Student profile here
#             Student.objects.create(user=user)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = StudentSignUpForm()
#     return render(request, 'students/signup.html', {'form': form})



def home(request):
    courses = Course.objects.all()

    return render(request, 'students/home.html', {'courses': courses})

# @login_required
# def dashboard(request):
#     # Assuming you have a related_name "enrollments" from enrollment model to user
#     # For example: user.enrollments.all()
#     return render(request, 'students/dashboard.html')

@login_required
def dashboard(request):
    # Get enrollments related to the student
    enrolled_enrollments = request.user.student.enrollments.all()  # QuerySet of Enrollment objects
    enrolled_course_ids = [enrollment.course.id for enrollment in enrolled_enrollments]
    
    # Get recommended courses (all courses not enrolled)
    recommended_courses = Course.objects.exclude(id__in=enrolled_course_ids)
    
    context = {
        'enrollments': enrolled_enrollments,
        'recommended_courses': recommended_courses,
    }
    
    return render(request, 'students/dashboard.html', context)
