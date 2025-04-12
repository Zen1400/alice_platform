from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
    required=True,
    widget=forms.DateInput(attrs={'type': 'date'})
    )
    domain = forms.ChoiceField(
        required=True,
        choices=[
            ('it', 'IT'),
            ('business', 'Business'),
            ('design', 'Design'),
            ('marketing', 'Marketing'),
            ('other', 'Other'),
            ('student', 'Student'),
            ('data', 'Data'),
            ('developer', 'Developer'),
        ]
    )
    city = forms.CharField(required=True, max_length=100)
    country = forms.CharField(required=True, max_length=100)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        username = forms.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Username can only contain letters, digits, and @/./+/-/_',
                code='invalid_username'
            )
            ],
            help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        )
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email