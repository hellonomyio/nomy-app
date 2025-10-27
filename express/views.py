from django.shortcuts import render
from django.utils.text import slugify

# -------------------------------
# Base pages
# -------------------------------

def home(request):
    return render(request, "express/home.html")

def expressIntro(request):
    return render(request, "express/express-intro.html")

def expressSpeak(request):
    return render(request, "express/express-speak.html")


# -------------------------------
# Scenario data
# -------------------------------

SCENARIOS = {
    "social-event": {
        "prompt": "Someone invites you to a social event you don’t want to attend",
        "options": [
            {"label": "Be honest with myself", "type": "direct"},
            {"label": "Be kind to others", "type": "relational"},
        ],
    },
    "interrupted": {
        "prompt": "Your colleague interrupts you during a meeting",
        "options": [
            {"label": "Say it simply", "type": "direct"},
            {"label": "Say it gently", "type": "relational"},
        ],
    },
    "unclear-instructions": {
        "prompt": "You need clearer instructions at work",
        "options": [
            {"label": "Ask directly", "type": "direct"},
            {"label": "Ask collaboratively", "type": "relational"},
        ],
    },
}


# -------------------------------
# Response data
# -------------------------------

RESPONSES = {
    "social-event": {
        "direct": "Thanks for the invite but I’m not up for a group event right now.",
        "relational": "I really appreciate the invite but I’ve had a full week and need some quiet time.",
    },
    "interrupted": {
        "direct": "Please let me finish my point, then I’ll listen to yours.",
        "relational": "I have a few more thoughts I’d like to finish before I lose them — can I share those first?",
    },
    "unclear-instructions": {
        "direct": "Could you clarify what’s expected for this task?",
        "relational": "I just want to make sure I’ve understood your request correctly — could you clarify what’s needed?",
    },
}


# -------------------------------
# Views
# -------------------------------

def expressScenario(request):
    """Display the chosen scenario and its two tone options."""
    situation = request.GET.get("situation", "social-event")
    slug = slugify(situation)
    scenario = SCENARIOS.get(slug)

    # Fallback if not found
    if not scenario:
        slug, scenario = "social-event", SCENARIOS["social-event"]

    print("DEBUG expressScenario:", slug)

    context = {
        "slug": slug,
        "prompt": scenario["prompt"],
        "options": scenario["options"],
    }
    return render(request, "express/express-scenario.html", context)

def expressResponse(request):
    """Display the selected response (direct / relational)."""
    situation = request.GET.get("situation")
    tone = request.GET.get("tone")  # direct or relational

    print("DEBUG expressResponse:", situation, tone)

    # Get matching response text
    data = RESPONSES.get(situation, {})
    response_text = data.get(tone)

    if not response_text:
        response_text = "No response available for this combination."

    context = {
        "tone": tone,
        "response": response_text,
        "situation": situation,
    }

    # 👇 Go to your new Express intro page instead
    return render(request, "express/express-intro.html", context)
