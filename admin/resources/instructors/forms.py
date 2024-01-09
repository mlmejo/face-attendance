from django import forms


class InstructorCreationForm(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(label="Email address", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class InstructorChangeForm(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(label="Email address", max_length=255)
