from django import forms
from .models import Riot

MAGNITUDE_LEVELS = (
    ('high','High'),
    ('medium','Medium'),
    ('low','Low'),
)



class RiotForm(forms.ModelForm):
    class Meta:

        model = Riot
        fields = ('location','magnitude',)
