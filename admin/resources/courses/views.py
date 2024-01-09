from django.forms import Field
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from admin.models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'admin/courses/index.html'


class CourseCreateView(CreateView):
    model = Course
    fields = ['name']
    template_name = 'admin/courses/create.html'
    success_url = '/admin/courses/'


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name']
    template_name = 'admin/courses/edit.html'
    success_url = '/admin/courses/'


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'admin/courses/delete.html'
    success_url = '/admin/courses/'
