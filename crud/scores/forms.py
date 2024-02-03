from django import forms
from .models import Score

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Score
        fields = ('__all__')
