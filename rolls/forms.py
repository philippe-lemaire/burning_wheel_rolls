from django import forms


class RollForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
