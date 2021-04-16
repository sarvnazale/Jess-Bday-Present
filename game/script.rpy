init python:
    #integer of how many of Maggie's math questions Jess gets correct
    maggieqs = 0


    class Person:
        def __init__(self, character, name, trust = 0, route = False):
            self.c = character
            self.name = name
            self.trust = trust
            self.route = route
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
    "You look down."
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
    b.c "It appears that your… abundance of domesticated creatures, decided to take a nap on you. While you were suffocating, you began to scream, alas no one came to your aid because… they were too used to your screams..."
    "He slowly closes the file and you look down, ashamed."
    show brennan happy
    b.c "Glad to know you’ve earned your place. Welcome aboard!"
    show brennan neutral
    b.c "Oh yes! The bonfire. Let me explain!"
    b.c "At the end of this week we have our bonfire.
    You see, the purpose of this realm is to rehabilitate those pathetic individuals,
    and reincarnate them back to earth.
    Yet, every single person is supposed to go back to earth with their soulmate…"
    b.c "Usually this is a romantic soulmate, but this school has been known
    to see the platonic soul mate or two. Anyways, When you discover who your soulmate is,"
    b.c "you have to help each other rehabilitate, so you are respawned at the exact same time.
    They will probably give you an item, maybe a hair clip or something. If you throw it into the fire, and the fire changes colour..."
    show brennan blush
    b.c "...voila. You’ve met your match."
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
    "Trembling, you get up from the chair, still shaken up, you head towards the door and murmur a weak \"alrighty then.\""
    play sound "audio/doorsfx.mp3"
    scene bg hall
    with dissolve
    #add hallway music later
    play music "audio/beforeclass.mp3" fadeout 1.0 fadein 1.0
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

    play music "audio/cassidy.mp3" fadeout 1.0 fadein 1.0
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
    play sound "audio/Doorsfx.mp3"

    scene bg hall
    with dissolve

    "Class goes by fast, but let’s be honest. You weren’t really listening. You decide to head over to the library, which took you a really long time to find."

    scene bg library
    with fade
    play sound "audio/Doorsfx.mp3"

    "You start looking around, but your attention is quickly averted to the large sobbing man sitting
    alone among a pile of math sheets and textbooks."

    "You look away, not wanting to make him uncomfortable, but his sobs and whimpers fill the library, and you feel obligated to help."
    play music "audio/argha.mp3" fadeout 1.0 fadein 1.0
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
            j.c "Ah ahem.. Uh yes so, let's take a look at this first problem. Oh easy, first question: what is 9 x 12?"
            $ answer1 = renpy.input("Enter an answer: ", "", allow="0123456789")
            if int(answer1) == 108:
                show argha happy
                a.c "All right! Thanks! Now, what’s next… oh, hey, do you know how to find the value of the numerator of cos A, if the value of tan A is 4/3 and we assume cos A is positive?"
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
                    a.c "Bro… this doesn’t look right... Are you sure it's not 3? Damn and I have a test today... this better be right and my judgement is failing me! Or we’re both in deep shit.."
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
    play sound "audio/Doorsfx.mp3"
    scene bg hall
    with dissolve
    "You leave the library and head towards the gym class. Along the way you take a good look at all the strange yet very attractive people around.. How were you supposed to just choose one? Maybe one of the people you’d already met…"
    scene bg gym
    with dissolve
    m.c "HEY YOU"
    play music "audio/maggie.mp3" fadeout 1.0 fadein 1.0
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

    play music "audio/beforeclass.mp3" fadeout 1.0 fadein 1.0

    "Scanning the area to make sure no one sees you eat alone like a loser, you meander your way over to a bench. Plopping yourself down, you unwrap your sandwich and take a bite."
    j.c "God.. This sucks"
    "You settle the sandwich on your lap and look at it in disgust. All of a sudden, a bird sits down right in front of you."
    "You rip off a small piece of bread and throw it onto the floor for it to eat."
    j.c "There you go buddy... I hope you don’t have… taste buds."
    "You watch the bird as it gobbles up the sandwich, when all of a sudden, you hear a squeal."
    d.c "Holy shit! Holy shit holy shit!"
    show doris neutral
    play music "audio/doris.mp3" fadeout 1.0 fadein 1.0
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
    "You wake up in your dorm, only slightly ready to begin a new day. The day prior had knocked you out well."
    "Reluctantly, you get out of your cozy bed, looking around your room for the textbooks needed for your class today. When you’re all prepared, you leave the room, hoping to run into some of the new friends you’ve made."

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
    j.c "Arghawan, what are you doing?"
    "Arghawan lights up at the sight of you. He puts on a flirtatious charm and winks at you. Or is that just how he regularly looks?"
    show argha happy
    a.c "Oh, Jemica!"
    j.c "Actually, it’s Jess-"
    "He stops you dead in your tracks and grabs you by the shoulders."
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
    $ a.trust_ch(1)
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
    "You smile and flash him a wink, trying to match his energy. You decide the best way to be friends is to buy his love."
    j.c "No worries, I got you covered."
    show argha blush
    a.c "Woah, dude… You’re awesome."
    "He gushes. Man! This motherfucker cute!"
    "The two of you walk back to the cafeteria, making small, casual conversation with each other."
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
    show argha neutral"
    "Arghawan takes a bite out of his sub and lets out a guttural moan and rolls his eyes. It makes you kind of uncomfortable."
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
    j.c "I mean, not like that. I like you but I don’t LIKE like you.. Like I like you as a friend, even more than that!"
    "You realize what you just said."
    j.c "AGhhhh I mean like a good friend! Like a really good friend. Am I coming across clear or hahahah…"
    "You nervously laugh and shakily grab ahold of the drink on your table, chugging it to calm yourself down."
    show argha happy blink
    "Arghawan chuckles."
    show argha sad
    a.c "Awee so you’re saying you don’t like me?"
    "Arghawan teases as he pouts and feigns sadness, acting like a shot puppy. You blush heavily and fold your hands in your lap, looking down to trying to hide your beet red face. *Was he always this intense?*"
    j.c "You know what I mean, asshole."
    "Your face cracks into a crooked smile and you look to the side."
    show argha blush
    a.c "You’re blushing! Aww, what’s wrong? Monkey got your tongue?"
    "Quickly, Arghawan shoots his head to the left to check the clock mounted on the wall."
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
    $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan", route = True)
    show brennan sad blink
    b.c "I’m so sorry to hear that Jessica."
    "The headmaster sighs."
    show brennan sad
    b.c "If you ever feel lonely during lunch, feel free to pay my office a visit. While I don’t recommend it because you will lose valuable time with your peers, I wouldn’t want you to feel unwelcome."
    "Strangely excited for this new offer, you smile and gladly accept."
    j.c "Oh! Thank you so much! That’s really kind of you."
    show brennan blush
    $ b.trust_ch(1)
    b.c "Just my duties as headteacher!"
    jump blmstartend

label blmstartend:
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
    Next class was english. You realize that your schedule has changed a bit. Courses were rearranged and you no longer had gym, rather english, and you had biology towards the end of the day."

    "You hurry yourself out of class and say bye to Arghawan. He shoots you a wink. Cocky bastard."

    #doing this again lolol
    scene bg classroom
    with fade
    #Classroom
    # this real? Class_sounds.mp3
    "From afar you can see who else but Maggie furiously jots down notes and mumbles under her breath."
    show maggie mad
    m.c "Ray Bradbury…. Sexist piece of shit why don’t you suck my-"
    "You interrupt her before she can go any further, afraid she may implode."
    j.c "Heya Maggie, what are you reading?"
    show maggie happy
    "She looks up and her expression softens a bit. She shows you the cover cover of the book and groans."
    m.c "Possibly the worst novel one of these white guys have ever written. Its called Fahrenheit 451."
    "You nod slowly in agreeance, more curious as to why she is reading the book if she hates it so much."
    j.c "So why are you reading it if you hate it so much?"
    "She looks around for the teacher and leans in. A small bit too close for your liking."
    m.c "You see, I have this… extremely lucrative business. Some of these assholes really want to get out of this whole… purgatory joint. So they pay me to do their work for them. Of course, they owe me. It can be money… favours…. Anything."
    "Maggie laughs heartily."
    show maggie happy blink
    m.c "And what these stupid bastards don’t even realize, is that the universe KNOWS I’m doing it for them! It’s not helping them one bit… so every bonfire they come crawling back, begging for me to do more!"
    "You stare blankly for a bit, realizing why she was still sitting in purgatory, tired but working away."
    j.c "You don’t… want to leave?"
    "She freezes for a second."
    m.c "Nah, not for a while. I’m kinda comfy here, ya know? They make this place too nice for us. A lot of people just end up staying for a really long time."

    menu:
        "Can I help you out with some of that work?":
            jump maggiestart
        "Can you do one for me?":
            $ m.trust_ch(-1)
            m.c "Are you an actual idiot? Didn’t I just explain to you what happens to those dumbasses when they ask me for help?"
            "Your face heats up in embarrassment as you feel the hammer of judgement BONK you on the head."
            m.c "Out of respect for you, and for my fine establishment, absolutely the fuck not."
            "Hey, at least she respects you."
            hide maggie
            jump lunchday1

label maggiestart:
    show maggie happy
    $ m = Person(Character("Maggie"), "Maggie", route = True)    
    m.c "That would be awesome! I really fucking suck at math, so I could really use your help on this one."
    "Jesus fucking christ how did you get stuck doing MORE MATH?!"
    j.c "Oh.. Math. Fun."
    show maggie happy blink
    m.c "Glad you think so! You can bring it to my room at night so I can give it to those stupid assholes tomorrow morning."
    "She grumbles."
    show maggie angry
    m.c "Maybe they’ll finally pay me this time."
    "Maggie hands you a sheet of paper, a name poorly scribbled at the top read ARGHAWAN. You sigh and smile to yourself as you shove the paper into your bag to do later tonight."
    show maggie neutral
    j.c "You seem tired, though, are you getting enough sleep?"
    show maggie sad blink
    "Maggie sighs and continues to read, jotting down notes as she goes along."
    show maggie sad
    m.c "I mean, do I need much sleep? It’s not like I can die here anyways."
    "Maggie mumbles."
    "You furrow your brows, frustrated at her deflection towards your concern."
    j.c "We both know that's not the point of this place. It’s to become a better person."
    "Maggie seems to be a bit more frustrated than before."
    m.c "I didn’t ask for your therapy or your concern. Take your interrogation to someone who’s more desperate for attention, like Arghawan."
    "Taken aback by her comment, and slightly offended on Arghawan’s behalf, you mutter a \"fine\" and sit back into the chair, ignoring her for the rest of the class."
    "Peeking at her once, you see her face muddled with guilt. Your expression softens too, yet you sit in each other’s silence. It's not unpleasant."
    hide maggie
    jump lunchday1

label lunchday1:
    "Class ends and hoards of students head down towards the cafeteria to grab a bite to eat."

    scene bg lunchroom
    with fade
    #Cafeteria_noises.mp3

    "You decide you want to sit with..."
    menu:
        "Maggie, sitting alone like a normal person.":
            $ m.trust_ch(1)
            show maggie neutral
            "You sit with Maggie. The awkwardness from class seems to have melt, and you share smalltalk about the class while she does some work."
            jump postlunchday1
        "Doris, sitting on the windowsill like a housecat.":
            $ d.trust_ch(1)
            show doris blush
            "Doris isn’t much for talking, but the two of you enjoy sitting together, bathing in the warm orange sun permeating through the window."
            jump postlunchday1
        "Arghawan, sitting next to heaps of people with a single empty seat next to him.":
            $ a.trust_ch(1)
            show argha happy
            "Sitting next to Arghawan and his group of friends is almost too loud and exciting. Bonus points, because he put his arm around you."
            jump postlunchday1
        "Cassidy, who isn’t actually sitting, but seems to be lying down on the dirty floor and moaning in pain, wailing \"my back, my back.\"":
            $ c.trust_ch(1)
            show cassidy happy blink
            "You lie on the floor next to Cassidy and offer to give her one of your life-changing massages. It’s kind of weird, and a bit pointless, since she’s cursed with a bad back, but she appreciates the effort."
            jump postlunchday1

label postlunchday1:
    scene bg hall
    "You finish off the rest of your classes with nothing interesting happening in any of them. You head towards you dorm to rest, when you run into Cassidy and Doris arguing."
    show doris mad at left
    show cassidy blink mad at right
    d.c "Cassidy, you have to eat vegetables! To get big and strong! You can’t just be eating dino nuggies for the rest of eternity, can you?"
    show cassidy mad at right
    c.c "I can, and honestly neither of us will be surprised if I do. Hey! Jessica!"
    "Cassidy shoots her hand up and waves it to grab your attention. You walk up to them."
    c.c "Doris here thinks that I should eat more vegetables so I can stay healthy. I’m already dead Doris! I can’t die more!"
    show doris mad blink at left
    d.c "And CASSIDY here doesn’t understand that while it may not save her from death, It’ll make her existence here just that much easier. Cassidy, you already have a bad back, save yourself from literally every other disease as well!"

    menu:
        "Cassidy, just eat the veggies. They’ll make you feel so much better, trust me.":
            show doris happy at left
            show cassidy mad at right
            $ d.trust_ch(1)
            $ c.trust_ch(-1)
            j.c "Doris is right Cassidy. You already have a hard time getting up the stairs. Some vegetables won’t hurt you. It’ll probably do the exact opposite."
            show cassidy mad blink at right
            "Cassidy grumbles as Doris force feeds her a head of broccoli. The sight is both horrific and oddly majestic."
            jump dormday1
        "Hey Doris! Don’t crump her vibe! Let her have her nuggies, like she said, she can’t be any more dead.":
            show doris mad at left
            show cassidy happy at right
            $ d.trust_ch(-1)
            $ c.trust_ch(1)
            c.c "Yeah man! Just let me eat whatever I want! Why do you care anyways?"
            show doris mad blink at left
            "Doris glares at you as she puts the fork down on the plate and closes her eyes in frustration."
            show doris mad at right
            d.c "Whatever. It’s not my body anyways."

label dormday1:
    "You head back to your room and start to rest."
    stop music
    scene dorm
    with fade
    if m.route == False:
        jump day2start

    else:
        "You quickly remember that you had some work to do for Maggie, and so you take out your pen and the sheet of paper and get to work."

        "The first problem reads: \"What is 1 X 3?\""
        $ answer3 = renpy.input("Enter an answer: ", "", allow="0123456789")
        python:
         if (answer3==3):
             maggieqs += 1

        "The second problem reads: \"If x^2 - 7x + 10 = 0, what is one possible value of x?\""
        $ answer4 = renpy.input("Enter an answer: ", "", allow="0123456789")
        python:
         if (answer4==2 or answer4==5):
             maggieqs += 1
        "The final problem reads: \"What is the value of the numerator of cos A, if the value of tan A is 4/3 and we assume cos A is positive?\"
        You feel that you have seen this exact problem before..."
        $ answer5 = renpy.input("Enter an answer: ", "", allow="0123456789")
        python:
         if (answer5==3):
             maggieqs += 1
        "Satisfied with your work, you head over to Maggie’s dorm to hand in the work."

        scene bg hall
        with fade
        "You nervously knock at what you assume to be her door, (it has a pentagram carved into it), and await for a response."
        show maggie neutral
        "Slowly she opens the door, taking a peek as to who her visitor was before pulling the door open more."

        #DOOR CLICK SOUND

        "You step into her dorm, closing the door behind you."
        scene dormMaggie
        with fade
        show maggie sad
        m.c "Took you long enough. Lemme take a look!"
        show maggie sad blink

        if (maggieqs==3):
            $ m.trust_ch(3)
            show maggie happy
            m.c "Hey, this is pretty good. Better than anything I could do. Nice job."
            "Closest thing you’ll get to a compliment from her, you assume. You blush."
            jump maggos

        #does elif work in renpy? yes it does
        else:
            if (maggieqs==0):
                $ m.trust_ch(1)
                show maggie neutral blink
                m.c "Hahahah, man this is pretty dumb. You didn’t do so well but at least I can get a laugh out of this."
                jump maggos

            else:
                $ m.trust_ch(2)
                m.c "Hey, not bad for a novice. Maybe you have a career in plagiarism."
                jump maggos

label maggos:
    show maggie neutral
    "Maggie settles the test down on her desk, and sits down. She looks you up and down."
    m.c "So, what are you… some kinda monkey?"
    j.c "The monkey queen, actually."
    show maggie neutral blink
    "You tease, curtseying. Maggie laughs and gets up, bowing."
    m.c "Your highness~"
    show maggie neutral
    "She teases, sitting back down on her chair, and takes a sip out of her juicebox. An idea comes to mind."
    j.c "So now since we’re.. In somewhere more private, can I ask you a question?"
    m.c "Shoot."
    #when i read this for the first time i was expecting smth dirtier (or at least more forward) tbh /srs LOL THAT'S FUNNY
    j.c "We both know you’re lying about the reason why you’re still here. Why do you do assignments for people when you know it won’t get you anywhere?"
    show maggie sad blink
    m.c "…"
    j.c "I mean, you laugh at the kids who come to you for help, but in the end, you’re in the exact same cycle as they are. What’s the point?"
    "Maggie sighs and gets up from her chair, glaring at you."
    m.c "Are you serious, Monkey Queen? Just take a fucking look at me? We’re supposed to get \"reincarnated into something that perfectly matches our essence on earth\", and I’m literally half a demon. The only reason I’m not in hell right now is because I died so stupidly."
    m.c "You know, on earth, I was actually kind of a big shot. Huge fucking cult leader. Jonestown type big. Killed hundreds of people."
    m.c "The only reason I’m here right now, is because I drank the wrong fucking cup of Koolaid. That's right. I died, because I drank a purple Kool Aid instead of a Koolaid jammer."
    m.c "You must be as naive as you look. There’s no getting better for people like me. I’ve been stuck here and I’m going to be stuck here for way longer than you and your dumb little soulmate will be. So get out of here while you still can. Maybe my \"evil\" is contagious."
    "She sits back in her chair and rests her head in her hands."
    m.c "{i}There’s no getting better…{/i}"
    "You sit yourself down on her bed, staying put."
    j.c "I’m not leaving."
    m.c "Don’t be difficult-"
    j.c "No. We’re both here. Aren’t we? The universe believes that you can get better, Maggie. You aren’t here by freak chance or coincidence, so why do you act like this?"
    m.c "I-"
    j.c "Don’t give me some bullshit fucking excuse. Yeah. You were a bad person. You did bad things, and you hurt good people, but you’ve been given something that so few people are. A second chance."
    j.c "You’re bad for killing people, but what makes you evil is taking up this spot, for having another chance, and refusing to take it. That's what’s shitty."

    show maggie mad
    "Maggie stands up, a fire burning in her eyes. You feel like she’s ready to strike you down."
    #Romance music start here
    play music "audio/romance.mp3" fadeout 1.0 fadein 1.0
    show maggie sad blink
    "But instead, she breaks down crying. She wraps her arms tightly around your waist and pulls you in close, resting her head softly on your shoulder."
    "You hesitate for a second, in absolute shock because of how uncharacteristic she was acting, believing for a second that it could be manipulation, but you cast all doubts aside and wrap your arms around her, knowing that in that moment, her walls had been shut down, and she was vulnerable."
    m.c "Fuck..."
    "She wipes the tears from her eyes, embarrassed that she shared such a moment with someone like- well really anybody."
    show maggie blush
    "Maggie sits on the ground against her bedframe and you follow shortly after. You chat silently about nothing in particular, when she absentmindedly grabs ahold of your hand and draws small and short circles on the inside of your palm."
    "You lay your head on her shoulder. She smiles warmly at the gesture. She believed that there was no possible way of seeing a moment of her weakness, yet you caught a glimpse. The night falls silent."
    scene dormMaggie
    show maggie
    with fade
    "Time passes and eventually you decide to part ways and go to bed."
    hide maggie
    with dissolve
    play music "audio/doorsfx.mp3"
    scene dorm
    with fade
    jump day2start

label day2start:
    #day 2 stuff here
    "You drift off to sleep, awaiting the next day..."
    scene bg dorm
    with fade

    scene bg dorm
    with dissolve
    "Once again, you wake up, finding yourself in your dorm. You stretch to relieve yourself of fatigue, and get ready for the day."

    "You take a quick glance at your schedule, noting its differences from the day before. Shrugging, not really caring, you prepare yourself for each of your classes to the best of your abilities and head out, ready to face the day."

    scene bg hall
    with dissolve
    "You walk into your Biology class, looking for a familiar face and smile when you finally find one."

    scene bg classroom
    show doris neutral
    "Doris is sitting at a table by herself on the far left side of the room, and while you’re walking over to greet her, you notice her inspecting… mushrooms. "
    "Doris stares intensely at the forage of mushrooms she has around her, periodically lifting up one from the table to examine it further."
    "She continues this until she finally leans in, ready to take a bite. Panic sweeps through you when you remember reading about two mushrooms that look exactly the same… except one of them is poisonous."
    "Quick, what should you do?!"

    menu:
        "Stop her before it’s too late!":
            j.c "Doris, no!"
            "You rush over to Doris, swatting the mushroom out of Doris’ hand, which dissolves into thin air before it manages to hit the table. You breathe a sigh of relief but Doris doesn’t seem all too happy."
            show doris mad
            d.c "What the hell?!"
            "Doris looks at you, furiously. You jump, slightly out of fear. This wasn’t the reaction you were hoping for."
            d.c "That was a vanishroom! Gah! It took me forever to find one of those!"
            j.c "I-I thought those were... poisonous...?"
            d.c "This isn’t Earth, the plants are different! Besides, we’re already dead, Jessica!"
            "You gulp audibly, that was a good point…"
            show doris sad
            d.c "Why didn’t you just trust me? I know what I’m doing."
            $ d.trust_ch(-1)
            "You open your mouth to issue an apology but nothing comes out… Shame washes over you and you mumble a goodbye, while finding a table to sit at, far away from Doris. "
            jump classendd2
        "Trust her judgement.":
            "You force yourself to stop in your tracks, and relax. She seems to know her stuff, or at least, better than you do."
            $ d.trust_ch(1)
            "Doris bites into the mushroom, her eyes glimmering."
            show doris blush blink
            d.c "Wow, this is so fluffy!"
            show doris happy
            "Out of the corner of her eye, she notices and turns towards you."
            d.c "Jessica, I didn’t see you there! C’mon, you have to try this!"
            j.c "A little reluctantly, you sit next to Doris and lean over, as Doris feeds you the mushroom she was eating just seconds before."

            " Before you realize the implications of her actions, a euphoric sensation hits you. For a moment, you can’t decipher what the taste reminds you of, before you remember the old stew your grandmother used to make you."
            "You look at Doris with a look of curiosity and excitement, desperate to try some more. "

            j.c "That was… the best thing I’ve ever tasted!"
            "Doris smiles at you, allowing you to take another bite as she launches into an explanation. "
            show doris happy blink
            "That was a vanishroom. They take the taste of a memory you thought was long gone, they help me remember the good old days."
            j.c "So… like drugs?"
            show doris happy
            d.c "Like drugs."
            d.c "Here, I have some extra I’d be happy to give you."
            "You grin, and eagerly take the gift offered to you."
            d.c "It’s nothing… Don’t worry about it."
            " Doris coughs nervously and tenses up, as if she’s working up to ask you an important question. You stare at her, wondering what she’s going to say next."
            d.c "Would you… maybe want to… forage some with me later?"
            menu:
                "Yes":
                    #Doris route unlocked
                    $ d = Person(Character("Doris"), "Doris", route = True)
                    j.c "Are you kidding? Of course, I’d love to!"
                    "Doris’ posture instantly relaxes and she shoots you a stellar smile that makes you feel warm all over."
                    show doris happy
                    d.c "Great, I’ll see you later this week then?"
                    j.c "Yep, it’s a date!"
                    "You freeze, realizing what you just said."
                    j.c "Shit! Uh, I didn’t mean it like that-"
                    show doris blush
                    d.c "It’s alright… I don’t mind. It’s a date then."
                    "You and Doris laugh nervously, avoiding eye contact with one another. You turn to her and open your mouth to say something, but at that moment, the teacher walks in, instructing everyone to take out their textbooks."
                    jump classendd2
                "No":
                    j.c "No thanks, I’m not really interested in that kind of stuff."
                    show doris sad blink
                    "Doris’ body delfates, mimicking a balloon. For a moment, she looks really disappointed before she forces a smile on her face."
                    "It’s alright, I understand."
                    jump classendd2


label classendd2:
    "After class ends, Doris rushes out before you get the chance to speak to her again. You sigh, a little sad but you’ll probably run into her later, right?"
    "You look at your schedule for a quick reminder on where you’re supposed to go next. Study hall, nice. "
    scene bg library
    "You enter the Library, expecting to find Chad but just find yourself even more disappointed when he’s nowhere to be found. "
    "Oh well, this was to be expected, he’s probably chatting up some nymph. "
    "You try to study for a few minutes before giving up and deciding to head to your next class early."

    scene bg classroom
    with dissolve
    "You go to your English class, and smile in excitement when you see Maggie. "
    "You walk over to her only to stop dead in your tracks when her demonic screams erupt."
    show maggie mad
    m.c "FUCK! YOU HATSUNE MIKU WHORE! JUST LET ME GET THE DAMN B SCORE!"
    "You feel a drop of sweat slide down your back as you remember the various Hatsune Miku posters plastered all over your dorm room. "
    "You notice Maggie tapping intensely on her phone, snarling. "
    show maggie mad blink
    m.c "I swear I’m gonna kill Arghawan for telling me to play this bullshit fucking game."
    "Maybe it’s best not to talk to her when she’s busy."
    show maggie neutral
    "You quietly walk away, pretending as if you never tried to approach her in the first place and find a table. You sit there until the bell rings and quickly bolt from class, yet there is a small moment where she catches you looking over your shoulder to catch a glimpse of her, and she gives you a small smile."
    scene bg hall

    "You speed through the halls, trying to go to your next class, Music. "
    "You see Arghawan walking on the other side of the hallway, with his arm wrapped around some girl you’ve never seen before, just as you expected. He passes by you, chatting away and completely unaware of your presence."
    scene bg classroom

    "You can’t help but feel a little annoyed when you enter music class. "
    "You walk over to the cabinet to take out your instrument but instead you’re met with the sight of a hunched over Cassidy, breathing heavily."
    j.c "Cassidy? What are you doing in there?"

    show cassidy mad
    c.c "None of your business!"
    "You have a feeling Cassidy isn’t being quite honest and you look around the room, searching for the source of Cassidy’s problems when you’re met with the sight of a beautiful young girl, elegantly playing the piano. A crowd gathers around her and they all stare at her with awe. "

    "You turn back to Cassidy, assessing whether or not this is the reason for Cassidy’s distress or if hunched over and breathing heavily was just Cassidy’s default."

    "What should you say…?"

    menu:
        "Wow, that girl sucks.":
            $ c.trust_ch(2)
            show cassidy neutral
            c.c "I know right?!"
            j.c "God, yeah, so fucking obnoxious."
            c.c "Everything about her is so perfect it pisses me the fuck off. Like why is someone like her still in purgatory anyways? She should’ve reincarnated ages ago"
            c.c "And don’t even get me started on her teeth!"
            "Cassidy leans forward and whispers, staring at you intensely."
            c.c "She has no fillings…!"
            "Wow, that’s a totally normal thing to notice and not creepy at all."
            menu:
                "Good for her…":
                    "Cassidy rolls her eyes at you in annoyance."
                    c.c "Yeah, sure, whatever."
                    $ c.trust_ch(-2)
                    c.c "Anyways, if you’re not going to say anything worthwhile, could you just leave me alone? The whole point of me hiding in here is so that no one could talk to me, thanks"
                    "Before you have the chance to say anything else, Cassidy shuts the cabinet doors on you."
                    "Well, that probably could’ve gone a lot better!"
                    jump musicendd2
                "God, people with good oral hygiene are such show offs.":
                    c.c "Ugh, I totally agree!"
                    $ c.trust_ch(1)
                    c.c "When I used to be a human, all those stupid fancy tooth doctors would always nag me. They’d sigh in frustration whenever I walked into their office, like hey pal, I don’t wanna be here either!"
                    "You find yourself laughing and for a while Cassidy stares at you blankly, before joining you."
                    c.c "You know, you might not be as bad as I originally thought you were. We seem to have a lot in common."
                    j.c "R-Really...? I feel the same way about you, I-"
                    c.c "Aaand, you’ve already ruined it."
                    "Before you can respond, Cassidy closes the cabinet door, leaving you standing there, dumbfounded."
                    jump musicendd2
        "Are you sure being hunched up like that is good for your body?":
            "Cassidy huffs, offended and you already feel yourself bracing for a negative reaction."
            c.c "I’m already dead, bitch, nothing can harm this body."
            "Cassidy growls at you and before you can mutter an apology, she shuts the cabinet door instantly. "
            "Wow, she seems really fucking pissed, good job, asshole. Just so you know, any relationship points you try and gain from her will be reduced in your next interaction."
            jump musicendd2
label musicendd2:
    "Unable to communicate with Cassidy for the rest of the class, you do your own thing until the bell rings. "
    scene bg lunchroom
    "You hurry and make your way to the Cafeteria, wanting to get a good seat. When you finally arrive, you’re presented with 3 options"
    menu:
        "MAGGIE, who is sitting with CASSIDY. They seem to be arguing about something":
            show maggie mad at left
            show cassidy mad at right
            "You silently take a seat next to Maggie and Cassidy, they both quiet down when they see you and pause whatever argument they were having when they notice you. The three of you sit in awkward silence, save for the sound of Cassidy’s concerning breathing patterns."
            show cassidy neutral at right
            show maggie neutral at left
            $ m.trust_ch(1)
            $ c.trust_ch(1)
            jump maggieargha

        "ARGHAWAN, who’s flirting with DORIS.":
            "You butt your way in between the way of Doris and Arghawan, the two of them both smile when they see you, Doris’ being one of relief. Arghawan shifts his focus onto you, it’s weird of course, but it feels nice getting some attention from him."
            $ a.trust_ch(1)
            $ d.trust_ch(1)
            jump maggieargha

        "BRENNAN LEE MULLIGAN…?":
            "Slowly and shyly you peek into Brennan Lee Mulligan’s office."
            show brennnan happy
            jump maggieargha

label maggieargha:
    "The rest of your school day passes by without any problems, and before you know it, you’re finally done for the day. "
    "You eagerly make your way towards your dorm when you pause midway after hearing Arghawan and Maggie both arguing."
    "The two of them are both sitting down in the hallways, both holding phones. That’s certainly a duo you wouldn’t have expected to see...."
    show maggie mad at left
    show argha mad at right
    a.c "Dude, enough with the ROKI ROKI, I’ve fucking had it with that song."
    m.c "Shut the hell up. If not Roki, then what? Your gay ass RAD DOGS? FRAGILE?! No way, asshole, no fucking way"
    a.c "First of all, I’m not gay!"
    m.c "I didn’t call you ga-"
    a.c "Second of all, they’re good songs, way better than Roki"
    m.c "YOU TAKE THAT BACK."
    a.c "I WON’T."
    menu:
        "Playing the same song over and over again does seem tedious…":
            a.c "See? Even Jessica agrees that you're being unreasonable, I’m choosing the song next!"
            m.c "Of course she agrees with you, you’ve got every girl in this school wrapped around your fruity finger, twat"
            a.c "Okay, well now you’re just being rude."
            jump argdone
        "Arghawan, stop being such a little pussy bitch.":
            m.c "There! See! Nothing wrong with wanting to listen to the same song. That's just who I am… "
            show maggie sad at left
            "Maggie fakes crying."
            m.c "And if you can’t accept me for who I am, I guess this just won’t work out.."
            show argha mad at right
            show maggie neutral at left
            a.c "I’LL SHOW YOU WHAT ‘WON’T WORK OUT"
            jump argdone
label argdone:
    "The two begin to brawl with the sounds of Hatsune Miku and various other Vocaloids in the background."
    scene bg dorm
    "You slowly walk back to your dorm to get ready for bed."
    if d.route == True:
        jump dorisdate
    else:
        jump day3
label dorisdate:
    "You recall making arrangements with Doris in class today, and start to get ready for a night out instead. The second after you finish washing your face, you hear a knock at the door. Grabbing a towel and quickly wiping your face, you make your way to open the door."
    play sound "audio/doorsfx.mp3"
    show doris happy
    "It’s Doris! She’s holding an empty basket in one hand, presumably ready for the night ahead."
    d.c "Are you ready?"
    scene bg forest
    with dissolve
    "The two of you walk in silence in a large clearing in the forest. She looks at you and kneels onto the ground, her eyes inviting you to do the same."
    d.c "You see, the thing with Vanishrooms is that you have to be extremely quiet. They’re shy and hate loud noises, so once a night, the minutes we have between the daytime animal settling down to rest, and the nocturnal ones just waking up, they come out to graze. "
    "You try to respond, but Doris holds her finger to your mouth to shush you."
    d.c "I can speak, only because they trust me, me and the shrooms became friends a couple of decades ago, and I’ve kept their location a secret ever since then. You’re the only person besides me to ever come here."
    "she looks to the side."
    show doris neutral
    d.c "I also trust that you keep this a secret. It took me an entire night to convince them to let me bring someone new. If you start telling people, I don’t know if they’ll trust me again."
    "You faintly nod, and all of a sudden, the ground begins to glow. Magically, clumps or iridescent mushrooms appear from thin air."
    show doris happy blink
    "Carefully, Doris reaches to pick some up and place them in her basket. She invites you to do the same."
    "After a few minutes, the mushrooms start to vanish again. Doris smiles warmly and examines her harvest."
    d.c "So many this time around.. They seem to like you."
    show doris blush blink
    "this time, it’s the both of you blushing. You both sit, you’re leaning against a tree hugging one leg while the other one lays straight, and she sits still, quite far from you."
    j.c "Why are you sitting so far away?"
    "Doris’ eyes light up and she scoots a bit closer. Not close enough though."
    "You pester for her to come closer, and she scoots all the way next to you. Her blush intensifies."
    d.c "Sorry.. It’s just, I’m not used to people sitting so close. Or I guess, I’m the one sitting close to you."
    j.c "Why’s that?"
    d.c "Well, when we were on Earth, my family and I lived… far from society. There weren’t many people close by, so I never really got close to anyone. The few times I did go into the city, people always… "
    show doris sad
    "She stops and sighs"
    d.c "Poked fun at me. Not just me, my family, our way of living, my clothes, my lack of education, everything. So I tried to stay as far away from them as possible."
    show doris sad blink
    d.c "We didn’t need other people anyways. My parents always told me, the only thing I needed was the land. So, when they got busted for ‘tax evasion’ and tried to escape down the creek we lived by."
    show doris happy blink
    d.c "Hahah, well I guess an education would have come in handy, because we drowned. Pretty fast."
    "You look at her in a mild horror."
    d.c "Ah, no worries. I like this place a whole lot more. So many animals, so many plants, and no one really judges me."
    j.c "Then why haven’t you tried to… you know… find your soulmate?"
    show doris sad
    d.c "Well I guess it’s just the fear of someone pointing out the dirt on my dress again, or the fact that I don’t show up to class and them thinking I’m stupid. It’s just hard to relieve what I died just to forget."
    show doris sad blink
    "Doris’ body is faced away from yours now, but you shift to look at her."
    j.c "I don’t think you’re dumb or dirty, if thats the bar we’re setting here."
    "Your hand grazes her jaw and encourages her to shift her head in your direction. If you thought she was blushing hard before."
    show doris blush
    "Her head faces you, yet her eyes stare straight through you.
    You push a loose strand of hair behind her ear. Now her eyes are set straight onto yours.
    She pulls away abruptly, probably because she noticed how little distance there was between the two of you."
    "Though, she yawned and rested her head gently on your lap. You didn’t mind though, because for once that night, she seemed to be at ease. Her typically shaky smile was in a serene line, lips parted softly as she drowned into the night, and transported herself into a land of dreams."
    scene bg dorm with dissolve


label day3:
    #this is actually end of day 2 rn sorry ames for the confusion
    "Before you go to bed that night, you reach over and grab a Vanishroom. You lay back as a memory rolls back into your mind."
    #SHOW BLACK BACKGROUND HERE
    "Jess! I haven't known you for too long but it's been awesome talking to you when I do.
    Your manic energy is delightful and I hope we get to meet in human land one day soon
    (along with the rest of the server of course). I really hope you like the present,"

    "these folks put a whole lot of effort into it, especially the poor artists,
    turns out crunch culture exists in the not-even game studios too /j. Happy Birthday!"

    "ellie / luna / elizabeth / L.e / more / names / for / comedic / effect / uwu"

    scene bg dorm
    "Slowly you fall asleep, and hear strange words coming into your head."
    "A voice you can remember to be your good friend Joe’s booms through your ears."
    "Joe: Oof. Can’t believe THAT’s how she dies, huh. Welp, rest in peace I guess."



# This ends the game.
return
