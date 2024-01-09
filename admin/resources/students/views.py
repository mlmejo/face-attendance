from django.views.generic import DeleteView, FormView, ListView
from django.views.generic.detail import SingleObjectMixin

from accounts.models import User
from admin.models import Student

from .forms import StudentChangeForm, StudentCreationForm


class StudentListView(ListView):
    model = Student
    template_name = 'admin/students/index.html'


class StudentCreateView(FormView):
    form_class = StudentCreationForm
    template_name = 'admin/students/create.html'
    success_url = '/admin/students/'

    def form_valid(self, form: StudentCreationForm):
        user = User(
            email=form.cleaned_data['email'],
            is_student=True
        )
        user.set_password(form.cleaned_data['password'])
        user.save()

        student = Student(
            course = form.cleaned_data['course'],
            user=user,
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
        student.save()

        return super().form_valid(form)


class StudentUpdateView(SingleObjectMixin, FormView):
    model = Student
    form_class = StudentChangeForm
    template_name = 'admin/students/edit.html'
    success_url = '/admin/students/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        self.object: Student
        form.initial = {
            'course': self.object.course,
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'email': self.object.user.email,
        }

        return form

    def form_valid(self, form: StudentChangeForm):
        student: Student = self.get_object()

        student.course = form.cleaned_data['course']
        student.first_name = form.cleaned_data['first_name']
        student.last_name = form.cleaned_data['last_name']
        student.save()

        student.user.email = form.cleaned_data['email']
        student.user.save()

        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = User
    template_name = 'admin/students/delete.html'
    success_url = '/admin/students/'
