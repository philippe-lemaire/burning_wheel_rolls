from django.http import HttpResponse


def roll_dice(request):
    return HttpResponse("Hello, do you want to roll dice?")


def assess_difficulty(request):
    return HttpResponse("Hello, do you want to assess difficulty?")
