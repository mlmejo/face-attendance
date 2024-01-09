from django.forms import Field
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from admin.models import Subject


class SubjectListView(ListView):
    model = Subject
    template_name = 'admin/subjects/index.html'


class SubjectCreateView(CreateView):
    model = Subject
    fields = [
        'course',
        'descriptive_title',
        'course_number',
        'lecture_hours',
        'laboratory_hours',
        'units',
    ]
    template_name = 'admin/subjects/create.html'
    success_url = '/admin/subjects/'


class SubjectUpdateView(UpdateView):
    model = Subject
    fields = [
        'course',
        'descriptive_title',
        'course_number',
        'lecture_hours',
        'laboratory_hours',
        'units',
    ]
    template_name = 'admin/subjects/edit.html'
    success_url = '/admin/subjects/'


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'admin/subjects/delete.html'
    success_url = '/admin/subjects/'
