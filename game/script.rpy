init python:
    # boolean for Brennan Lee Mulligan route
    boolean brennanRoute = False

    #boolean about whether Jess chose to do some of Maggie's assignments
    boolean maggieRoute = False

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

# The game starts here.

label start:

    $ b = Person(Character("???"), "???")
    $ j = Person(Character("Jessica"), "Jessica")
    $ c = Person(Character("???"), "???")
    $ a = Person(Character("???"), "???")
    $ d = Person(Character("???"), "???")
    $ m = Person(Character("???"), "???")
    $ love_candidates = [b, c, a, d, m]

    scene bg blmoffice
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

    'Trembling, you get up from the chair, still shaken up, you head towards the door and murmur a weak \"alrighty then.\"'

    play sound "audio/Door.mp3"
    scene bg hall
    with dissolve

    #add hallway music later

    play music "audio/ambient noise.mp3" fadeout 1.0 fadein 1.0

    j.c "How the hell am I supposed to know what class to go to? That creepy guy didn’t even give me a schedule…"
    "You realize, while you may be some… monkey beast… you are wearing a school uniform.
    Quickly, you check your pockets and pull out a slip of paper, somehow, it appears to be untouched,
    even though it was just shoved in your pocket.."

    j.c "Period 1… Math class. Second floor, all right."

    stop music

    scene bg staircase
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
            c.c "Thanks, but I'm not really a ‘water’ kind of girl. If you have any whisky I’ll take some. The name’s Cassidy."
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

    scene bg hall
    with dissolve

    "Class goes by fast, but let’s be honest. You weren’t really listening. You decide to head over to the library, which took you a really long time to find."

    scene bg library
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
    scene bg hall
    with dissolve

    "You leave the library and head towards the gym class. Along the way you take a good look at all the strange yet very attractive people around.. How were you supposed to just choose one? Maybe one of the people you’d already met…"

    scene bg gym
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
            hide maggie
            "Maggie coldly shoves the ball back into your hands and it hits your stomach. She walks into the girls change room."
            jump cafeteria
        #changed it to "play" from "win" here... I feel there is no guarantee that you will win agaionst a new foe
        "Play the game fair and square.":
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

            m.c "My name is Maggie, and rest assured, next time, I’ll win."
            $ m = Person(Character("Maggie"), "Maggie")
            $ m.trust_ch(1)
            "She pats you on the back. Rough. A little too rough.
            So rough in fact that when you try to feign sportsmanship the inside you feel nothing but a burning pain.
            Holy shit why did that hurt so much."
            #sarv you forgot to jump to the cafeteria here... was this intentional?
            jump cafeteria

label cafeteria:
    "After an afternoon of terrible, terrible classes, you decide to grab a bite to eat in the cafeteria,
    but by the time you reach the cafeteria, all of the tables are taken.
    You groan and take your three dollar sandwich elsewhere."

    scene bg outside

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

    d.c "Oh! Yes! So sorry this must be strange for you. My name is Doris, I’m a fungal nymph! Would you like to see the picture?"
    $ d = Person(Character("Doris"), "Doris")
    "Doris flips around her sketchpad to show you a sketching of the bird, alongside a flattering image of you sitting on the bench. For a second, you forgot you were a monkey-person."

    menu:
        "That’s … kind of creepy":
            show doris sad
            d.c "Oh… I’m sorry then.. um … I guess I’ll get going then.."
            show doris sad blink
            $ d.trust_ch(-1)
            hide doris
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
            hide doris
            "but by the time you look back up to respond to Doris’ question, she’s gone drawing pictures of some other creature."
            jump dormchoice
label dormchoice:
    stop music
    "You sigh and pack up, going to your dorm as classes have finished after lunchtime."
    scene bg dorm
    with fade

    "Uncharacteristically, You decide to go to bed early, and reflect on your day. You feel that you’ve connected the most with…"

    menu:
        "Cassidy":
            "Cassidy may have been cold and slightly off putting, but something about her icy presence felt so warm."
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
    scene bg dorm
    with fade
    #where day 1 actually begins
    "You wake up in your dorm, only slightly ready to begin a new day. The day prior had knocked you out well.
    Reluctantly, you get out of your cozy bed, looking around your room for the textbooks needed for your class today. When you’re all prepared, you leave the room, hoping to run into some of the new friends you’ve made."

    scene bg hall
    with fade
    "As you walk down the halls, your stomach growls, reminding you that you have to eat something before you properly begin the day, but there’s also so much of the school you haven’t seen yet… what should you do?"

    menu:
        "Go to the Cafeteria for some food":
            jump breakfastday1
        "Explore the school":
            jump blmstart

label breakfastday1:
    "Your stomach growls again, urging you to eat something. You give in, heading towards the Cafeteria and ready to eat some hashbrowns, when you find someone familiar scurrying around the halls."
    scene bg lunchroom
    with fade
    #music?
    show argha sad
    a.c "Helloooooo? Mr. 5 dollar bill? Where are you?"
    "You see Arghawan on all floors crawling around wailing for his lost bill, as if it’s going to come flying back at the sound of his voice."
    j.c "Arghawan, what are you doing?""
    "Arghawan lights up at the sight of you. He puts on a flirtatious charm and winks at you. Or is that just how he regularly looks?"
    show argha happy
    a.c "Oh, Jemica!"
    j.c "Actually, it’s Jess-"
    "He stops you dead in your tracks and grabs you by the shoulders.
    a.c "Thank God you’re here, bro!"
    show argha sad
    a.c "Dude, I’ve been looking for my 5 dollar bill all morning… Have you seen it?"
    j.c "...Can’t say that I have."
    a.c "Yeah, neither has anyone else in the school. It’s kinda sus…"

    menu:
        "Let’s look for it together.":
            jump arghabrekkie
        "You’re kind of a scatterbrain, huh?":
            show argha neutral
            $a.trust_ch(-1)
            a.c "Aw man.. That sucks… Oh well, math class starts now anyways. You should get going."
            hide argha
            jump mathday1

label arghabrekkie:
    .trust_ch(1)
    show argha happy
    a.c "Seriously!? Thank you so much!"
    "And so, the two of you walk around the school, looking for Arghawan’s missing $5 bill. However..."
    show argha mad
    a.c "Man, are you serious?! We looked everywhere! It’s totally gone."
    show argha mad blink
    a.c "Someone stole it, I bet."
    "Arghawan sighs in frustration, and almost as if in sync, your stomachs both growled. You looked at eachother sheepishly..."
    show argha blush
    a.c "Sorry… I’m pretty hungry."
    "You sigh heavily"
    j.c "Me too…"
    j.c "C’mon, let’s just go to the cafeteria and get some grub."
    show argha sad
    a.c "B-But, I’m penniless!"
    "You smile and flash him a wink, trying to match his energy. You decide the best way to be friends is to buy his love.""
    j.c "No worries, I got you covered."
    show argha blush
    a.c "Woah, dude… You’re awesome."
    "He gushes. Man! This motherfucker cute!"
    "The two of you walk back to the cafeteria, making small, casual conversation with each other.
    show argha neutral
    a.c "Hm, what should I have for breakfast today?"
    "He eyes a menu with two options, though you can't see what they are at this distance.
    You take a closer look at what he was eyeing. Pizza and… Subway? What the hell?"
    j.c "What about… eggs? You know, something people actually eat for breakfast?"
    "Arghawan shrugs."
    show argha neutral
    a.c "I can’t eat eggs, they make me feel queasy… I’m also not really much of a breakfast person."
    j.c "Well, I guess you can go with…"

    menu:
        "...pizza.":
            $ a.trust_ch(-1)
            show argha neutral
            a.c "Meh, I don’t really feel like it. I’m just gonna go for a sub instead."
            jump day1brekkie

        "...subway":
            $ a.trust_ch(1)
            show argha happy
            a.c "Totally! It’s such a Subway kind of day."
            jump day1brekkie


label day1brekkie:
    "The two of you buy a lot of food. Like, too much, but after you purchase enough food for a small army, you sit at a grimy cafeteria table.
    show argha neutral
    "Arghawan takes a bite out of his sub and lets out a guttural moan and rolls his eyes. It makes you kind of uncomfortable.
    a.c "Dude, I can’t thank you enough for saving my ass like that. I totally owe you one."
    "You look at the dashing, ginger man."
    j.c "Anyone would have done the same for you, you’re that kind of kid, ya know? Easy for people to like you. Got the whole school wrapped around your horn."
    show argha sad blink
    a.c "Not really…"
    show argha sad
    a.c "I mean, you can say that I’m popular and I have a lot of friends but… I’m not close to anyone. Nobody would do what you’ve done for me. Everyone *loves* me, but nobody *likes* me."
    "Instantly your heart flutters with empathy and you have the sudden urge to reach out to him, but you stop yourself and look down."
    j.c "Well, I like you! Wait,"
    show argha happy
    j.c "I mean, not like that. I like you but I don’t LIKE like you.. Like I like you as a friend, even more than that!""
    "You realize what you just said."
    j.c "AGhhhh I mean like a good friend! Like a really good friend. Am I coming across clear or hahahah…"
    "You nervously laugh and shakily grab ahold of the drink on your table, chugging it to calm yourself down."
    show argha happy blink
    "Arghawan chuckles."
    show argha sad
    a.c "Awee so you’re saying you don’t like me?""
    "Arghawan teases as he pouts and feigns sadness, acting like a shot puppy. You blush heavily and fold your hands in your lap, looking down to trying to hide your beet red face. *Was he always this intense?*"
    j.c "You know what I mean, asshole."
    "Your face cracks into a crooked smile and you look to the side."
    show argha blush
    a.c "You’re blushing! Aww, what’s wrong? Monkey got your tongue?""
    "Quickly, Arghawan shoots his head to the left to check the clock mounted on the wall.
    a.c "Oh shit! Class is starting!"
    hide argha
    "Arghawan shoves the rest of the sub into his mouth, and runs off, but before he is out of eyeshot, he sends you a playful wink. You sit there, dumbfounded."
    j.c "Oh SHIT!"
    jump mathday1

label blmstart:
    scene bg hall
    with fade
    "You walk around the halls of the school. They’re quiet around this time, as most students are still asleep, or eating breakfast in the caf."
    "You see a figure hovering quickly down the hallway. It’s muttering something but then stops when it sees you."
    b.c "Oh Jessica! Hello there! How is everything?"
    j.c "Oh, things are… okay I guess. I’m having a hard time adjusting I think."
    show brennan sad
    b.c "I’m so sorry to hear that. You know, the quickest way to be accustomed to a new environment is to familiarize yourself with the inhabitants. Is there anyone here you feel close to?"

    menu:
        "Maggie":
            $ m.trust_ch(1)
            show blm happy
            b.c "Oh I’m glad to hear that! Well keep working towards your rehabilitation. The next bonfire is coming up soon! Who knows, maybe you’ll be ready by then."
            jump blmstartend
        "Cassidy":
            $ c.trust_ch(1)
            show blm happy
            b.c "Oh I’m glad to hear that! Well keep working towards your rehabilitation. The next bonfire is coming up soon! Who knows, maybe you’ll be ready by then."
            jump blmstartend
        "Arghawan":
            $ a.trust_ch(1)
            show blm happy
            b.c "Oh I’m glad to hear that! Well keep working towards your rehabilitation. The next bonfire is coming up soon! Who knows, maybe you’ll be ready by then."
            jump blmstartend
        "Doris":
            $ d.trust_ch(1)
            show blm happy
            b.c "Oh I’m glad to hear that! Well keep working towards your rehabilitation. The next bonfire is coming up soon! Who knows, maybe you’ll be ready by then."
            jump blmstartend
        "No one in particular.":
            jump blmstart2

label blmstart2:
    $ b.trust_ch(1)
    $ brennanRoute = True
    show brennan sad blink
    b.c "I’m so sorry to hear that Jessica."
    "The headmaster sighs."
    show brennan sad
    b.c "If you ever feel lonely during lunch, feel free to pay my office a visit. While I don’t recommend it because you will lose valuable time with your peers, I wouldn’t want you to feel unwelcome."
    "Strangely excited for this new offer, you smile and gladly accept."
    j.c "Oh! Thank you so much! That’s really kind of you."
    show brennan blush
    b.c "Just my duties as headteacher!"
    jump blmstartend

label blmstartend
    show brennan neutral
    b.c "Oh would you look at that! It’s 8:29. I must be getting back to my duties."
    hide brennan
    "Brennan Lee Mulligan resumes back to his hyperspeed hovering across the hallway, and you watch him fly off.
    Your eyes widen at the realization of the time."
    j.c "Oh shit! I gotta get the fuck outta here!"
    jump mathday1

label mathday1:
    "Picking yourself up, you dash to your math class. You arrive and sit down."
    scene bg classroom
    with fade
    "It was, as always, the most boring shit ever, but at least you got to vibe with Arghawan a bit.
    Next class was english. You realize that your schedule has changed a bit. Courses were rearranged and you no longer had gym, rather english, and you had biology towards the end of the day.
    You hurry yourself out of class and say bye to Arghawan. He shoots you a wink. Cocky bastard."

    #doing this again lolol
    scene bg classroom
    with fade
    Classroom
    Class_sounds.mp3

    "From afar you can see who else but Maggie furiously jots down notes and mumbles under her breath.

    Maggie_mad

    Maggie: "Ray Bradbury…. Sexist piece of shit why don’t you suck my-"

    "You interrupt her before she can go any further, afraid she may implode.

    j.c Heya Maggie, what are you reading?

    Maggie_happy

    "She looks up and her expression softens a bit. She shows you the cover cover of the book and groans.

    Maggie: Possibly the worst novel one of these white guys have ever written. Its called Fahrenheit 451.

    "You nod slowly in agreeance, more curious as to why she is reading the book if she hates it so much.

    j.c So why are you reading it if you hate it so much?

    "She looks around for the teacher and leans in. A small bit too close for your liking.

    Maggie: You see, I have this… extremely lucrative business. Some of these assholes really want to get out of this whole… purgatory joint. So they pay me to do their work for them. Of course, they owe me. It can be money… favours…. Anything.

    "Maggie laughs heartily.
    Maggie_happy_blink

    Maggie: And what these stupid bastards don’t even realize, is that the universe KNOWS I’m doing it for them! It’s not helping them one bit… so every bonfire they come crawling back, begging for me to do more!

    "You stare blankly for a bit, realizing why she was still sitting in purgatory, tired, but working away.

    j.c You don’t… want to leave?

    "She freezes for a second.

    Maggie: Nah, not for a while. I’m kinda comfy here, ya know? They make this place too nice for us. A lot of people just end up staying for a really long time.

    menu:
    Can I help you out with some of that?
    Can you do one for me?

    1.
     Maggie_happy

    UNLOCK MAGGIE ROUTE

    Maggie: That would be awesome! I really fucking suck at math, so I could really use your help on this one.

    "Jesus fucking christ how did you get stuck doing MORE MATH?!"

    j.c Oh.. Math. Fun.

    Maggie_happy_blink

    Maggie: Glad you think so! You can bring it to my room at night so I can give it to those stupid assholes tomorrow morning.

    X:She grumbles.

    Maggie-angry

    Maggie: Maybe they’ll finally pay me this time.

    "Maggie hands you a sheet of paper, a name poorly scribbled at the top read ARGHAWAN. You sigh and smile to yourself as you shove the paper into your bag to do later tonight.

    Maggie-neutral

    j.c You seem tired, though, are you getting enough sleep?

    Maggie_sad_blink

    "Maggie sighs and continues to read. Jotting down notes as she goes along.

    Maggie_sad

    Maggie: I mean do I need much sleep? It’s not like I can die here anyways.

    "Maggie mumbles.

    "You furrow your brows, frustrated at her deflection towards your concern.

    j.c We both know that's not the point of this place, it’s to become a better person.

    "Maggie seems to be a bit more frustrated than before.

    Maggie: I didn’t ask for your therapy or your concern. Take your interrogation to someone who’s more desperate for attention, like Arghawan.

    "Taken aback by her comment, and slightly offended on Arghawan’s behalf, you mutter a \"fine\" and sit back into the chair, ignoring her for the rest of the class.

    "Peeking at her once, you see her face muddled with guilt. Your expression softens too, yet you sit in each other’s silence. It's not unpleasant.

    2.
    m.trust_ch(-1)

    Maggie: Are you an actual idiot? Didn’t I just explain to you what happens to those dumbasses when they ask me for help?

    "Your face heats up in embarrassment as you feel the hammer of judgement BONK you on the head.

    Maggie: Out of respect for you, and for my fine establishment, absolutely the fuck not.

    "Hey, at least she respects you.



    "Class ends and hoards of students head down towards the cafeteria to grab a bite to eat.

    Lunchroom
    Cafeteria_noises.mp3

    "Who do you want to sit with?

    Maggie, sitting alone like a normal person.
    Doris, sitting on the windowsill like a housecat.
    Arghawan, sitting next to heaps of people with a single empty seat next to him.
    Cassidy, who isn’t actually sitting, but seems to be lying down on the dirty floor and moaning in pain, wailing "my back, my back."

    1.
    m.trust_ch(1)
    Maggie_neutral
    "You sit with Maggie. The awkwardness from class seems to have melt, and you share smalltalk about the class while she does some work.

    2.
    d.trust_ch(1)
    Doris blush blink
    "Doris isn’t much for talking, but the two of you enjoy sitting together, bathing in the warm orange sun permeating through the window.

    3.
    a.trust_ch(1)
    Arghawan happy
    "Sitting next to Arghawan and his group of friends is almost too loud and exciting. Bonus points, because he put his arm around you."

    4.
    c.trust_ch(1)
    cassidy_happy_blink
    "You lie on the floor next to Cassidy and offer to give her one of your life-changing massages. It’s kind of weird, and a bit pointless, since she’s cursed with a bad back, but she appreciates the effort.



    Hallway

    "You finish off the rest of your classes with nothing interesting happening in any of them. You head towards you dorm to rest, when you run into Cassidy and Doris arguing.

    D: Cassidy, you have to eat vegetables! To get big and strong! You can’t just be eating dino nuggies for the rest of eternity, can you?

    C: I can, and honestly neither of us will be surprised if I do. Hey! Jessica!

    "Cassidy shoots her hand up and waves it to grab your attention. You walk up to them.

    C: Doris here thinks that I should eat more vegetables so I can stay healthy. I’m already dead Doris! I can’t die more!

    D: And CASSIDY here doesn’t understand that while it may not save her from death, It’ll make her existence here just that much easier. Cassidy, you already have a bad back, save yourself from literally every other disease as well!

    OPTION:
    Cassidy, just eat the veggies. They’ll make you feel so much better, trust me.
    Hey Doris! Don’t crump her vibe! Let her have her nuggies, like she said, she can’t be any more dead.

    1.
    CASSIDY -1 AFFECTION | DORIS +1 AFFECTION
    J: Doris is right Cassidy. You already have a hard time getting up the stairs. Some vegetables won’t hurt you. It’ll probably do the exact opposite.

    "Cassidy grumbles as Doris force feeds her a head of broccoli. The sight is both horrific and oddly majestic.

    2.
    DORIS -1 AFFECTION | CASSIDY +1 AFFECTION

    C: Yeah man! Just let me eat whatever I want! Why do you care anyways?

    "Doris glares at you as she puts the fork down on the plate and rolls her eyes.

    D: Whatever. It’s not my body anyways.




    "You head back to your room and start to rest.

    DAY ENDS HERE IF MAGGIE ROUTE IS LOCKED.

    IF JESSICA HAS UNLOCKED THE MAGGIE ROUTE:

    "You quickly remember that you had some work to do for Maggie, and take out your pen and the sheet of paper and get to work.

    QUESTION ONE: what is 1x3
    QUESTION TWO: What is (amy please insert a moderately difficult math question here)
    QUESTION THREE: (amy please insert a harder math question here)

    "Satisfied with your work, you head over to Maggie’s dorm to hand in the work.
    BLACK SCREEN

    "You nervously knock at what you assume to be her door, (it has a pentagram carved into it), and await for a response.

    "Slowly she opens the door, taking a peek as to who her visitor was before pulling the door open more.

    DOOR CLICK SOUND
    Maggie Dorm
    Maggie sad

    m.c "Took you long enough. Lemme take a look

    Maggie sad blink
    If she gets at least one wrong:
    $ m.trust_ch(2))
    m.c "Hey, not bad for a novice. Maybe you have a career in plagiarism.

    If she gets all right:
    $ m.trust_ch(-1)
    show maggie happy
    m.c "Hey, this is pretty good. Better than anything I could do. Nice job.

    "Closest thing you’ll get to a compliment from her, you assume. You blush.

    If she gets all wrong"
    .trust_ch(1)
    show maggie neutral blink
    m.c "Hahahah, man this is pretty dumb. You didn’t do so well but at least I can get a laugh out of this."



    Maggie neutral
    "Maggie settles the test down on her desk, and sits down. She looks you up and down.

    m.c "So, what are you… some kinda monkey?

    J: The monkey queen, actually.

    Maggie neutral blink

    "You tease, curtseying. Maggie laughs and gets up, bowing.

    m.c "Your highness~

    Maggie neutral

    "She teases, sitting back down on her chair, and takes a sip out of her juicebox. An idea comes to mind.

    J: So now since we’re.. In somewhere more private, can I ask you a question?"

    m.c "Shoot.

    J: We both know you’re lying about the reason why you’re still here. Why do you do assignments for people when you know it won’t get you anywhere?

    Maggie sad blink
    m.c "…

    J: I mean, you laugh at the kids who come to you for help, but in the end, you’re in the exact same cycle as they are. What’s the point?

    "Maggie sighs and gets up from her chair, glaring at you.

    m.c "Are you serious, Monkey Queen? Just take a fucking look at me? We’re supposed to get ‘reincarnated into something that perfectly matches our essence on earth,’ I’m literally half a demon. The only reason I’m not in hell right now is because I died so stupidly.

    m.c "You know, on earth, I was actually kind of a big shot. Huge fucking cult leader. Jonestown type big. Killed hundreds of people.

    m.c "The only reason I’m here right now, is because I drank the wrong fucking cup of Koolaid. That's right. I died, because I drank a purple Kool Aid instead of a Koolaid jammer.

    m.c "You must be as naive as you look. There’s no getting better for people like me. I’ve been stuck here and I’m going to be stuck here for way longer than you and your dumb little soulmate will be. So get out of here while you still can. Maybe my ‘evil’ is contagious.

    "She sits back in her chair and rests her head in her hands.

    m.c "(in italics) There’s no getting better…

    "You sit yourself down on her bed, staying put.

    J: I’m not leaving.

    m.c "Don’t be difficult-

    J: No. We’re both here. Aren’t we? The universe believes that you can get better, Maggie. You aren’t here by freak chance or coincidence, so why do you act like this?

    m.c "I-

    J: Don’t give me some bullshit fucking excuse. Yeah. You were a bad person. You did bad things, and you hurt good people, but you’ve been given something that so few people are given the chance to do. To have a second chance. You’re bad for killing people, but what makes you evil is taking up this spot, for having another chance, and refusing to take it. That's what’s shitty.

    Maggie mad
    "Maggie stands up, a fire burning in her eyes. You feel like she’s ready to strike you down.

    Romance music start here
    Maggie sad blink

    "But instead, she breaks down crying. She wraps her arms tightly around your waist and pulls you in close, resting her head softly on your shoulder. You hesitate for a second, in absolute shock because of how uncharacteristic she was acting, believing for a second that it could be manipulation, but you cast all doubts aside and wrap your arms around her, knowing that in that moment, her walls had been shut down, and she was vulnerable.

    m.c "Fuck..

    X; She wipes the tears from her eyes, embarrassed that she shared such a moment with someone like- well really anybody.

    Maggie blush

    "Maggie sits on the ground against her bedframe and you follow shortly after. You chat silently about nothing in particular, when she absent mindedly grabs a hold of your hand and draws small and short circles on the inside of your palm. You lay your head on her shoulder and she smiles warmly at the gesture, believing there was no possible way of seeing the moment of weakness, yet you caught a glimpse, and the night falls silent.

    DAY END.

# This ends the game.
return
