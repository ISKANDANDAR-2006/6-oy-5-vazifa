from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("course/<int:pk>/", views.course_detail, name="course_detail"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
]
