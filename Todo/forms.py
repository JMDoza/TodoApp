from django import forms
from .models import Todo

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_name', 'completed']

        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }