from django.shortcuts import render
from django.utils.text import slugify

# Create your views here.
def home(request):
    return render(request, 'emotionfy/home.html')

def emotionfyAll(request):
    return render(request, 'emotionfy/emotionfy-all.html')

SLIDES = {
    "anxiety": [
        {
            "lead": "Anxiety can appear in many different ways and for autistic people it often feels like tension, restlessness or overload.",
            "sub":  "Here, you’ll notice how anxiety shows up in your body, thoughts and emotions."
        },
        {
            "lead": "When you learn your personal signals, you can start recognising anxiety earlier and responding with care instead of confusion.",
            "sub":  "Anxiety often grows from moments of unpredictability or sensory strain.",
            "note": "Explore situations that activate your nervous system. <strong class='callout'>Sudden changes, unclear expectations, overwhelming environments</strong> are common."
        },
        {
            "lead": "What tends to trigger it for <em>you</em>?",
            "note": "Think of places, tasks or social moments that raise your alertness. No judgment — we’re mapping patterns so you can care for yourself sooner."
        },
    ],
    "shame": [
        {"lead": "Shame can make you want to hide or shrink, even when you did nothing wrong.", "sub":"We’ll map signals in body, thoughts and emotions."},
        {"lead": "Shame often shows up after social misunderstandings or harsh self-talk.", "note":"Notice themes without blaming yourself."},
        {"lead": "Where does shame pop up most for you?", "note":"What helps you feel seen and safe again?"}
    ],
    "overwhelm": [
        {
            "lead": "Overwhelm happens when too much is coming at you at once - sensations, thoughts, or emotions that feel hard to process all together.",
            "sub": "For many autistic people, it can build up from bright lights, noise, expectations or rapid changes."
        },
        {
            "lead": "Your body might give early signals - tension, zoning out, or the need to withdraw.",
            "note": "Paying attention to these cues helps you step back <strong class='callout'>before</strong> your system overloads."
        },
        {
            "lead": "What helps you come back to balance?",
            "note": "You might notice that quiet spaces, deep pressure, or gentle movement help your nervous system recover."
        }
    ],
    "frustration": [
        {
            "lead": "Frustration often appears when things don’t go as expected, communication feels blocked, or your needs aren’t understood.",
            "sub": "It’s a natural signal that something important to you isn’t working right now."
        },
        {
            "lead": "For autistic people, frustration can rise from unclear instructions, sensory discomfort, or slow systems.",
            "note": "Notice what parts of those moments are in your control — and which aren’t. <strong class='callout'>Self-compassion</strong> turns frustration into information, not shame."
        },
        {
            "lead": "How does frustration show up for you?",
            "note": "Recognising it early lets you pause, adjust or ask for support before it builds into anger or shutdown."
        }
    ]
}

def emotionStory(request):
    slug = slugify(request.GET.get("emotion", "anxiety"))
    slides = SLIDES.get(slug)
    if not slides:
        # fallback to a safe default
        slug, slides = "anxiety", SLIDES["anxiety"]
    ctx = {
        "emotion": slug,            # e.g., "anxiety"
        "title": slug.capitalize(), # page title/heading use
        "slides": slides,           # list of dicts for template loop
    }
    return render(request, "emotionfy/emotionfy-story.html", ctx)