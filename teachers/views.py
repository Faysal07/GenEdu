from django.shortcuts import render

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from teachers.models import Teacher

# Create your views here.

# My Created View Here
class TeacherListView(ListView):
    template_name = 'teacher.html'
    model = Teacher
    context_object_name = 'teachers'
    paginate_by = 6
