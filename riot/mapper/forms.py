from django import forms

MAGNITUDE_LEVELS = (
    ('high','High'),
    ('medium','Medium'),
    ('low','Low'),
)



class RiotForm(forms.Form):
    location= forms.CharField()
    magnitude = forms.MultipleChoiceField(
        required = True,
        widget = forms.RadioSelect,
        choices = MAGNITUDE_LEVELS
    )
