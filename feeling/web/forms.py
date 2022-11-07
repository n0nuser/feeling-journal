from django import forms
from tempus_dominus.widgets import DateTimePicker

from web.models import Journal, Thought, Habit, Cue, Routine, Reward


class JournalForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                "useCurrent": True,
                "collapse": False,
            },
            attrs={
                "append": "fa fa-calendar",
                "input_toggle": False,
                "icon_toggle": True,
            },
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


class HabitForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                "useCurrent": True,
                "collapse": False,
            },
            attrs={
                "append": "fa fa-calendar",
                "input_toggle": False,
                "icon_toggle": True,
            },
        ),
    )

    class Meta:
        model = Habit
        fields = (
            "ocurred_at",
            "number_of_times",
            "cue",
            "routine",
            "reward",
        )
        labels = {
            "cue": "Cue: What triggered the habit?",
            "routine": "Routine: What did you do?",
            "reward": "Reward: What did you get out of it?",
        }


class CueForm(forms.ModelForm):
    class Meta:
        model = Cue
        fields = ("trigger", )
        labels = {
            "trigger": "Describe a trigger that makes you want to do this X habit",
        }


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ("response", )
        labels = {
            "response": "Describe a response that you do when you feel this X habit",
        }


class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ("reward", )
        labels = {
            "reward": "Describe a reward that you get when you do this X habit",
        }
