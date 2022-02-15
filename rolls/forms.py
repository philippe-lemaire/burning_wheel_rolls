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

    dice = forms.IntegerField(
        label="How many dice are you rolling?",
        min_value=1,
        max_value=13,
    )
    obstacle = forms.IntegerField(
        label="What is the obstacle?",
        min_value=1,
        max_value=13,
    )

    open_ended = forms.BooleanField(label="Is the roll open-ended?", required=False)
