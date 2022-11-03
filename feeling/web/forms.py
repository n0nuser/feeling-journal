from django import forms
from tempus_dominus.widgets import DateTimePicker

from web.models import Journal, Thought

class JournalForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
                
            },
            attrs={
                'append': 'fa fa-calendar',
                'input_toggle': False,
                'icon_toggle': True,
            }
        ),
    )
    
    class Meta:
        model = Journal
        fields = (
            "ocurred_at",
            "number_of_times",
            "situation_emotion",
            "afterwards_feeling",
        )
        labels = {
            "situation_emotion": "Situation/Emotion",
            "afterwards_feeling": "Afterwards Feeling",
        }
        
class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ("journal", "thought")
        labels = {
            "thought": "Thought",
            "journal": "Associated Journal (Optional)",
        }
