from django import forms

from admin.models import Course


class StudentCreationForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(label='Email address', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class StudentChangeForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(label='Email address', max_length=255)
