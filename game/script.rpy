init python:
    class Person:
        def __init__(self, character, name, trust = 0):
            self.c = character
            self.name = name
            self.trust = trust

        def trust_ch(self, change):
            image = "heart_fill"
            self.trust += change
            if change > 0:
                direction = "increased"
            else:
                direction = "decreased"
                image = "heart_empty"
            renpy.notify("Romance with " + str(self.name) + " " + direction)
            renpy.show(image, [heart_pos])
            renpy.pause(2)
            renpy.hide(image)

transform heart_pos:
    xalign 0.01
    yalign 0.15

image heart_fill = "heart_fill.png"
image heart_empty = "heart_empty.png"
# boolean for Brennan Lee Mulligan route
boolean brennanRoute = False

# The game starts here.

label start:

    $ b = Person(Character("???"), "???")
    $ j = Person(Character("Jessica"), "Jessica")
    $ c = Person(Character("???"), "???")
    $ a = Person(Character("???"), "???")
    $ d = Person(Character("???"), "???")
    $ m = Person(Character("???"), "???")
    $ love_candidates = [b, c, a, d, m]

    scene blm office
    with dissolve

    "Hello? Hello! Can you hear me? Ah you’re awake."

    show brennan neutral
    with dissolve

    #add brennan lee mulligan intro song
    "A strange figure stands tall in front of you. The body odd, yet the face seems.. Familiar."

    b.c "Hello there!"

    $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan")

    j.c "B-Brennan lee mulligan?!?"

    show brennan blush

    b.c "Well.. My name is Headmaster Dean, but if you’d like, you can refer to me as Brennan Lee mulligan."

    show brennan neutral

    j.c "Wh… Why do you.. Look like that? Where am I?"

    "You look down"

    show brennan happy

    b.c "Oh! Well that is a lot of interesting questions all at once.
    You see, you are in purgatory. You humans have a very weak perception of the afterlife
    you know. Unlike your heaven and hell, some people are given second chances!
    Welcome to that place."

    b.c "Also, The reason I appear like this, is because
    I assume the figure of the person you trusted most in your past life.
    I assume for you that would be.. Brennan Lee Mulligan on a Kaonashi’s body…"

    j.c "O..Oh… Okay.. So I’m in hell."

    b.c "Ah well, no you are not, that… doesn’t exist."

default option1 = False
default option2 = False
menu:
    "Why do i look like this?":
        $ option1 = True
        jump soul

    "What do you mean purgatory? Why am I not in heaven? Or uhh…":
        $ option2 = True
        jump death


label soul:

    b.c "Similarly to how I become the person who you are the most comfortable with,
    You also assume a sprite. You resemble what your SOUL appears to be."

    b.c "You are… well… a monkey queen. Present in many different kinds of mythology.
    You’ll find some other mythological creatures, maybe some Satyrs, nymphs, what nots."
    if option1:
        menu:
            "What do you mean purgatory? Why am I not in heaven? Or uhh…":
                jump death
    else:
        jump exposition


label death:

    b.c "Well… you see, most people don’t like my answer to this.
    People who get sent to purgatory are… well they died the most pathetic deaths."
    j.c "I died a pathetic death?"
    b.c "Ah.. yes… quite so…"

    "The headmaster opens a drawer and looks through a file. He grimaces."

    b.c "Oh dear.."

    j.c "What is it?"

    b.c "Are you sure you want to know?"

    j.c "Yes?!? Obviously."

    "The headmaster takes a deep breath and looks closer."

    b.c "It appears that your… abundance of domesticated creatures, decided to take a nap on you. While you were suffocating, you began to scream, alas no one came to your aid because… they were too used to your screams.."

    "He slowly closes the file and you look down, ashamed."

    show brennan happy

    b.c "Glad to know you’ve earned your place. Welcome aboard!"

    show brennan neutral

    b.c "Oh yes! The bonfire. Let me explain"

    b.c "At the end of this week we have our bonfire.
    You see, the purpose of this realm is to rehabilitate those pathetic individuals,
    and reincarnate them back to earth.
    Yet, every single person is supposed to go back to earth with their soulmate…"

    b.c "Usually this is a romantic soulmate, but this school has been known
    to see the platonic soul mate or two. Anyways, When you discover who your soulmate is,"

    b.c "you have to help each other rehabilitate, so you are respawned at the exact same time.
    They will probably give you an item. Maybe a hair clip or something, if you throw it into the fire, and the fire changes colour,"

    show brennan blush

    b.c "voila. You’ve met your match."

    show brennan neutral
    #check to see if this option was chosen first, if yes, give user chance to choose the other option
    if option2:
        menu:
            "Why do i look like this?":
                jump soul
    else:
        jump exposition

label exposition:
    b.c "Alright so, I’m a very busy headmaster. I trust that you won’t get into trouble if you look around on your own.
    Class starts in a half hour, you best not be late!"

    'Trembling, you get up from the chair, still shaken up, you head towards the door and murmur a weak “alrighty then.”'

    play sound "audio/Door.mp3"
    scene hall
    with dissolve

    #add hallway music later

    play music "audio/ambient noise.mp3" fadeout 1.0 fadein 1.0

    j.c "How the hell am I supposed to know what class to go to? That creepy guy didn’t even give me a schedule…"
    "You realize, while you may be some… monkey beast… you are wearing a school uniform.
    Quickly, you check your pockets and pull out a slip of paper, somehow, it appears to be untouched,
    even though it was just shoved in your pocket.."

    j.c "Period 1… Math class. Second floor, all right."

    stop music

    scene staircase
    with dissolve

    "You locate the staircase, and start to walk up, but you see a panting figure."

    show cassidy neutral blink

    j.c "whoa! Are you okay?! You’re so out of breath! Is someone chasing you?"

    show cassidy mad
    play music "audio/cassidy theme.mp3" fadeout 1.0 fadein 1.0

    "The girl glares slightly at you."

    c.c "Yes, I’m fine. I just.. Have difficulty walking up stairs sometimes.
    Its normal this is a normal thing for people with normal bodies to do."

    menu:
        "Do you want some water?":
            show cassidy happy
            c.c " Thanks, but I'm not really a ‘water’ kind of girl. If you have any whisky I’ll take some. The name’s Cassidy."
            $ c = Person(Character("Cassidy"), "Cassidy")
            $ c.trust_ch(1)
            show cassidy happy blink
            "Unfortunately for the two of you, neither of you have any whisky on hand, but you feel content that you may have made your first friend."
            stop music
            jump library
        "It's… just a flight of stairs.. This shouldn’t be hard for you.":
            show cassidy mad
            c.c "Yes. It is just a flight of stairs. *grumbles* You are also just a bitch. Funny how things workout that way. My name is Cassidy, but I doubt we’ll see each other often."
            "Cassidy storms away, you fear you’ve made a bad choice."
            $ c = Person(Character("Cassidy"), "Cassidy")
            $ c.trust_ch(-1)
            stop music
            jump library

label library:
    "After an odd encounter with a wraith, you run up the stairs and look around for your math classroom.
    Nervous, you enter, and all of a sudden think; how the hell will math help with making me a better person?"
    play sound "audio/Door.mp3"

    scene hall
    with dissolve

    "Class goes by fast, but let’s be honest. You weren’t really listening. You decide to head over to the library, which took you a really long time to find."

    scene library
    with fade
    play sound "audio/Door.mp3"

    "You start looking around, but your attention is quickly averted to the large sobbing man sitting
    alone among a pile of math sheets and textbooks."

    "You look away, not wanting to make him uncomfortable, but his sobs and whimpers fill the library, and you feel obligated to help."
    play music "audio/argha theme.mp3" fadeout 1.0 fadein 1.0
    show argha mad

    a.c "FUCK! 9 x 4??? Since when did we go back to X meaning you times it! Oh god why is that little two so small and so close to the 3? Aw fuck.."

    "You slide into the seat across from the crying creature and he looks up, wiping snot from his nose."

    show argha sad blink

    a.c "hNnhn… are you *sniff*… the tutor? Bro you’re like.. Thirty two minutes late.. You were supposed to be here at 1:00…"

    j.c "Um, well, no I’m not your tutor, and its 1:13 so it has definitely not been thirty two minutes…"

    menu:
        "Can I help you?":
            show argha blush
            a.c "Really? You can?! Aw yeah! Thank you! Arghawan’s the name, and Charming ladies is the game."
            "Arghawan winks at you and you blush."
            $ a = Person(Character("Arghawan"), "Arghawan")
            j.c "Ah ahem.. Uh yes so, let's take a look at this first problem. Oh easy, first question so what is 9 x 12?"
            $ answer1 = renpy.input("Enter an answer: ", "", allow="0123456789")
            if int(answer1) == 108:
                show argha happy
                a.c "All right! Thanks! Now, what’s next… oh, hey, do you know how to find the value of the numerator of cos A, if the value of tan A is 4/3?"
                "You gulp."
                j.c "What the hell? This went from 0-100 way too fast."
                $ answer2 = renpy.input("Enter an answer: ", "", allow="0123456789")
                if int(answer2) == 3:
                    show argha happy blink
                    a.c "Awesome! Wow bro, you really are the best!"
                    "He checks the time."
                    $ a.trust_ch(1)
                    jump gym
                else:
                    a.c "Bro… this doesn’t look right.. Damn and I have a test today..this better be right and my judgement is failing me! Or we’re both in deep shit.."
                    show argha sad
                    a.c "Not to be rude, but i think you should seriously reevaluate your dream of being an educator."
                    "You look frazzled."
                    j.c "When did I ever say-"
                    $ a = Person(Character("Arghawan"), "Arghawan")
                    $ a.trust_ch(-1)
                    jump gym

            else:
                show argha sad
                a.c "Are you sure about that? I may be dumb, but I know at least that much…"
                $ a = Person(Character("Arghawan"), "Arghawan")

                jump gym

            "Well, I hope your tutor comes in soon.":
                "You grimace at the mathwork. You do NOT want to remember horrible memories from when you were alive. You try to make up an excuse, until all of a sudden Arghawan shoots up from his seat."
                $ a = Person(Character("Arghawan"), "Arghawan")

                jump gym
label gym:
    a.c "Oh shit homie! I gotta run! Class is almost starting. I’ll catch you tomorrow!"
    "Arghawan interrupts you, then runs off to his next class. You check your schedule and see what class to head to next."
    stop music
    j.c "UGH are you fucking kidding me?! Gym? Again, what does any of this have to do with rehabilitation?"

    play sound "audio/Door.mp3"
    scene hall
    with dissolve

    "You leave the library and head towards the gym class. Along the way you take a good look at all the strange yet very attractive people around.. How were you supposed to just choose one? Maybe one of the people you’d already met…"

    scene gym
    with dissolve
    m.c "HEY YOU"

    play music "audio/maggie theme.mp3" fadeout 1.0 fadein 1.0

    "You sharply turn around to see someone pointing their hand at you.
    All of a sudden you realize you’ve changed, entered the gym glass, and started playing a game of dodgeball."

    "Somehow you have survived an entire game of dodgeball until it was just you and some other person across the room from you."
    #make maggie angry
    show maggie happy
    m.c "I DOUBT YOU’RE A WORTHY OPPONENT, BE PREPARED TO FEEL MY WRATH"

    "She whips a dodgeball towards you, hurling towards your face. Quickly you duck. Holy shit this chick is crazy."

    m.c "WHATS WRONG? TOO CHICKEN TO THROW THE BALL?"

    "You decide between winning the game or just letting her have it. Maybe its a chance for you to make some friends."

    menu:
        "Throw the game and let her have the victory":
            show maggie sad
            $ m.trust_ch(-1)
            "You decide letting her win is the quickest way to becoming friends.
            You weakly throw a ball, and she catches it. The coach yells something along the lines of
            ‘Get the hell out and hit the showers’ but the girl catches you as you leave."
            hide maggie sad
            m.c "HEY! You!"
            "You stop"
            m.c "You let me win the game huh? Not cool. I don’t need your handout, jackass. My name is Maggie, but I don’t encourage you to talk to me again if you’re as much of a coward as you seem."
            $ m = Person(Character("Maggie"), "Maggie")
            "Maggie coldly shoves the ball back into your hands and it hits your stomach. She walks into the girls change room."
            jump cafeteria
        "Win the game fair and square.":
            "You assume this is the kind of person who likes a fight.
            So a fight you’ll give her. Back and forth, like it’s more intense than just trying to slap someone with a ball,
            the game goes on, but eventually you reign victorious."
            hide maggie happy
            "You leave to go change, but you hear a voice call after you."
            show maggie neutral
            m.c "HEY!"
            "you stop in your tracks."
            m.c ".. Good game out there. Glad to see you aren’t a pussy like the rest of these chumps."

            "The girl who you know now to be a tiefling jerks her head at a bunch of kids to freak them out."

            show maggie happy

            m.c " My name is Maggie, and rest assured, next time, I’ll win."
            $ m = Person(Character("Maggie"), "Maggie")
            $ m.trust_ch(1)
            "she pats you on the back. Rough. A little too rough.
            So rough in fact that when you try to feign sportsmanship the inside you feel nothing but a burning pain.
            Holy shit why did that hurt so much."

label cafeteria:
    "After an afternoon of terrible, terrible classes, you decide to grab a bite to eat in the cafeteria,
    but by the time you reach the cafeteria, all of the tables are taken.
    You groan and take your three dollar sandwich elsewhere."

    scene outside

    play music "audio/ambient noise.mp3" fadeout 1.0 fadein 1.0

    "Scanning the area to make sure no one sees you eat alone like a loser, you meander your way over to a bench. Plopping yourself down, you unwrap your sandwich and take a bite."

    j.c "God.. This sucks"

    "You settle the sandwich on your lap and look at it in disgust. All of a sudden, a bird sits down right in front of you."

    "You rip off a small piece of bread and throw it onto the floor for it to eat."

    j.c "There you go buddy... I hope you don’t have… taste buds."

    "You watch the bird as it gobbles up the sandwich, when all of a sudden, you hear a squeal."

    d.c "Holy shit! Holy shit holy shit!"
    show doris neutral

    play music "audio/doris theme.mp3" fadeout 1.0 fadein 1.0

    "You stare at the stranger in amazement, as to how she was comfortable with yelling next to a stranger."

    d.c "That’s an Opal-Tit Boobyfoot! It’s so rare in these parts!"

    "Her eyes twinkle in amazement as she examines the species. She pulls out a pad of paper and a pencil to quickly sketch a picture."

    "Eventually the sandwich is done and the bird flies away. Doris gets up off the ground and smiles in amazement at her picture."

    j.c "You draw?"

    d.c "Oh! Yes! So sorry this must be strange for you. My name is Doris, I’m a fungal nymph! Oh would you like to see the picture?"
    $ d = Person(Character("Doris"), "Doris")
    "Doris flips around her sketchpad to show you a sketching of the bird, alongside a flattering image of you sitting on the bench. For a second, you forgot you were a monkey-person."

    menu:
        "That’s … kind of creepy":
            show doris sad
            d.c "Oh… I’m sorry then.. um … I guess I’ll get going then.."
            show doris sad blink
            $ d.trust_ch(-1)
            "You see small tears well up in her eyes, but before you can stop her, she’s run away to God knows where, doing God knows what."
            jump dormchoice
        "That looks incredible!":
            d.c "..."
            show doris blush
            d.c "th.. Thank you. Well you know, these birds are only attracted to beautiful things…"
            show doris blush blink
            $ d.trust_ch(1)
            show doris neutral
            d.c "OH! Like umm… ahh.. That pretty bracelet you have right there! Ahh what is that? Silver?"
            "Doris’ quick change in demeanor gave you whiplash as you coughed and looked down on your wrist."
            j.c "Um actually I think its some sort of bone-"
            "but by the time you look back up to respond to Doris’ question, she’s gone drawing pictures of some other creature."
            jump dormchoice
label dormchoice:
    stop music
    "You sigh and pack up, going to your dorm as classes have finished after lunchtime."
    scene dorm
    with fade

    "Uncharacteristically, You decide to go to bed early, and reflect on your day. You feel that you’ve connected the most with…"

    menu:
        "Cassidy":
            "Cassidy may have been cold and slightly off putting, but something about her icy presence felt so warm"
            $ c.trust_ch(1)
            jump day1
        "Arghawan":
            "Arghawan seems like the classic heartbreaker, but something about him is just so magnetic.. It’s probably the muscles, no yeah, it’s at least 47 percent the muscles."
            $ a.trust_ch(1)
            jump day1
        "Maggie":
            "Maggie is nothing short of fiery and aggressive, but something about her just makes you want to get to know her better."
            $ m.trust_ch(1)
            jump day1
        "Doris":
            "Doris is the classic nerd, shy and antsy, but you can’t help but want to hear her go on for hours about her discoveries that day."
            $ d.trust_ch(1)
            jump day1
        "Brennan lee mulligan....":
            "What about that Brennan Lee Mulligan guy... "
            $ b.trust_ch(1)
            jump day1

label day1:
    "Satisfied with your decision for the night, you lay your head down against the cool hatsune miku pillow and close your heavy eyes. Tomorrow is going to be crazy…"
    #will this work?
    scene dorm
    with fade
    #where day 1 actually begins
    "You wake up refreshed and get ready for school, but find you still have some time before the first class starts.
    You figure you have enough time to either get breakfast at the cafeteria or explore the school, but not both."
    menu:
        "Get food at the cafeteria":
            "You decide that you are hungry and could go for some hashbrowns."
            jump cafday1
        "Explore the school":
            "You decide to find out more about this place you have ended up in."
            jump blmstart

label cafday1:
    scene lunchroom
    with fade
    "You are busy eating your hashbrowns when you spot a familiar face outside in the courtyard. Arghawan!
    You hear the bell ring, summoning you to class, but you also notice he looks distraught.
    He seems to be running about. Perhaps he's looking for something?"
    #idk if this will work, but i want to see if I can edit the narration slightly depending on how much characters trust Jess
    #let me know if this is a bad idea, Sarv.
    if a.trust >= 0:
        "You decide to go investigate, because knowing Arghawan, they will probably need help. Either way, you have no doubt you'll be entertained."
    else:
        "You decide to go investigate, because perhaps Arghawan will have done something stupid and funny."
    scene outside
    with fade

    a.c "Help! Has anyone seen my $5? $10 reward!"
    a.c "You! From yesterday! Could you please help me look for my $5? I need it for lunch!"
    a.c "Even though I have been offering a $10 reward, I have had no luck so far."

    menu:
        "Decide to help Arghawan.":
            j.c "Here, perhaps I can help you. Let's look for it together!"
            $ a.trust_ch(1)

    Jessica has the choice to either help him, laugh at him, or lend him $5
    “Let’s look for it together.” +1 AFFECTION
    Jessica doesn’t end up finding the $5, but lends Chad $5
    Chad feels financially indebted towards Jessica
    “That’s pretty funny.” -1 AFFECTION
    CHAD ROBS YOU AND TAKES $5 FROM YOU /J
    Guilts you into giving him money


    ONLY IF SHE SELECTED TO HELP:After resolving the issue of $5, Chad asks her what she thinks he should have for breakfast. According to him, this is the best reward he can offer.
    “Pizza” -1 AFFECTION
    “Hamburgers” +1 AFFECTION
    “How did you know that was my favourite food?!”






    # This ends the game.
    return
