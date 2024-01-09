from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import DeleteView, FormView, ListView
from django.views.generic.detail import SingleObjectMixin

from accounts.models import User
from admin.models import Instructor

from .forms import InstructorChangeForm, InstructorCreationForm


class InstructorListView(ListView):
    model = Instructor
    template_name = 'admin/instructors/index.html'


class InstructorCreateView(FormView):
    form_class = InstructorCreationForm
    template_name = 'admin/instructors/create.html'
    success_url = '/admin/instructors/'

    def form_valid(self, form: InstructorCreationForm):
        user = User(
            email=form.cleaned_data['email'],
            is_instructor=True
        )
        user.set_password(form.cleaned_data['password'])
        user.save()

        instructor = Instructor(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
        instructor.user = user
        instructor.save()

        return super().form_valid(form)


class InstructorUpdateView(SingleObjectMixin, FormView):
    model = Instructor
    form_class = InstructorChangeForm
    template_name = 'admin/instructors/edit.html'
    success_url = '/admin/instructors/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        self.object: Instructor
        form.initial = {
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'email': self.object.user.email,
        }

        return form

    def form_valid(self, form: InstructorChangeForm):
        instructor: Instructor = self.get_object()

        instructor.first_name = form.cleaned_data['first_name']
        instructor.last_name = form.cleaned_data['last_name']
        instructor.save()

        instructor.user.email = form.cleaned_data['email']
        instructor.user.save()

        return super().form_valid(form)


class InstructorDeleteView(DeleteView):
    model = User
    template_name = 'admin/instructors/delete.html'
    success_url = '/admin/instructors/'
