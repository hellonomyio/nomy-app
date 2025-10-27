from django.shortcuts import render
from django.utils.text import slugify

# Create your views here.
def home(request):
    return render(request, 'emotionize/home.html')

def emotionizeIntro(request):
    return render(request, "emotionize/emotionize-intro.html")

def emotionizeAll(request):
    return render(request, 'emotionize/emotionize-all.html')

def emotionizeEnergised(request):
    return render(request, 'emotionize/emotionize-energised.html')

def emotionizePleasant(request):
    return render(request, 'emotionize/emotionize-pleasant.html')

def emotionizeLowEnergy(request):
    return render(request, 'emotionize/emotionize-low-energy.html')

def emotionizeVulnerable(request):
    return render(request, 'emotionize/emotionize-vulnerable.html')

EMOTION_CATEGORIES = {
    # Energised group
    "excitement": "energised",
    "curiosity": "energised",

    # Pleasant group
    "relief": "pleasant",
    "happiness": "pleasant",
    "amusement": "pleasant",
    "contentment": "pleasant",

    # Low-Energy group
    "exhaustion": "low-energy",
    "numbness": "low-energy",
    "sadness": "low-energy",
    "overwhelm": "low-energy",
    "uncertainty": "low-energy",

    # Vulnerable group
    "shame": "vulnerable",
    "embarrassment": "vulnerable",
    "loneliness": "vulnerable",
    "confusion": "vulnerable",
    "stupidity": "vulnerable",
}

SLIDES = {
    "excitement": [
        {
            "sub": "Excitement can feel volcanic. Like energy flooding every corner of your body at once. It’s that rush when an idea clicks, a plan forms or something beloved appears unexpectedly. For autistic adults, excitement can be exhilarating but also overwhelming. The nervous system doesn’t always separate joy energy from stress energy so excitement can tip into overload if there’s no room for release."
        },
        {
            "sub": "Some autistic people stim more intensely when excited: jumping, flapping, pacing or speaking fast, with words tumbling over each other. Others go quiet, flooded by the intensity of it. Both are normal. Both are ways the body translates emotional current into motion."
        },
        {
            "sub": "Excitement might also bring mixed feelings like pride tangled with anxiety, joy mixed with exhaustion. That’s because the body is processing something big. Allow it. The goal isn’t to dampen excitement but to channel it safely and to let it live in your body without it burning through."
        },
        {
            "sub": "Research on autistic affect regulation shows that high arousal emotions, even positive ones, can trigger overwhelm when sensory thresholds are already stretched (Kinnaird et al., 2019). That doesn’t make excitement bad, it means your body feels joy deeply. It’s an intensity that deserves space, not shame.",
            "note": "Reflect"
        },
    ],

    "happiness": [
        {
            "sub": "Amusement, for many autistic adults doesn’t always look the way others expect it to. Laughter might not come easily or it might burst out suddenly, surprising even you. Sometimes humour lands in patterns or details other people don’t notice like the rhythm of words, the absurd logic of a situation, the unexpected predictability of something breaking the same way every time. Your sense of humour might be literal, dry, dark, or rooted in pattern recognition not sarcasm or social teasing but the delight of a mental puzzle snapping together. There’s also the kind of amusement that comes from seeing the world’s oddness clearly."
        },
        {
            "sub": "Happiness for many autistic adults doesn’t always look like the typical smiling, laughing or social excitement you’ve been told it should. It often lives in moments of quiet rightness when the sensory world finally fits, when a rhythm clicks, when you’re immersed in something that fascinates you. For you, happiness might feel like breathing evenly for the first time all day or noticing a steady warmth in your chest. Maybe it’s when you’re alone but deeply content, doing something that brings focus and peace rather than noise and energy.",
            "note": "Reflect"
        },
    ],
    "contentment": [
        {
            "sub": "Contentment often looks subtle. It can look like a stillness that doesn’t demand attention. It’s when everything around you aligns just enough that your body lets its guard down. For some autistic adults, contentment comes in solitude, familiar environments or repetitive, soothing activities. It’s the quiet hum of safety, where you can finally stop anticipating the next unpredictable thing."
        },
        {
            "sub": "If you’ve spent years surviving in environments that didn’t match your sensory needs, this calm can feel almost sacred. Protect it. Identify what brings it, the lighting, the background sound, the time of day and recreate it deliberately. Calmness could be evidence of regulation and something your nervous system has been craving.",
            "note": "Reflect"
        },
    ],
    "amusement": [
        {
            "sub": "If you’ve spent years masking, you may have learned to question whether you even feel happiness at all or to downplay it because it didn’t match what others expected. But your version of happiness has always been there, subtle, steady and deeply personal. It doesn’t have to be shared to be real. You might stim gently, hum or let yourself sit in calm focus. That’s joy too. Many autistic adults describe this kind of happiness as “alignment”, which is the rare and wonderful moment when your body and the world agree."
        },
        {
            "sub": "Some autistic adults share that humour is one of the safest emotional outlets, where your unique way of seeing becomes joy. Research on autistic humour shows that while it may differ in social style, it’s equally complex and emotionally rich, often built on incongruity and pattern recognition rather than social play (Samson & Hegenloh, 2010). So if your laughter comes out sideways, delayed, or just in your head, it’s still laughter. You’re experiencing something you find joyful and funny.",
            "note": "Reflect"
        },
    ],

    "anxiety": [
        {
            "sub": "Anxiety can be one of the most constant companions in autistic life and not because you worry too much but because the world is unpredictable in ways your body can’t ignore. Bright lights, unexpected sounds, social ambiguity, shifting plans. Each of these can trigger the same alarm system that neurotypical people might only feel during real danger. Sometimes your mind can’t explain why it’s happening but your body already knows."
        },
        {
            "sub": "You might notice your stomach tightening, your jaw locking, your shoulders lifting towards your ears. Your thoughts race or they disappear altogether. It’s important for you to know that that’s not weakness. That’s the nervous system doing its best to protect you. Many autistic adults learn to live in a near-constant state of alertness, so when you finally start to feel safe, it can be disorienting. The calm almost feels wrong. Give yourself permission to listen to the early signals: restlessness, breath shortening or a need to escape. Those are cues for care, not shame.",
            "note": "Reflect"
        },
    ],

    "exhaustion": [
        {
            "sub": "Exhaustion in the autistic body feels like a depletion that seeps into thought, movement and even language. It’s waking up already spent because simply existing, processing light, sound, expectations and unspoken social rules takes more from you than most people realise. This exhaustion often builds silently. Masking drains energy, but so does translating trying to make yourself understood, trying to read a room, trying to be easy to be around. Over time, your body begins to run on borrowed energy and when it runs out, you crash. The brain and body have been in constant overdrive, filtering input and emotion without rest."
        },
        {
            "sub": "When you reach that point, you might feel foggy, detached or unable to do even simple things. Words might vanish. Small decisions feel like cliffs. That’s autistic burnout, a full-body shutdown born from long-term overwhelm (Raymaker et al., 2020). “Pushing through” as a way of recovery is ineffective. Give yourself permission to rest, to reduce demands and to let silence and sameness heal you. The way you may need to rest can sometimes feel like indulgence but remind yourself that it’s a necessary to recharge. And when you give yourself that, your system begins to trust that it doesn’t always have to fight.",
            "note": "Reflect"
        },
    ],

    "shame": [
        {
            "sub": "Shame can linger long after the original moment passes. Many autistic adults carry deep layers of it from being told again and again that their natural behaviours were wrong. You might have learned early to mask, to perform what others expected and now you carry the quiet ache of “I’m too much” or “I’m not enough.” That’s not shame you created. It was given to you."
        },
        {
            "sub": "Relearning emotion means gently peeling that weight away. When you notice shame, pause before apologising. Ask yourself: Is this guilt for something I did, or shame for who I am? Most times, it’s the latter, a conditioned reflex from survival. The truth is, your traits were never moral flaws. They were adaptations to a world that demanded sameness.",
            "note": "Reflect"
        },
    ],
    "sadness": [
        {
            "sub": "For you, sadness might not always arrive as tears or emotional expression. It can creep in disguised as fatigue, silence or retreat. Because alexithymia, the difficulty identifying internal states, is common in autism. Sadness can live in your body before you have words for it. You might feel heavy or blank, like the colour has drained from things you usually care about."
        },
        {
            "sub": "Other people might not recognise it. They might see you go quiet and think you’re distant or detached. But inside, sadness can be thick and consuming. It’s not that you don’t feel, it’s that your feelings sometimes move through pathways that don’t translate neatly into visible emotion. It’s okay to let sadness exist without explaining it immediately. Sometimes it helps just to name it later, once you notice: “That was sadness.” Over time, you’ll start to spot its footprints and the moments when your body slows down, or when you want to curl inward.",
            "note": "Reflect"
        },
    ],

    "uncertainty": [
        {
            "sub": "Uncertainty can feel like standing between two doors, both open but neither safe. For many autistic adults, uncertainty is a real source of distress. The brain craves predictability; it feels safer when it knows what to expect, what rules apply, and how to prepare. When that stability breaks or when plans change suddenly or when someone’s words mean different things depending on tone, uncertainty can trigger full-body unease."
        },
        {   
            "sub": "You might feel it in your stomach first or in your skin like a buzzing tension that won’t settle until something becomes clear. Some people describe it as being “on high alert for what’s about to happen.” That’s your nervous system’s way of protecting you from unpredictability. Many autistic adults live in a world that demands constant adaptation, which means uncertainty is everywhere. You might mask harder, over-prepare or replay conversations to fill the gaps of not knowing. That’s survival strategy."
        },
        {
            "sub": "Other people might not recognise it. They might see you go quiet and think you’re distant or detached. But inside, sadness can be thick and consuming. It’s not that you don’t feel, it’s that your feelings sometimes move through pathways that don’t translate neatly into visible emotion. It’s okay to let sadness exist without explaining it immediately. Sometimes it helps just to name it later, once you notice: “That was sadness.” Over time, you’ll start to spot its footprints and the moments when your body slows down, or when you want to curl inward.",
            "note": "Reflect"
        },
    ],

    "numbness": [
        {
            "sub": "Numbness can feel like nothing and that’s what makes it so hard to recognise. For autistic adults, numbness often follows sensory or emotional overload, when the system shuts down to protect itself. It’s the mind going offline so the body can recover. You might describe it as emptiness, flatness, or just not caring but beneath that blankness is exhaustion, not absence."
        },
        {
            "sub": "Sometimes numbness comes after too much masking, too much feeling, too much explaining. It’s what happens when emotion fatigue sets in. When your system has had to regulate so long that it simply stops producing signals. That can feel frightening if you’ve just begun reconnecting with your emotions after diagnosis: “Why can’t I feel anything?” But numbness is a feeling and it could be your nervous system saying, “I need quiet.”",
            "note": "Reflect"
        },
    ],

    "relief": [
        {
            "sub": "Relief often feels like collapse. A sudden melting after tension. It’s the moment your body finally stops bracing. You might sigh, cry or go quiet. That’s your nervous system exhaling after holding itself too tightly. Many autistic adults describe feeling drained right after relief and it’s normal. Your body needs time to process that it’s safe again. Let yourself rest in it. Don’t rush to “bounce back.” Think of relief as recovery data. It tells you what was too much and what safety feels like again. We’ll map signals in body, thoughts and emotions.",
            "note": "Reflect"
        },
    ],

    "overwhelm": [
        {
            "sub": "Overwhelm happens when too much is coming at you at once - sensations, thoughts, or emotions that feel hard to process all together. For many autistic people, it can build up from bright lights, noise, expectations or rapid changes."
        },
        {
            "lead": "Your body might give early signals - tension, zoning out, or the need to withdraw."
        },
        {
            "lead": "What helps you come back to balance?",
            "note": "Reflect"
        }
    ],

    "frustration": [
        {
            "sub": "Frustration hits hard when you can see what you mean but can’t get it across. It’s feeling stuck and the pain of being misunderstood. For autistic adults, this is a common emotional flashpoint because communication gaps or executive function barriers can make even simple interactions feel like mazes."
        },
        {
            "sub": "When frustration builds, your words may trip, your tone may sharpen or your body might need to move, pacing, clenching, flapping. It can feel like aggression but it’s more that energy trying to escape. The key is to catch the block before it explodes: pause and label it “I’m frustrated because my words aren’t working right now.” Naming the block can loosen its grip.",
            "note": "Reflect"
        }
    ]
}


def emotionizeStory(request):
    slug = slugify(request.GET.get("emotion", "anxiety"))
    slides = SLIDES.get(slug)
    if not slides:
        slug, slides = "anxiety", SLIDES["anxiety"]

    # Determine category (fallback to low-energy if unknown)
    category = EMOTION_CATEGORIES.get(slug, "low-energy")

    ctx = {
        "emotion": slug,             # e.g. "anxiety"
        "title": slug.capitalize(),  # "Anxiety"
        "slides": slides,            # content
        "category": category,        # e.g. "low-energy"
        "category_url_name": f"emotionfy:{category}",  # ✅ add this line
    }
    return render(request, "emotionize/emotionize-story.html", ctx)
