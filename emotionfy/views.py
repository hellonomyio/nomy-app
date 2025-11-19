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
    "anxiety": "energised",
    "frustration": "energised",

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
    "curiosity": [
        {
            "sub": "Curiosity is one of the brightest emotions in autistic experience. It’s the spark that draws focus so tightly that the rest of the world fades away. When curiosity lights up, it can feel like being pulled forward by invisible thread, the need to understand, to connect the pieces, to know. It’s both mental and physical."
        },
        {
            "sub": "Curiosity for autistic adults often has depth rather than breadth. It’s more “I want to understand this completely.” than “I want to know a little about everything”. That deep-focus which is sometimes dismissed as fixation, is actually a powerful form of sustained curiosity. What some researchers call monotropism (Murray, Lesser & Lawson, 2005). It’s an attentional pattern that allows profound discovery but can make transitions feel jarring."
        },
        {
            "sub": "Many autistic people describe curiosity as comfort. Like a place where the world finally makes sense, predictable and full of patterns. It’s exploration even if it feels to others like escapism. When curiosity is safe, it’s self-regulation. When it’s interrupted, it can turn into distress.",
            "note": "Reflect"
        },
    ],

    "happiness": [
        {
            "sub": "When masking has been part of life for a long time, it’s easy to wonder if happiness is something you really feel or to minimise it because it doesn’t look the way the world tells you it should. But your version of happiness has always been there. It’s steady, subtle, and deeply personal. It doesn’t have to be loud or shared to be real.",
            "note": "How it Shows Up"
        },
        {
            "sub": "For many autistic adults, happiness doesn’t show up as big smiles or bursts of energy. It’s often quiet. It lives in those small, grounding moments when the body feels calm, the mind feels clear and the world finally feels safe to exist in. It’s when everything inside says, this feels right. <br>Sometimes happiness looks like gentle stimming, humming softly, or being deeply focused on something that feels good. Many autistic people describe it as a sense of alignment—when body, mind and environment are working together instead of against each other.",
            "note": "Reflect"
        },
        {
            "sub": "Happiness often comes from experiences that create comfort, safety, or meaning:<br><br><b>Special interests</b> that bring deep focus and satisfaction.<br><b>Predictable routines</b> that offer stability and peace.<br><b>Sensory comfort</b> from sound, light, touch, or movement.<br><b>Quiet time alone</b> to recharge and feel grounded.<br><b>Authentic connection</b> with people who accept and understand you.<br><b>Self-expression</b> through movement, creativity, or work that feels purposeful.",
            "note": "It Affects"
        },
        {
            "sub": "When happiness is present, the nervous system begins to settle. Breathing slows. Muscles release. The body shifts from protection into calm.<br><br>This is regulation for autistic people. These moments allow the body to recover from masking, stress and sensory overload. Even brief moments of happiness like listening to a comforting sound, engaging in a favourite routine, or sitting in a space that feels right, can be deeply restorative.",
            "note": "Reflect"
        }
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
            "sub": "Amusement, for many autistic adults doesn’t always look the way others expect it to. Laughter might not come easily or it might burst out suddenly, surprising even you. Sometimes humour lands in patterns or details other people don’t notice like the rhythm of words, the absurd logic of a situation, the unexpected predictability of something breaking the same way every time. Your sense of humour might be literal, dry, dark, or rooted in pattern recognition not sarcasm or social teasing but the delight of a mental puzzle snapping together. There’s also the kind of amusement that comes from seeing the world’s oddness clearly."
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
    "stupidity": [
        {
            "sub": "The feeling of stupidity is one of the most painful emotional states many autistic adults describe, definitely not because it’s true but because it’s actually learned. It often grows from years of misunderstanding, when your way of processing didn’t match what teachers, peers or workplaces expected. Maybe you knew the answer but couldn’t get it out fast enough. Maybe you asked for clarification and were told it was obvious. Over time, those moments stack up until they whisper, “You’re stupid.” But here’s the truth: the feeling of stupidity is evidence of mismatch rather than failure. Autistic cognition often works in deep, nonlinear ways. You might need time to translate thoughts into speech, or your mind might explore ten possible meanings before choosing one. To others, that delay looks like not knowing. Inside, it’s precision."
        },
        {
            "sub": "That lingering sense of inadequacy can make you hesitate to speak up, to ask questions or to show what you actually know. It can also show up as anger or withdrawal because you’re tired of being misread. Many autistic adults find that this feeling softens once they begin to understand their brain’s rhythm, the way it thinks in layers, patterns or sensory associations rather than in straight lines. Intelligence here isn’t broken, it’s different architecture."
        },
        {
            "sub": "Research supports this too: autistic adults often show strong abilities in systemising, memory, and pattern recognition (Baron-Cohen et al., 2009), even when social processing feels like a foreign language. So the feeling of stupidity isn’t about ability, it’s about living in an environment that grades communication speed over depth.",
            "note": "Reflect"
        },
    ],
    "confusion": [
        {
            "sub": "Confusion can feel like everything familiar still exists but it’s suddenly harder to make sense of what’s around you. For some autistic people, confusion is about knowing too many possible meanings all at once. The brain tries to make sense of every detail, every tone, every possibility competing to be the right one.  It can show up in ways like someone gives you a vague instruction like “just do what feels right” and you paude because what feels right? and to whom? or maybe a conversation shifts tone halfway through and everyone else seems to keep up except you."
        },
        {
            "sub": "It also runs deeper. Many autistic people describe a more painful kind. The confusion of people. The moments when someone reacts sharply or grows distant or looks uncomfortable and you’re left trying to piece together what happened. You replay the conversation again and again: Did I say something wrong? Did I miss a cue? Did they misunderstand me? Over time this social confusion can build layers of self doubt and even shame because the rules seem to change without warming and you can’t keep up."
        },
        {
            "sub": "After a late diagnosis, you might find yourself revisitng years of memories and wondering ‘Was that actually my fault? or was I overwhelmed misunderstood or masking too hard?’. This kindof reflection can be both clarifying and disorienting. It means you’re finally seeing your story clearly but from a new perspective.",
            "note": "Reflect"
        },
    ],
    "loneliness": [
        {
            "sub": "Loneliness in the autistic experience is more about the feeling of being surrounded by people yet unseen and less about being physically alone. It’s the ache of existing in a world that speaks a language just a bit different from yours. You might crave connection deeply but find that most social spaces feel like they cost too much to enter. For many autistic adults, loneliness begins early when your way of communicating, or your sensory needs didn’t match the people around you. Over time, you might have learned to keep parts of yourself hidden to stay safe, only to realise that the safety came with silence. That silence is heavy; it’s a loneliness of self."
        },
        {
            "sub": "And yet, autistic loneliness is rarely total. There are moments of belonging with another neurodivergent person, a trusted friend or even a comforting routine that reflects you back to yourself. Many autistic people find that connection happens best through shared focus rather than forced conversation. Through parallel play, mutual interests or simply being side by side without pressure. Research on autistic well-being (Botha & Frost, 2020) highlights how belonging and validation, being accepted as is, are what actually dissolve loneliness. It’s less about having more people and more about being allowed to exist without translation."
        },
        {
            "sub": "You are not alone in your aloneness. The loneliness itself is proof of your capacity for connection. You feel it because you want to belong. And that desire is something profoundly human, profoundly whole.",
            "note": "Reflect"
        },
    ],
    "embarrassment": [
        {
            "sub": "Embarrassment can feel like a sudden flush that takes over your body before your brain catches up. For autistic adults, it often hits harder and not necessarily because of sensitivity but because social mistakes happen in an environment full of invisible rules. You might not even know what you did “wrong” until you see someone’s reaction and by then, the feeling is already burning. It can feel like a deep body-sense of exposure like heat, confusion and shame tangled together. Many autistic people describe embarrassment as “too much feeling all at once.” You might laugh awkwardly, go quiet or mask harder to hide it. Sometimes you replay the moment for hours or days, trying to find the logic in what happened."
        },
        {
            "sub": "What often hurts isn’t the mistake itself but the disconnection, the moment you realise others saw something you didn’t mean to show. Remember: embarrassment is part of being human and for autistic people, it’s amplified by unpredictability and the effort of constant self-monitoring. Research on social camouflaging (Hull et al., 2017) shows that repeated social misalignments can create long-term self-consciousness, where even small social slips trigger old survival reflexes. The key is gentleness. When embarrassment hits, remind yourself that this moment doesn’t define you and that it’s simply your nervous system remembering old lessons about safety.",
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

    "exhaustion": [
        {
            "sub": "Exhaustion in the autistic body feels like a depletion that seeps into thought, movement and even language. It’s waking up already spent because simply existing, processing light, sound, expectations and unspoken social rules takes more from you than most people realise. This exhaustion often builds silently. Masking drains energy, but so does translating trying to make yourself understood, trying to read a room, trying to be easy to be around. Over time, your body begins to run on borrowed energy and when it runs out, you crash. The brain and body have been in constant overdrive, filtering input and emotion without rest."
        },
        {
            "sub": "When you reach that point, you might feel foggy, detached or unable to do even simple things. Words might vanish. Small decisions feel like cliffs. That’s autistic burnout, a full-body shutdown born from long-term overwhelm (Raymaker et al., 2020). “Pushing through” as a way of recovery is ineffective. Give yourself permission to rest, to reduce demands and to let silence and sameness heal you. The way you may need to rest can sometimes feel like indulgence but remind yourself that it’s a necessary to recharge. And when you give yourself that, your system begins to trust that it doesn’t always have to fight.",
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
            "sub": "Frustration is the feeling that happens when something gets in the way of what’s needed or wanted. It’s that sense of being blocked or stuck. Everyone feels it, but for autistic people, it can be stronger and more intense because of how the brain and nervous system process information and emotion. Frustration is the body and brain’s way of saying, “Something isn’t working right now, and support is needed.”",
            "note": "How it shows up"
        },
        {
            "sub": "Frustration can show up in many ways: <br><br><b>The body might feel tight, hot or restless.<br> The mind may feel foggy, fast or overwhelmed.<br> Words might stumble, or come out louder or sharper than intended.<br> Movement might increase, pacing, clenching fists, rocking, or flapping.</b><br><br> These are all ways the nervous system tries to release built-up energy.",
            "note": "Common Triggers"
        },
        {
            "sub": "Frustration often builds when there are barriers that make daily life harder to manage, such as:<br><br> <b>Communication difficulties</b> – knowing what to say but not being able to express it.<br><b>Executive function challenges</b> – trouble starting, organisng, or finishing tasks.<br><b>Sensory overload</b> – too much noise, light, movement, or touch.<br><b>Changes in routine</b> – unexpected shifts or uncertainty.<br><b>Social misunderstandings</b> – being misread, interrupted, or dismissed.<br><b>Feeling unsupported</b> – not being given the time, space, or understanding needed.<br><br>These experiences can pile up and when they do, frustration can quickly turn into overwhelm.",
            "note": "It Affects"
        },
        {
            "sub": "For autistic people, frustration is an emotion and a physical state. The nervous system moves into stress mode to prepare to protect itself. This can make it hard to think clearly, use words, or stay calm. When this stress keeps building, it can lead to: Meltdowns, where the body releases energy through crying, yelling, or movement. Shutdowns, where the body and mind pull inward to recover. Both are natural responses to overload and neither failures nor overreactions. They are signs that the body and mind have reached their limit and need care.",
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
