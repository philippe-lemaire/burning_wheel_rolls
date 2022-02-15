from django.urls import path

from . import views

app_name = "rolls"

urlpatterns = [
    path("roll_dice/", views.roll_dice, name="roll_dice"),
    path("assess_difficulty/", views.roll_dice, name="assess_difficulty"),
]
