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
            # retrieve the values from the form
            shade = form.cleaned_data["shade"]
            dice = form.cleaned_data["dice"]
            obstacle = form.cleaned_data["obstacle"]
            open_ended = form.cleaned_data["open_ended"]
            # call the roll function
            rolls, result = roll(
                shade=shade, dice=dice, obstacle=obstacle, open_ended=open_ended
            )

            context = {"form": form, "rolls": rolls, "result": result}
            return render(
                request, template_name="rolls/roll_dice.html", context=context
            )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RollForm()

    return render(request, "rolls/roll_dice.html", {"form": form})


def assess_difficulty(request):
    return HttpResponse("Hello, do you want to assess difficulty?")
