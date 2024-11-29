from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthly_challenges = {
    "January": "Start a daily journaling habit.",
    "February": "Practice gratitude by writing down three things you're thankful for every day.",
    "March": "Complete a 30-day fitness challenge.",
    "April": "Spend 30 minutes learning a new skill each day.",
    "May": "Declutter one area of your home each week.",
    "June": "Try cooking a new recipe every weekend.",
    "July": "Spend at least 15 minutes outdoors every day.",
    "August": "Read one book during the month.",
    "September": "Limit your screen time to two hours daily outside of work.",
    "October": "Commit to a daily mindfulness or meditation practice.",
    "November": "Practice random acts of kindness weekly.",
    "December": "Reflect on the year and set achievable goals for the next year."
}


def monthly_challenge_by_number(request,month):
    try:
        month_keys = list(monthly_challenges.keys())
        challenge = month_keys[month-1] 
        redirect_path = reverse("month-challenge",args=[challenge])
        print(redirect_path)
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("no challenge is found!")

def monthly_challenge(request,month):
    try:
        challenge = monthly_challenges[month.capitalize()]
        response_data = f"<h1>{challenge}</h1>"

        return HttpResponse(response_data)
    except:
      link = 'http://127.0.0.1:8000/challenges'
      text = "<ul>"
      for i in list(monthly_challenges.keys()):
          text+=f"<li><a href='{link}/{i}'>{i}</a></li>"
      text+="</ul>"
      return HttpResponseNotFound(text)