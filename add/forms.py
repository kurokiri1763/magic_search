from django import forms
from search.models import Magic

class MagicForm(forms.ModelForm):
    class Meta:
        model = Magic
        fields = [
            'name', 'magic_type', 'rank', 'target', 'range_shape', 
            'resistance', 'duration', 'cost', 'summary', 
            'attribute', 'effect', 'extended_effect1', 'extended_effect2',
            'spell'
        ]
        widgets = {
            'effect': forms.Textarea(attrs={'rows': 4}),
            'summary': forms.Textarea(attrs={'rows': 2}),
            'extended_effect1': forms.Textarea(attrs={'rows': 2}),
            'extended_effect2': forms.Textarea(attrs={'rows': 2}),
        }
