from django.db import models

# extennd the user model to use Django’s built-in authentication

from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for the student profile (optional)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
