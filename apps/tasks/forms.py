from django import forms
from apps.tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description')
