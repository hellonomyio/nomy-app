from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import EmotionReflection, ExpressReflection
import datetime, json

@login_required
def save_express(request):
    data = json.loads(request.body)
    ExpressReflection.objects.create(
        user=request.user,
        date=datetime.date.today(),
        text=data["text"]
    )
    return JsonResponse({"saved": True})

@login_required
def save_emotion(request):
    data = json.loads(request.body)
    EmotionReflection.objects.create(
        user=request.user,
        date=datetime.date.today(),
        emotion=data["emotion"],
        text=data["text"]
    )
    return JsonResponse({"saved": True})

@login_required
def get_emotion_reflections(request):
    items = EmotionReflection.objects.filter(user=request.user).order_by("-date")
    data = []
    for i in items:
        data.append({
            "date": i.date.strftime("%d/%m/%Y"),
            "emotion": i.emotion,
            "reflection": i.text
        })
    return JsonResponse(data, safe=False)