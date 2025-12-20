from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'dailies/home.html')

def dailiesMorningAffirmation(request):
    return render(request, 'dailies/dailies-morning-affirmation.html')

def dailiesMorningGoal(request):
    return render(request, 'dailies/dailies-morning-goal.html')

def dailiesMorningChecklist(request):
    return render(request, 'dailies/dailies-morning-checklist.html')

def dailiesEvening(request):
    return render(request, 'dailies/dailies-evening.html')

def dailiesStory(request):
    return render(request, "dailies/dailies-story.html")
