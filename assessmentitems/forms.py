
from django import forms
from .models import AssessmentItems


class AssessmentItemsForm(forms.ModelForm):
    model = AssessmentItems
    fields = ('item', 'compliance_level_id', 'measures', 'reasonfornotapplicable')
