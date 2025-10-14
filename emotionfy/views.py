from django.shortcuts import render
from django.utils.text import slugify

# Create your views here.
def home(request):
    return render(request, 'emotionize/home.html')

def emotionizeAll(request):
    return render(request, 'emotionize/emotionize-all.html')

SLIDES = {
    "excitement": [
        {
            "sub":  "Excitement can feel volcanic. Like energy flooding every corner of your body at once. It’s that rush when an idea clicks, a plan forms or something beloved appears unexpectedly. For autistic adults, excitement can be exhilarating but also overwhelming. The nervous system doesn’t always separate joy energy from stress energy so excitement can tip into overload if there’s no room for release.",
            "note": "read more"
        },
        {
            "sub": "Some autistic people stim more intensely when excited: jumping, flapping, pacing or speaking fast, with words tumbling over each other. Others go quiet, flooded by the intensity of it. Both are normal. Both are ways the body translates emotional current into motion.",
            "note": "read more"
        },
        {
            "sub": "Excitement might also bring mixed feelings like pride tangled with anxiety, joy mixed with exhaustion. That’s because the body is processing something big. Allow it. The goal isn’t to dampen excitement but to channel it safely and to let it live in your body without it burning through.",
            "note": "read more"
        },
        {
            "sub": "Research on autistic affect regulation shows that high arousal emotions, even positive ones, can trigger overwhelm when sensory thresholds are already stretched (Kinnaird et al., 2019). That doesn’t make excitement bad, it means your body feels joy deeply. It’s an intensity that deserves space, not shame.",
            "note": "read more"
        },
    ],
    "anxiety": [
        {
            "sub":  "Anxiety can be one of the most constant companions in autistic life and not because you worry too much but because the world is unpredictable in ways your body can’t ignore. Bright lights, unexpected sounds, social ambiguity, shifting plans. Each of these can trigger the same alarm system that neurotypical people might only feel during real danger. Sometimes your mind can’t explain why it’s happening but your body already knows.",
            "note": "read more"
        },
        {
            "sub":  "You might notice your stomach tightening, your jaw locking, your shoulders lifting towards your ears. Your thoughts race or they disappear altogether. It’s important for you to know that that’s not weakness. That’s the nervous system doing its best to protect you. Many autistic adults learn to live in a near-constant state of alertness, so when you finally start to feel safe, it can be disorienting. The calm almost feels wrong. Give yourself permission to listen to the early signals: restlessness, breath shortening or a need to escape. Those are cues for care, not shame.",
            "note": "read more"
        },
    ],
    "numbness": [
        { "sub":"Numbness can feel like nothing and that’s what makes it so hard to recognise. For autistic adults, numbness often follows sensory or emotional overload, when the system shuts down to protect itself. It’s the mind going offline so the body can recover. You might describe it as emptiness, flatness, or just not caring but beneath that blankness is exhaustion, not absence.", "note": "read more"},
        { "sub":"Sometimes numbness comes after too much masking, too much feeling, too much explaining. It’s what happens when emotion fatigue sets in. When your system has had to regulate so long that it simply stops producing signals. That can feel frightening if you’ve just begun reconnecting with your emotions after diagnosis: “Why can’t I feel anything?” But numbness is a feeling and it could be your nervous system saying, “I need quiet.", "note": "read more"},
    ],
    "relief": [
        {"sub": "Relief often feels like collapse. A sudden melting after tension. It’s the moment your body finally stops bracing. You might sigh, cry or go quiet. That’s your nervous system exhaling after holding itself too tightly. Many autistic adults describe feeling drained right after relief and it’s normal. Your body needs time to process that it’s safe again. Let yourself rest in it. Don’t rush to “bounce back.” Think of relief as recovery data. It tells you what was too much and what safety feels like again. We’ll map signals in body, thoughts and emotions.", "note": "read more"}, 
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

def emotionizeStory(request):
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
    return render(request, "emotionize/emotionize-story.html", ctx)