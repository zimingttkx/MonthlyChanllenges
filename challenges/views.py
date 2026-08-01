from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.template.base import FILTER_ARGUMENT_SEPARATOR
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
    "december": None,
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly__challenge_by_str(request, month):
    try:
        challenge_test = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"challenge_test": challenge_test,
                                                             "month_name": month})
    except KeyError:
        raise Http404()


def monthly__challenge_by_number(request,  month):
    if month < 1 or month > 12:
        return HttpResponseNotFound("<h1>This is not a valid month</h1>")

    month_names = list(monthly_challenges.keys())
    forward_month = month_names[month - 1]
    return HttpResponse(monthly_challenges[forward_month])

