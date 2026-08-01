from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
monthly_challenges = {
    "january": "Running for 20 minutes",
    "february": "Learning English for 30 minutes",
    "march": "Doing homework for 40 minutes",
    "april": "Doing housework for 70 minutes",
    "may": "Doing homework for 20 minutes",
    "june": "Learning English for 21 minutes",
    "july": "Learning English for 22 minutes",
    "august": "Learning English for 24 minutes",
    "september": "Learning English for 26 minutes",
    "october": "Learning English for 27 minutes",
    "november": "Learning English for 29 minutes",
    "december": "Learning English for 88 minutes",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse('b', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly__challenge_by_str(request, month):
    try:
        challenge_test = monthly_challenges[month]
        return render("challenges/challenge.html")
    except KeyError:
        return HttpResponseNotFound("<h1>This month dose not exist</h1>")


def monthly__challenge_by_number(request,  month):
    if month < 1 or month > 12:
        return HttpResponseNotFound("<h1>This is not a valid month</h1>")

    month_names = list(monthly_challenges.keys())
    forward_month = month_names[month - 1]
    return HttpResponse(monthly_challenges[forward_month])

