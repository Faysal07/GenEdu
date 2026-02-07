from django.contrib import admin

from .models import Teacher

# Register your models here.

# Teacher Regioster Here
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacherSerial', 'teacherId', 'teacherName', 'teacherCardNo', 'teacherDesignation', 'teacherSubject', 'teacherCategory', 'teacherCreated', 'teacherInfo',)
    search_display = ('teacherId', 'teacherName', 'teacherDesignation', 'teacherSubject','teacherCategory',)
    

admin.site.register(Teacher, TeacherAdmin)
