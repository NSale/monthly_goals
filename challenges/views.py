import logging
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

logger = logging.getLogger(__name__)

responses = {
    "january": "Eat no meat for an entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read a book for at least 20 minutes every day!",
    "may": "Do at least 50 pushups every day!",
    "june": "Install Pihole on RPI!",
    "july": "Have a vacation!",
    "august": "Watch a Formula 1 race in Hungaroring",
    "setpember": "Play basketball every day!",
    "october": "Play squash every day!",
    "november": "Go to the Stara Planina for state holiday!",
    "december": None,
}


# Create your views here.
def index(request):
    return render(request, "challenges/index.html", {
        "months": list(responses.keys())
    })


def monthly_challenge(request, month):
    try:
        return render(request, "challenges/challenge.html", {
            "text": responses[month],
            "month": month,
        })
    except Exception as e:
        logger.error('something went wrong!', e)
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(responses.keys())
    try:
        return HttpResponseRedirect(reverse("month_challenge", args=[months[int(month) - 1]]))
    except Exception as e:
        logger.error('something went wrong!', e)
        raise Http404()
