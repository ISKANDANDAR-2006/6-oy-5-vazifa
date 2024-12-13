
from django.shortcuts import render, get_object_or_404
from .models import Course, Student

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = course.students.all()
    return render(request, "courses/course_detail.html", {"course": course, "students": students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "courses/student_detail.html", {"student": student})
