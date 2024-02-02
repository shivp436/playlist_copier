from django import forms
from .models import Source

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['source']
        widgets = {
            'source': forms.Select(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source'].initial = 'spotify'  # Set the initial value to 'spotify'