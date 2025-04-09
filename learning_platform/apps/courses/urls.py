from django.urls import path
from . import views

app_name = 'courses'   # This registers the namespace for the app, allowing you to use 'courses:home' in templates and views.


urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/content/', views.course_content, name='course_content'),
    path('<int:course_id>/purchase/', views.purchase_course, name='purchase_course'),
]
