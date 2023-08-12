from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "January": "Build a simple web server",
    "February": "Write a Python script to automate a daily task",
    "March": "Learn a new programming language",
    "April": "Contribute to an open-source project",
    "May": "Write a technical blog post",
    "June": "Create a CI/CD pipeline for a small project",
    "July": "Read a technical book",
    "August": "Optimize a piece of code for efficiency",
    "September": "Work with a new DevOps tool",
    "October": "Complete a coding challenge online",
    "November": "Mentor or teach a coding skill to someone else",
    "December": "Explore a new area of technology or methodology",
}
def index(request):
    list_items = ""
    months =list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months,
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect (redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
