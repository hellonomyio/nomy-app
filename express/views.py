from django.shortcuts import render, redirect
from openai import OpenAI
client = OpenAI()

from django.utils.text import slugify


# -------------------------------
# Base pages
# -------------------------------

def home(request):
    return render(request, "express/home.html")

def expressIntro(request):
    return render(request, "express/express-intro.html")

def expressSpeak(request):
    response_text = request.GET.get("response", "")
    return render(request, "express/express-speak.html", {"response": response_text})

def expressText(request):
    response_text = request.GET.get("response", "")
    return render(request, "express/express-text.html", {"response": response_text})

# -------------------------------
# Scenario data
# -------------------------------

SCENARIOS = {
    "social-event": {
        "prompt": "Someone invites you to a social event you don’t want to attend",
        "style": "boundary-setting",
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
    "text-over-call": {
        "prompt": "You're explaining why you prefer text over calls",
        "options": [
            {"label": "Be honest with myself", "type": "direct"},
            {"label": "Reach out gently", "type": "relational"},
        ],
    },
    "group-setting": {
        "prompt": "You’re in a group and can’t get a word in",
        "options": [
            {"label": "Be honest with myself", "type": "direct"},
            {"label": "Reach out gently", "type": "relational"},
        ],
    },
}

STYLE_INFO = {
    "boundary-setting": {
        "label": "Setting Boundaries",
        "description": "Used when you need to protect your time, energy, or comfort.",
    },
    "assert-turn-taking": {
        "label": "Holding Your Turn",
        "description": "Used when someone interrupts or talks over you.",
    },
    "clarify-info": {
        "label": "Requesting Clarity",
        "description": "Used when instructions or expectations aren't clear.",
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
    "text-over-call": {
        "direct": "I find calls stressful. I prefer texting.",
        "relational": "Texting helps me focus and express myself clearly. I appreciate when people are understanding of that.",
    },
    "group-setting": {
        "direct": "I’d like to share something too.",
        "relational": "I want to share something that connects with what you said. Can I go next?",
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

    return render(request, "express/express-intro.html", context)

def expressCustom(request):
    if request.method != "POST":
        return redirect("express:intro")

    user_scenario = request.POST.get("scenario", "").strip()

    if not user_scenario:
        return render(request, "express/custom-error.html", {
            "error": "Please enter a situation."
        })

    # --- GPT QUERY ---
    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",  # use GPT-5 later when available
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You help late-diagnosed autistic adults express themselves "
                        "in difficult or unclear social moments. "
                        "Give a response that is short (1–2 sentences), emotionally validating, "
                        "and direct but gentle. Avoid shame, masking, or overly formal tone."
                    )
                },
                {
                    "role": "user",
                    "content": f"Scenario: {user_scenario}\nProvide a gentle/directional response I could say."
                }
            ]
        )

        ai_response = completion.choices[0].message.content.strip()

    except Exception as e:
        return render(request, "express/custom-error.html", {"error": str(e)})

    # --- RENDER THE RESPONSE PAGE ---
    return render(request, "express/custom-response.html", {
        "user_scenario": user_scenario,
        "response": ai_response,
    })

def createScenarioPage(request):
    return render(request, "express/create-scenario.html")
