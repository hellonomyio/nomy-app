from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie  # NEW

PROMPT_THRESHOLD = 3

@ensure_csrf_cookie  # NEW: sets the CSRF cookie on GET /
def home(request):
    if not request.session.session_key:
        request.session.save()

    count = int(request.session.get("explore_count", 0))
    dismissed = bool(request.session.get("signup_prompt_dismissed", False))

    show_signup_prompt = (
        (not request.user.is_authenticated)
        and (count >= PROMPT_THRESHOLD)
        and (not dismissed)
    )

    request.session["explore_count"] = count + 1
    return render(request, "core/home.html", {"show_signup_prompt": show_signup_prompt})

@require_POST
def dismiss_signup_prompt(request):
    request.session["signup_prompt_dismissed"] = True
    request.session["explore_count"] = 0
    return JsonResponse({"ok": True})
