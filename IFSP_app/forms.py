from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Tool, ToolCopy

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image')


# class CreateToolForm(forms.ModelForm):
#     class Meta:
#         model = Tool
#         fields = ['title', 'manufacturer', 'date_production', 'category', 'ean_code', 'image']
#
#
# class CreateToolCopyDetailForm(forms.ModelForm):
#     class Meta:
#         model = ToolCopy
#         fields = ['tool', 'customer']
