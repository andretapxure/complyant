from django import forms
from .models import Assessment
from assessmentitems.models import AssessmentItems


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ('name', 'customer', 'template', 'date')
        labels = {
            'name': 'Nome',
            'customer': 'Cliente',
            'template': 'Template',
            'date': 'Data',
        }

