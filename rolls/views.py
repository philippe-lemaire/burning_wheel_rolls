from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .roll import roll

from .forms import RollForm


def roll_dice(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RollForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, template_name="rolls/roll_dice.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RollForm()

    return render(request, "rolls/roll_dice.html", {"form": form})


def assess_difficulty(request):
    return HttpResponse("Hello, do you want to assess difficulty?")
