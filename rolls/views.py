from django.http import HttpResponse
from django.shortcuts import render


def roll_dice(request):
    return render(request, template_name="rolls/roll_dice.html")


def assess_difficulty(request):
    return HttpResponse("Hello, do you want to assess difficulty?")
