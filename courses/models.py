from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Kurs tavsifi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Oxirgi tahrirlangan vaqt")

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Talaba ismi")
    email = models.EmailField(unique=True, verbose_name="Talaba email manzili")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro‘yxatdan o‘tgan vaqt")
    course = models.ForeignKey(Course, related_name="students", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
