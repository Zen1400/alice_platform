from django.db import models

# extennd the user model to use Django’s built-in authentication

from django.db import models
from django.contrib.auth.models import User
from apps.courses.models import Course

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for the student profile (optional)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')  # Prevent duplicate enrollments

    def __str__(self):
        return f"{self.student} enrolled in {self.course.title}"