from django.contrib import admin
from crudapi.models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'email']