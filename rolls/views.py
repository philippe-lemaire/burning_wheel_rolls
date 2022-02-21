from django.http import HttpResponse
from django.shortcuts import render

from .roll import roll
from .assess_difficulty import difficulty

from .forms import RollForm, AssessDifficultyForm


def roll_dice(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RollForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # retrieve the values from the form
            shade = form.cleaned_data["shade"]
            natural_dice = int(form.cleaned_data.get("natural_dice", 0))
            artha_dice = form.cleaned_data.get("artha_dice")
            if artha_dice is None:
                artha_dice = 0
            else:
                artha_dice = int(artha_dice)
            obstacle = int(form.cleaned_data["obstacle"])
            open_ended = form.cleaned_data["open_ended"]

            # count dice rolled
            if not artha_dice:
                artha_dice = 0

            dice_rolled = natural_dice + artha_dice

            # call the roll function
            rolls, result = roll(
                shade=shade, dice=dice_rolled, obstacle=obstacle, open_ended=open_ended
            )

            # assess the difficulty
            assessed_difficulty = difficulty(natural_dice, obstacle)

            # build the context
            context = {
                "form": form,
                "rolls": rolls,
                "result": result,
                "open_ended": open_ended,
                "difficulty": assessed_difficulty,
                "shade": shade,
            }
            # store values in session for luck mechanic
            request.session["shade"] = shade
            request.session["obstacle"] = obstacle
            request.session["assessed_difficulty"] = assessed_difficulty
            request.session["last_roll"] = rolls
            request.session["form"] = form.cleaned_data

            return render(
                request, template_name="rolls/roll_dice.html", context=context
            )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RollForm()

    return render(request, "rolls/roll_dice.html", {"form": form})


def roll_luck(request):
    if request.method == "POST":
        # retrieve variables
        shade = request.session["shade"]
        obstacle = int(request.session["obstacle"])
        last_roll = request.session["last_roll"]
        assessed_difficulty = request.session["assessed_difficulty"]
        form_data = request.session["form"]
        form = RollForm(form_data)

        # call the roll function
        rolls, result = roll(
            shade=shade, obstacle=obstacle, luck=True, last_roll=last_roll
        )

        # create new context
        context = {
            "rolls": rolls,
            "result": result,
            "used_luck": True,
            "form": form,
            "shade": shade,
            "difficulty": assessed_difficulty,
        }
        return render(request, "rolls/roll_dice.html", context=context)


def assess_difficulty(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AssessDifficultyForm(request.POST)
        if form.is_valid():
            # retrieve the values from the form
            natural_dice = int(form.cleaned_data["natural_dice"])
            obstacle = int(form.cleaned_data["obstacle"])

            # assess the difficulty
            assessed_difficulty = difficulty(natural_dice, obstacle)

            # build the context
            context = {
                "form": form,
                "difficulty": assessed_difficulty,
            }

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AssessDifficultyForm()
        context = {"form": form}

    return render(request, "rolls/assess_difficulty.html", context=context)
