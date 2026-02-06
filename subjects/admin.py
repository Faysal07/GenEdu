from django.contrib import admin

from .models import Subject

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subjectId", "subjectName", "subjectCatagory", "subjectCreated",)
    search_fields = ("subjectName", "subjectCatagory",)
    
admin.site.register(Subject, SubjectAdmin)
