from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job

FIELD_STYLE = 'width:100%;padding:0.6rem 0.8rem;border:1.5px solid #e2e8f0;border-radius:8px;font-size:0.95rem;outline:none;font-family:inherit;'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': FIELD_STYLE})


class JobForm(forms.ModelForm):
    class Meta:
        model   = Job
        fields  = ['company', 'role', 'status', 'job_url', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3, 'style': FIELD_STYLE}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'style': FIELD_STYLE})