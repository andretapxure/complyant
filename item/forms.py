from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'risk_type', 'category', 'risk', 'how_to_assess')
        labels = {
            'name': 'Nome',
            'riskType': 'Tipo de risco',
            'category': 'Categoria',
            'risk': 'Risco provável',
            'how_to_assess': 'Como avaliar',
        }

