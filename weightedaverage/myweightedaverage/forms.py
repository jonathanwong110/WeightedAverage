from django import forms
from .models import Assignment, TASK_CHOICES


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('name', 'task', 'grade', 'weight')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'task': forms.Select(choices=TASK_CHOICES, attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control', 'minlength': 1, 'maxlength': 3, }),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'minlength': 1, 'maxlength': 3}),
        }
