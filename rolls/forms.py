from mimetypes import init
from django import forms

shade_choices = [
    ("B", "Black"),
    ("G", "Gray"),
    ("W", "White"),
]


class RollForm(forms.Form):

    shade = forms.ChoiceField(
        label="What is the Shade?",
        choices=shade_choices,
    )

    natural_dice = forms.ChoiceField(
        label="How many dice are you rolling from exponent, advantage, help and FoRKs?",
        choices=[(n, n) for n in range(13)],
    )

    artha_dice = forms.ChoiceField(
        label="How many extra dice are you rolling from Artha spending?",
        choices=[(n, n) for n in range(14)],
        required=False,
    )

    obstacle = forms.ChoiceField(
        label="What is the obstacle?",
        choices=[(n, n) for n in range(1, 14)],
    )

    open_ended = forms.BooleanField(label="Is the roll open-ended?", required=False)


class AssessDifficultyForm(forms.Form):
    natural_dice = forms.ChoiceField(
        label="How many dice are you rolling from exponent, advantage, help and FoRKs?",
        choices=[(n, n) for n in range(13)],
    )

    obstacle = forms.ChoiceField(
        label="What is the obstacle?",
        choices=[(n, n) for n in range(1, 14)],
    )
