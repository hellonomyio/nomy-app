from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dailies/home.html')

def dailiesMorningAffirmation(request):
    return render(request, 'dailies/dailies-morning-affirmation.html')

def dailiesMorningGoal(request):
    return render(request, 'dailies/dailies-morning-goal.html')

def dailiesEvening(request):
    return render(request, 'dailies/dailies-evening.html')

def dailiesStory(request):
    return render(request, "dailies/dailies-story.html")
