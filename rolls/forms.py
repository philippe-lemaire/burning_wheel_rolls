from mimetypes import init
from django import forms

shade_choices = [
    ("B", "Black"),
    ("G", "Gray"),
    ("W", "White"),
]


class RollForm(forms.Form):

    shade = forms.ChoiceField(
        label="Abiltity shade",
        choices=shade_choices,
    )

    natural_dice = forms.IntegerField(
        label="How many dice are you rolling from exponent, help and FoRKs?",
        min_value=0,
        max_value=13,
        initial=1,
    )

    artha_dice = forms.IntegerField(
        label="How many extra dice are you rolling from Artha spending?",
        min_value=0,
        max_value=10,
        initial=0,
        required=False,
    )

    obstacle = forms.IntegerField(
        label="What is the obstacle?",
        min_value=1,
        max_value=13,
    )

    open_ended = forms.BooleanField(label="Is the roll open-ended?", required=False)


class AssessDifficultyForm(forms.Form):
    natural_dice = forms.IntegerField(
        label="How many dice did you roll from exponent, help and FoRKs?",
        min_value=0,
        max_value=13,
    )

    obstacle = forms.IntegerField(
        label="What was the obstacle?",
        min_value=1,
        max_value=13,
    )
