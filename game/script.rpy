init python:
    #integer of how many of Maggie's math questions Jess gets correct
    maggieqs = 0

    class Person:
        def __init__(self, character, name, trust = 0, route = False, item = False):
            self.c = character
            self.name = name
            self.trust = trust
            self.route = route
            self.item = item

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
    "A strange figure stands tall in front of you. The body odd, yet the face seems… Familiar."
    b.c "Hello there!"
    $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan", False)
    j.c "B-Brennan lee mulligan?!?"
    show brennan blush
    b.c "Well… My name is Headmaster Dean, but if you’d like, you can refer to me as Brennan Lee mulligan."
    show brennan neutral
    j.c "Wh… Why do you… Look like that? Where am I?"
    "You look down."
    show brennan happy
    b.c "Oh! Well that is a lot of interesting questions all at once.
    You see, you are in purgatory. You humans have a very weak perception of the afterlife
    you know. Unlike your heaven and hell, some people are given second chances!
    Welcome to that place."
    b.c "Also, The reason I appear like this, is because
    I assume the figure of the person you trusted most in your past life.
    I assume for you that would be… Brennan Lee Mulligan on a Kaonashi’s body…"
    j.c "O…Oh… Okay… So I’m in hell."
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
    b.c "Ah… yes… quite so…"
    "The headmaster opens a drawer and looks through a file. He grimaces."
    b.c "Oh dear…"
    j.c "What is it?"
    b.c "Are you sure you want to know?"
    j.c "Yes?!? Obviously."
    "The headmaster takes a deep breath and looks closer."
    b.c "It appears that your… abundance of domesticated creatures, decided to take a nap on you. While you were suffocating, you began to scream, alas no one came to your aid because… they were too used to your screams…"
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
    They will probably give you an item, maybe a hair clip or something. If you throw it into the fire, and the fire changes colour…"
    show brennan blush
    b.c "…voila. You’ve met your match."
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
    even though it was just shoved in your pocket."
    j.c "Period 1… Math class. Second floor, all right."
    stop music

    scene bg staircase
    with fade

    "You locate the staircase, and start to walk up, but you see a panting figure."
    show cassidy neutral blink
    j.c "whoa! Are you okay?! You’re so out of breath! Is someone chasing you?"
    show cassidy mad

    play music "audio/cassidy.mp3" fadeout 1.0 fadein 1.0
    "The girl glares slightly at you."
    c.c "Yes, I’m fine. I just… Have difficulty walking up stairs sometimes.
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
        "It's… just a flight of stairs… This shouldn’t be hard for you.":
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
    play sound "audio/doorsfx.mp3"

    scene bg hall
    with fade
    "Class goes by fast, but let’s be honest. You weren’t really listening. You decide to head over to the library, which took you a really long time to find."
    scene bg library
    with fade
    play sound "audio/doorsfx.mp3"

    "You start looking around, but your attention is quickly averted to the large sobbing man sitting
    alone among a pile of math sheets and textbooks."

    "You start looking around, but your attention is quickly averted to the large sobbing man sitting alone among a pile of math sheets and textbooks."
    "You look away, not wanting to make him uncomfortable, but his sobs and whimpers fill the library, and you feel obligated to help."
    play music "audio/argha.mp3" fadeout 1.0 fadein 1.0
    show argha mad
    a.c "FUCK! 9 x 4??? Since when did we go back to X meaning you times it! Oh god why is that little two so small and so close to the 3? Aw fuck…"
    "You slide into the seat across from the crying creature and he looks up, wiping snot from his nose."
    show argha sad blink
    a.c "hNnhn… are you *sniff*… the tutor? Bro you’re like… Thirty two minutes late… You were supposed to be here at 1:00…"
    j.c "Um, well, no I’m not your tutor, and it's 1:13. It has definitely not been thirty two minutes…"

    menu:
        "Can I help you?":
            show argha blush
            a.c "Really? You can?! Aw yeah! Thank you! Arghawan’s the name, and Charming ladies is the game."
            "Arghawan winks at you and you blush."
            $ a = Person(Character("Arghawan"), "Arghawan")
            j.c "Ah ahem… Uh yes so, let's take a look at this first problem. Oh easy, first question: what is 9 x 12?"
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
                    a.c "Bro… this doesn’t look right… Are you sure it's not 3? Damn and I have a test today… this better be right and my judgement is failing me! Or we’re both in deep shit…"
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
    play sound "audio/doorsfx.mp3"
    scene bg hall
    with dissolve
    "You leave the library and head towards the gym class. Along the way you take a good look at all the strange yet very attractive people around… How were you supposed to just choose one? Maybe one of the people you’d already met…"
    scene bg gym
    with dissolve
    m.c "HEY YOU"
    play music "audio/maggie.mp3" fadeout 1.0 fadein 1.0
    "You sharply turn around to see someone pointing their hand at you.
    All of a sudden you realize you’ve changed, entered the gym glass, and started playing a game of dodgeball."
    "Somehow you have survived an entire game of dodgeball until it was just you and some other person across the room from you."
    #make maggie angry
    #wait sarv am i missing smth why is there a comment here can i do it
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
            hide maggie
            stop music
            play sound "audio/doorsfx.mp3"
            jump cafeteria
        #changed it to "play" from "win" here… I feel there is no guarantee that you will win agaionst a new foe
        "Play the game fair and square.":
            "You assume this is the kind of person who likes a fight.
            So a fight you’ll give her. Back and forth, like it’s more intense than just trying to slap someone with a ball,
            the game goes on, but eventually you reign victorious."
            hide maggie happy
            "You leave to go change, but you hear a voice call after you."
            show maggie neutral
            m.c "HEY!"
            "you stop in your tracks."
            m.c "… Good game out there. Glad to see you aren’t a pussy like the rest of these chumps."
            "The girl who you know now to be a tiefling jerks her head at a bunch of kids to freak them out."
            show maggie happy
            m.c "My name is Maggie, and rest assured, next time, I’ll win."
            $ m = Person(Character("Maggie"), "Maggie")
            $ m.trust_ch(1)
            "She pats you on the back. Rough. A little too rough.
            So rough in fact that when you try to feign sportsmanship the inside you feel nothing but a burning pain.
            Holy shit why did that hurt so much."
            #sarv you forgot to jump to the cafeteria here… was this intentional?
            play sound "audio/doorsfx.mp3"
            jump cafeteria

label cafeteria:
    "After an afternoon of terrible, terrible classes, you decide to grab a bite to eat in the cafeteria,
    but by the time you reach the cafeteria, all of the tables are taken.
    You groan and take your three dollar sandwich elsewhere."

    scene bg outside

    play music "audio/beforeclass.mp3" fadeout 1.0 fadein 1.0

    "Scanning the area to make sure no one sees you eat alone like a loser, you meander your way over to a bench. Plopping yourself down, you unwrap your sandwich and take a bite."
    j.c "God… This sucks"
    "You settle the sandwich on your lap and look at it in disgust. All of a sudden, a bird sits down right in front of you."
    "You rip off a small piece of bread and throw it onto the floor for it to eat."
    j.c "There you go buddy… I hope you don’t have… taste buds."
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
            d.c "Oh… I’m sorry then… um … I guess I’ll get going then…"
            show doris sad blink
            $ d.trust_ch(-1)
            hide doris
            stop music
            "You see small tears well up in her eyes, but before you can stop her, she’s run away to God knows where, doing God knows what."
            jump dormchoice
        "That looks incredible!":
            d.c "…"
            show doris blush
            d.c "th… Thank you. Well you know, these birds are only attracted to beautiful things…"
            show doris blush blink
            $ d.trust_ch(1)
            show doris neutral
            d.c "OH! Like umm… ahh… That pretty bracelet you have right there! Ahh what is that? Silver?"
            "Doris’ quick change in demeanor gave you whiplash as you coughed and looked down on your wrist."
            j.c "Um actually I think its some sort of bone-"
            hide doris
            "but by the time you look back up to respond to Doris’ question, she’s gone drawing pictures of some other creature."
            stop music
            jump dormchoice
label dormchoice:
    stop music
    "You sigh and pack up, going to your dorm as classes have finished after lunchtime."
    play sound "audio/doorsfx.mp3"
    scene bg dorm
    with fade
    "Uncharacteristically, You decide to go to bed early, and reflect on your day. You feel that you’ve connected the most with…"

    menu:
        "Cassidy":
            "Cassidy may have been cold and slightly off putting, but something about her icy presence felt so warm."
            $ c.trust_ch(1)
            jump day1
        "Arghawan":
            "Arghawan seems like the classic heartbreaker, but something about him is just so magnetic… It’s probably the muscles, no yeah, it’s at least 47 percent the muscles."
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
        "Brennan Lee Mulligan…":
            "What about that Brennan Lee Mulligan guy… "
            $ b.trust_ch(1)
            jump day1

label day1:
    "Satisfied with your decision for the night, you lay your head down against the cool hatsune miku pillow and close your heavy eyes. Tomorrow is going to be crazy…"
    #will this work?
    scene bg dorm
    with fade
    #just gonna set argha's boolean to true don't mind me
    $ a = Person(Character("Arghawan"), "Arghawan", route = True)
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
    play sound "audio/doorsfx.mp3"
    "Your stomach growls again, urging you to eat something. You give in, heading towards the cafeteria and ready to eat some hashbrowns, when you find someone familiar scurrying around the halls."
    scene bg lunchroom
    with fade
    stop music
    play music "audio/argha.mp3" fadeout 1.0 fadein 1.0
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
    j.c "…Can’t say that I have."
    a.c "Yeah, neither has anyone else in the school. It’s kinda sus…"

    menu:
        "Let’s look for it together.":
            jump arghabrekkie
        "You’re kind of a scatterbrain, huh?":
            show argha neutral
            $a.trust_ch(-1)
            a.c "Aw man… That sucks… Oh well, math class starts now anyways. You should get going."
            hide argha
            stop music
            play sound "audio/doorsfx.mp3"
            jump mathday1

label arghabrekkie:
    $ a.trust_ch(1)
    show argha happy
    a.c "Seriously!? Thank you so much!"
    "And so, the two of you walk around the school, looking for Arghawan’s missing $5 bill. However…"
    show argha mad
    a.c "Man, are you serious?! We looked everywhere! It’s totally gone."
    show argha mad blink
    a.c "Someone stole it, I bet."
    "Arghawan sighs in frustration, and almost as if in sync, your stomachs both growled. You looked at eachother sheepishly…"
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
        "…pizza.":
            $ a.trust_ch(-1)
            show argha neutral
            a.c "Meh, I don’t really feel like it. I’m just gonna go for a sub instead."
            jump day1brekkie

        "…subway":
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
    j.c "I mean, not like that. I like you but I don’t LIKE like you… Like I like you as a friend, even more than that!"
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
    stop music
    play sound "doorsfx.mp3"
    jump mathday1

label blmstart:
    play sound "audio/doorsfx.mp3"
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
    stop music
    play sound "audio/doorsfx.mp3"
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
    play music "audio/maggie.mp3" fadeout 1.0 fadein 1.0
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
            stop music
            jump lunchday1

label maggiestart:
    show maggie happy
    $ m.trust_ch(1)
    $ m = Person(Character("Maggie"), "Maggie", route = True)
    m.c "That would be awesome! I really fucking suck at math, so I could really use your help on this one."
    "Jesus fucking christ how did you get stuck doing MORE MATH?!"
    j.c "Oh… Math. Fun."
    show maggie happy blink
    m.c "Glad you think so! You can bring it to my room at night so I can give it to those stupid assholes tomorrow morning."
    "She grumbles."
    show maggie mad
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
    stop music
    jump lunchday1

label lunchday1:
    "Class ends and hoards of students head down towards the cafeteria to grab a bite to eat."
    play sound "audio/doorsfx.mp3"
    scene bg lunchroom
    with fade
    play music "audio/cafeteriasfx.mp3" fadeout 1.0 fadein 1.0

    "You decide you want to sit with…"
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
    #why isn't it just called evening? idk
    play music "audio/eveningmusic.mp3" fadeout 1.0 fadein 1.0
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
            #is there a reason u got rid of this command?
            hide doris

label dormday1:
    "You head back to your room and start to rest."
    stop music
    scene bg dorm
    with fade
    #unless i'm missing smth, == False is just not but slower
    if (not m.route):
        jump day2start

    else:
        play music "audio/eveningmusic.mp3" fadeout 1.0 fadein 1.0
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
        You feel that you have seen this exact problem before…"
        $ answer5 = renpy.input("Enter an answer: ", "", allow="0123456789")
        python:
         if (answer5==3):
             maggieqs += 1
        "Satisfied with your work, you head over to Maggie’s dorm to hand in the work."
        play sound "audio/doorsfx.mp3"
        scene bg hall
        with fade
        "You nervously knock at what you assume to be her door, (it has a pentagram carved into it), and await for a response."
        show maggie neutral
        play music "audio/maggie.mp3" fadeout 1.0 fadein 1.0
        "Slowly she opens the door, taking a peek as to who her visitor was before pulling the door open more."

        #DOOR CLICK SOUND

        "You step into her dorm, closing the door behind you."
        play sound "audio/doorsfx.mp3"
        scene bg dormMaggie
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
        elif (maggieqs==0):
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
    j.c "So now since we’re… In somewhere more private, can I ask you a question?"
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
    m.c "Fuck…"
    "She wipes the tears from her eyes, embarrassed that she shared such a moment with someone like- well really anybody."
    show maggie blush
    "Maggie sits on the ground against her bedframe and you follow shortly after. You chat silently about nothing in particular, when she absentmindedly grabs ahold of your hand and draws small and short circles on the inside of your palm."
    "You lay your head on her shoulder. She smiles warmly at the gesture. She believed that there was no possible way of seeing a moment of her weakness, yet you caught a glimpse. The night falls silent."
    scene bg dormMaggie
    show maggie neutral
    with fade
    "Time passes and eventually you decide to part ways and go to bed."
    hide maggie
    stop music
    with dissolve
    play sound "audio/doorsfx.mp3"
    scene bg dorm
    with fade
    jump day2start

label day2start:
    #day 2 stuff here
    "You drift off to sleep, awaiting the next day…"
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
            j.c "I-I thought those were… poisonous…?"
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
                    j.c "R-Really…? I feel the same way about you, I-"
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
        "Maggie, who is sitting with Cassidy. They seem to be arguing about something":
            show maggie mad at left
            show cassidy mad at right
            "You silently take a seat next to Maggie and Cassidy, they both quiet down when they see you and pause whatever argument they were having when they notice you. The three of you sit in awkward silence, save for the sound of Cassidy’s concerning breathing patterns."
            show cassidy neutral at right
            show maggie neutral at left
            $ m.trust_ch(1)
            $ c.trust_ch(1)
            #no more blm route
            $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan", False)
            jump maggieargha

        "Arghawan, who’s flirting with Doris.":
            "You butt your way in between the way of Doris and Arghawan, the two of them both smile when they see you, Doris’ being one of relief. Arghawan shifts his focus onto you, it’s weird of course, but it feels nice getting some attention from him."
            $ a.trust_ch(1)
            $ d.trust_ch(1)
            $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan", False)
            jump maggieargha

        "Brennan Lee Mulligan…?" if b.route:
            "Slowly and shyly you peek into Brennan Lee Mulligan’s office."
            $ b.trust_ch(1)
            show brennnan happy
            jump maggieargha

label maggieargha:
    #i feel a black screen would be appropriate here
    scene bg black
    with fade
    "The rest of your school day passes by without any problems, and before you know it, you’re finally done for the day. "
    "You eagerly make your way towards your dorm when you pause midway after hearing Arghawan and Maggie both arguing."
    scene bg hall
    with fade
    "The two of them are both sitting down in the hallways, both holding phones. That’s certainly a duo you wouldn’t have expected to see…"
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
            m.c "And if you can’t accept me for who I am, I guess this just won’t work out…"
            show argha mad at right
            show maggie neutral at left
            a.c "I’LL SHOW YOU WHAT ‘WON’T WORK OUT"
            jump argdone
label argdone:
    "The two begin to brawl with the sounds of Hatsune Miku and various other Vocaloids in the background."
    scene bg dorm
    "You slowly walk back to your dorm to get ready for bed."
    if d.route:
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
    d.c "So many this time around… They seem to like you."
    show doris blush blink
    "this time, it’s the both of you blushing. You both sit, you’re leaning against a tree hugging one leg while the other one lays straight, and she sits still, quite far from you."
    j.c "Why are you sitting so far away?"
    "Doris’ eyes light up and she scoots a bit closer. Not close enough though."
    "You pester for her to come closer, and she scoots all the way next to you. Her blush intensifies."
    d.c "Sorry… It’s just, I’m not used to people sitting so close. Or I guess, I’m the one sitting close to you."
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
    scene bg dorm
    with dissolve


label day3:
    #this is actually end of day 2 rn sorry ames for the confusion
    #dis ames, it ok
    "Before you go to bed that night, you reach over and grab a Vanishroom. You lay back as a memory rolls back into your mind."
    scene bg black
    with fade
    "Jess! I haven't known you for too long but it's been awesome talking to you when I do.
    Your manic energy is delightful and I hope we get to meet in human land one day soon
    (along with the rest of the server of course). I really hope you like the present,"

    "these folks put a whole lot of effort into it, especially the poor artists,
    turns out crunch culture exists in the not-even game studios too /j. Happy Birthday!"

    "ellie / luna / elizabeth / L.e / more / names / for / comedic / effect / uwu"

    scene bg dorm
    #transition here? idk
    with dissolve
    "Slowly you fall asleep, and hear strange words coming into your head."
    "A voice you can remember to be your good friend Joe’s booms through your ears."
    "Joe: Oof. Can’t believe THAT’s how she dies, huh. Welp, rest in peace I guess."

    scene bg dorm
    with fade

    "The morning comes and you wake up in your bedroom. There’s a strange taste in your mouth after eating that vanishroom, but you feel warm after remembering the message your friend left to you on your birthday."
    "The schedule has changed again, but you’re flexible, it’s no big deal."

    scene bg hall
    with fade

    "You head to your first class, biology, excited to see Doris."

    scene bg classroom
    with fade

    "However, when you enter the classroom, Doris is nowhere to be found."
    "You suck it up and take a seat by the window. After a while, you notice a strange figure running around, chasing birds. Imagine your surprise when you notice that the figure was actually Doris."
    "You watch her for a while, a little bewildered and for a minute, that’s all Doris seems to do but then she secretly takes a look around her and enters the same place she brought you yesterday."
    #adding fade to same place to signify time passing
    scene bg classroom
    with fade
    "Eventually, the bell rings and you head to your next class, Music with Cassidy."
    "But much like Doris, Cassidy is off doing her own thing and doesn't seem very interested in conversation. She’s hunched over on her seat, intensely doing her music theory homework, which should’ve been done yesterday."
    "You decide not to comment on her awful posture today and just focus on the lesson your teacher is giving today."
    #here too
    scene bg classroom
    with fade
    "After what seemed like hours, the bell finally rang for English class."
    "After making your way there, you sit down next to Maggie in the middle of an argument she was having with her teacher about some sexist old white guy."

    show maggie mad
    m.c "Bro, this guy is clearly a dickhead! Why are we even examining his work in this class about REHABILITATION?"

    #new character go brr
    "Teacher" "Please, just let us move onto the next lesson."
    "Much to your demise, you had been looking forward to today's lesson, which was all about Milfs."

    menu:
        "Side with the teacher and just move on with the lesson.":
            $ m.trust_ch(-1)
            j.c "Let’s just move on to the next lesson. This isn’t worth fighting against"
            show maggie sad
            m.c "What the hell bro, why didn’t you take my side? Now we just have to sit here and look at tits. Good job."
            "Although she was bitter, you can’t help but feel you did do a good job. Unfortunately, Maggie definitely didn’t feel the same way."
            jump engday3end
        "Side with Maggie and fight with the teacher.":
            $ m.trust_ch(1)
            show maggie happy
            m.c "Yeah sir! See! She agrees! I’m done with this archaic bullshit, and move onto a new dawn of feminism-"
            "Maggie’s speech is long and drawn out and no one in the class seems to be enjoying this, well, at least accept for her. And by proxy you."
            show maggie blush
            "Maggie sits back down in her chair and turns to you."
            m.c "Thanks for taking my side! Man, I sure do love yelling at people early in the morning."
            #NOT A THING! (i'll leave it here anyway though, in this comment)
            #show maggie blush blink
            "She turns back into her seat, and listens to the lesson on MILFs with you. You both make compelling arguments to your cases, but both agree that the best milf is Izuku’s mother from BNHA."
            jump engday3end

label engday3end:
    "Class ends, and after looking at a bunch of milfs, you’re ready to wind down with some lunch. You head to the cafeteria."

    scene bg lunchroom
    with fade

    "You choose to sit with…"
    menu:
        "Maggie and Arghawan, who are playing games on their consoles \"SPIRITgame™\"":
            show maggie neutral at left
            show argha neutral at right
            $ m.trust_ch(1)
            $ a.trust_ch(1)
            $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan", False)
            "You take a seat next to the two of them, they acknowledge your presence for a quick second before focusing all their attention onto the game."
            show maggie happy at left
            show argha sad at right
            "Eventually, Arghawan sighs in what seems like defeat and Maggie laughs hysterically. She must have won whatever game they were playing."
            jump lunchend
        "Doris and Cassidy, who are talking about someone they don’t like.":
            $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan", False)
            show doris neutral at left
            show cassidy neutral at right
            "After witnessing how Maggie and Arghawan acted yesterday over games, you decided it would be safer to sit with Doris and Cassidy. The three of you partake in some civilized conversation."
            jump lunchend
        "Brennan Lee Mulligan." if b.route:
            scene bg blmoffice
            with fade
            show brennan happy
            $ b.trust_ch(1)
            "You head over to Brennan Lee Mulligan's office to enjoy some lunch with him.
            The two of you chat about schoolwork and personal lives. He gives you half of his cranberry muffin and you bond over some soap opera from when you were alive."
            scene bg hall
            with fade
            "After your lunch, you decide to wander around the school. You take special care to avoid the cafeteria, with all of the strange people…"
            jump postarg

label lunchend:
    scene bg hall
    with fade
    "Lunch ends, and you take a step out of the cafeteria into the hall. But barely after leaving the cafeteria, you hear Doris and Cassidy get into another fight."
    "You walk back in to hear what they are shouting about."
    scene bg lunchroom
    with fade
    show cassidy mad blink at right
    show doris mad at left
    c.c "OBVIOUSLY the metaphor is to outline their love for eachother! Why else would he violently proclaim his love in a physical way?"
    show cassidy mad at right
    d.c "Violently proclaim his love? Cassidy, this is abuse. This is an abusive relationship."
    show doris mad blink at left
    c.c "Doris, you have to look past the nuance. Maybe physicality isn’t what needs to be looked at here but rather the motive behind it!"
    show cassidy mad blink at right
    d.c "Motive? Behind what, throwing a limited edition Hatsune Miku figure at your wife!"
    show doris mad at left
    c.c "See! When you say it out loud it doesn’t sound too bad."
    show cassidy mad at right
    "Seeing the heated discussion unfold, you decide to participate and make your opinion on this book clear."

    menu:
        "Maybe the relationship itself being abusive is a metaphor for something!":
            show cassidy happy at right
            show doris sad at left
            $c.trust_ch(1)
            $ d.trust_ch(-1)
            c.c "See! There’s a girl who understands nuance! I’m not justifying anything but you need to read between the lines missy."
            "Doris groans and leaves the room, throwing the book in the trash on her way out."
            hide doris
            c.c "I count that as a win."
            "Cassidy huffs and walks away."
            "After the chaos of that argument, you decide to take a break but get the sudden urge to see how Arghawan was doing."
            jump postarg
        "What the hell kind of books are you guys reading?":
            $ d.trust_ch(1)
            $ c.trust_ch(-1)
            show doris mad blink at left
            d.c "Good question! Cassidy, why the hell are you choosing such garbage books for our bookclub?"
            show cassidy mad blink at right
            c.c "You keep telling me you, and I quote, \"I don’t care, it’s up to you\", and so I chose! What else do you want me to do?"
            show doris mad at left
            d.c "You’re a control freak! Every time I say I wanna read a book, you whine until I agree to give you what you want instead!"
            show cassidy neutral
            "Giving up, Cassidy groaned."
            c.c "Alright! You’re choosing next time!"
            show doris happy
            "Doris turns her head to look back at you and she smiles, winking because she finally got what she wanted."
            scene bg hall
            with fade
            "You leave quickly before there is amy more trouble"
            "When you finally manage to escape the chaos of the argument Doris and Cassidy were having, you get the sudden urge to see how Arghawan was doing."
            jump postarg

label postarg:
    scene bg outside
    with fade
    "You walk around the school, aimlessly for a while until you finally see Arghawan taking a nap… on the courtyard bench?"
    show argha sad blink
    "You wince, that surely mustn’t be good for his back. Not wanting another Cassidy to deal with, you walk over and gently nudge his shoulder, telling him to wake up."
    "Arghawan stirs, mumbling something you can’t quite catch. You shake his shoulder again."
    j.c "Arghawan, if you sleep on there, your back will hurt later on."
    show argha sad blink
    a.c "Nngh… Shut up…"
    "Arghawan doesn’t budge, and it doesn’t feel right just leaving him there, so you take a seat beside his resting body and wait."
    "The two of you relax there peacefully, and it gets a little boring at times, but it’s kind of funny seeing Arghawan snore and drool."
    scene bg outside
    show argha sad blink
    with fade
    "After what seemed like an hour, Arghawan shifts again and slowly gets up, yawning."
    j.c "Good morning…"
    show argha sad
    a.c "…"
    "Arghawan blinks once, twice, and frowns."
    show argha mad
    a.c "What are you doing here…?"
    j.c "Well, I was trying to wake you up."
    a.c "Classes are over! I can sleep for however long I want!"
    j.c "Sorry… but why are you sleeping on some bench anyways? You have a bed."
    "He doesn’t respond for a minute, and his attempts at avoiding eye contact are obvious, but after a while, he finally speaks up."
    show argha sad
    a.c "…I mean, I kind of sleep all over the school. I don’t like sleeping on my bed."
    j.c "Well, surely you can just sort that out with Brennan Lee Mulligan."
    a.c "Who?"
    j.c "The Headmaster?"
    show argha happy
    a.c "Oh, you mean the dilf dude who runs the place? I like that guy, he gives nice hugs."
    "Before you question him again, you remember Brennan mentioning something about how he takes the form of the figure you trusted the most in your past life. Huh, interesting."
    j.c "Oh… yeah, sure, let’s go with that. Anyways, why don’t you ask the- er- Dilf dude, for a better bed?"
    show argha sad blink
    "Arghawan sighs and shakes his head."
    a.c "No, the bed itself isn’t the problem. I just… dislike beds in general. They kind of… scare me."
    "You blink in bewilderment. Sure, you’ve seen Arghawan in some vulnerable positions before, but this felt… different from the other times. This time it didn’t seem so funny."
    show argha sad
    a.c "I know, it’s a really stupid fear."
    j.c "No, I don’t think that at all."
    show argha sad blink
    a.c "Every time I close my eyes and lay in a bed, I can feel the horrible sensation of suffocation all over again."
    j.c "Suffocation?"
    show argha neutral
    a.c "Haha, I guess I’ll have to give you a little explanation, huh?"
    show argha happy
    a.c "Back when I was alive and human, I was a bit of a ladies man, y’know, flirting with ladies, breaking their hearts. I messed around a lot. I know, totally different from what I’m like now, huh?"
    "You can’t tell if he’s being serious or not, but decide not to comment."
    show argha sad
    a.c "I was… a real jerk. An asshole, honestly. I never considered how my actions would have hurt others. To me, it was like a game… and for a while, I was winning, but then I never had the chance to complete it."
    a.c "You see, these girls, they uh… I guess they had about enough of me, so they decided to kill me."
    a.c "I don’t know if they did it on purpose. If it was, I wouldn’t blame them."
    show argha happy blink
    a.c "They lured me into a bedroom, and… gosh, this is gonna sound really embarrassing, but I thought we were gonna have an orgy."
    a.c "I know, that’s stupid! But I was a bit of an idiot back then… well, I guess I still kind of am, huh?"
    a.c "They tied me onto a bed, and like the dumbass I was, I thought \"wow, they’re into some real kinky shit!\""
    show argha sad
    a.c "Then they suffocated me to death… No matter how much I tried to beg them to stop, that I was sorry, they didn’t care. It was too late."
    show argha happy blink
    a.c "Hahah, sorry for talking your ear off."
    j.c "No… I understand."
    a.c "You do?"
    j.c "Well, not the whole… multiple girlfriends thing but… I was suffocated on a bed too."
    show argha sad
    a.c "Holy shit, for real?"
    j.c "Haha, my story is a little more stupider than yours though."
    j.c "I was sleeping and then my cats kinda… decided to take a nap on my face? I couldn’t breathe, so I kinda died."
    show argha mad
    a.c "Wha… Why didn’t anyone help you?!"
    j.c "Well, according to the Headmaster, everyone in my family was just so used to hearing me scream, that they kind of ignored me."
    show argha happy
    a.c "Okay, that’s a little funny."
    "The two of you both laugh together before you remember the whole reason why you were having this whole conversation in the first place."
    j.c "Hey, even if you can’t sleep on a bed, surely there must be something more comfortable than a rock hard bench."
    show argha sad
    a.c "Are you sure? I would hate to burden you like that."
    j.c "Arghawan, I wouldn’t be offering in the first place if it was a burden."
    show argha happy blink
    "Arghawan smiles and together, the two of you go to Brennan’s office and explain the situation."

    scene bg blmoffice
    show brennan neutral at left
    show argha neutral at right
    with fade

    b.c "So, what you’re saying is that Arghawan needs a new sleeping area that’s not a bed?"
    a.c "If it’s not too much trouble… sir…"
    b.c "Well, of course I’d do anything I can to help but… I’m afraid all I have to offer is this old couch I found in the dump."
    "With the snap of his fingers, a couch flies out of what seems to be nowhere and lands gracefully in front of both you and Arghawan."
    "Almost instantly, you and Arghawan clutch your nose, hoping to block out the awful stench coming from the couch."
    show argha sad at right
    "For a moment, you see Arghawan’s face fall before he plasters a smile onto his face."
    show argha happy at right
    a.c "Don’t worry sir, that works perfectly for me."
    b.c "Are you sure? I-"
    a.c "Of course! Thank you so much."

    scene bg hall
    with fade

    "Quietly, the two of you leave the office."

    show argha mad
    a.c "No way am I sleeping on… whatever that was. Oh fuck, why does it smell like that?!"
    j.c "I think it’d be safer to sleep in the woods than on that."

    if (not d.route):
        jump nowoods
    else:
        "All of a sudden your mind wanders where it shouldn’t…"
        j.c "Wait, that’s it!"
        show argha sad
        a.c "Huh?"
        "You suddenly remember the large clearing Doris showed you the other day. It’d be perfect for Arghawan!"
        "But you also remember Doris asking you to keep it a secret. Surely, if you tell Arghawan about the area, Doris wouldn’t trust you anymore. But she’ll get over it. Probably. Right?"
        "You’re gonna have to choose…"
        menu:
            "Tell Arghawan about the area.":
                jump arghaday3
                $ d.route = False
            "Keep Doris' secret.":
                jump keepdoris
                $ d.route = True
label arghaday3:
    $ a.trust_ch(2)
    $ d.trust_ch(-1)
    j.c "There’s some place I want to show you, c’mon!"
    a.c "Wha- Huh? Hold on!"
    "But there’s no time. You grab his hand and run down the hallway. Arghawan, helpless to stop you, has no choice but to follow you."
    scene bg outside
    show argha sad
    with fade
    "You keep running until you reach the forest. You ignore Arghawan’s protests as you push him through the opening of the forest and encourage him to keep going."
    scene bg argha
    with fade
    show argha neutral blink
    "And that’s when you finally find it."
    "The clearing still looks just as beautiful as the day before, and Arghawan’s complaints slowly dies down as he takes in what he’s seeing."
    show argha happy
    a.c "Holy shit…"
    j.c "It’s amazing, isn’t it? You can sleep here all you want! It’s peaceful, no distractions at all. An ideal sleeping place for a satyr such as yourself."
    play music "audio/romance.mp3" fadein 1.0 fadeout 1.0
    show argha sad
    a.c "…"
    "Arghawan stares at you, his expression unreadable. For a second, you start to wonder if you’ve done something to upset him but he suddenly grabs you, a sound that resembles a sob escaping him, and… hugs you."
    "You stand there in shock for a moment, before you melt into the hug and slowly snake your arms around him. He sniffles and whispers something you can’t quite catch."
    j.c "Are you… crying?"
    "Reaching your arm out you lightly place your arm on his shoulder."
    "Again, there was another loud sniffle."
    j.c "Oh my god, you totally are."
    "Arghawan lets go of you, wiping his tears, and frowns."
    show argha mad
    a.c "Am not!"
    j.c "Sure, whatever you say…"
    show argha sad
    a.c "Um… Thank you, seriously. I… don’t know why you’re doing this, but I’m really thankful."
    j.c "Why? I’m doing this because I care about you."
    a.c "Jessica, you truly are one of a kind."
    j.c "What do you mean?"
    a.c "I mean… I’ve been in this school for a long time, I… this sounds a little dumb but I’ve been looking for the perfect chick to be my soulmate, so we can reincarnate together. You’ve probably seen me, right? Talking to all of those girls, and all."
    show argha sad blink
    a.c "I know how it probably looks… I haven’t learned my lesson at all, huh?"
    show argha sad
    a.c "It’s the opposite, actually. I don’t want to repeat my past mistakes, that’s why… I’m so dedicated to finding a soulmate."
    show argha blush
    a.c "Jessica, I really like you… I think you’re the kind of person I’ve been looking for."
    "You open your mouth to respond but Arghawan just closes his eyes and rests his forehead against yours. The heat radiating from his soft breathing grazes your face and you rest calmly, feeling his warmth."
    a.c "It’s fine, I didn’t tell you this to get an answer… I just wanted to let you know how I feel."
    "Eventually, he pulls away from you but instead, takes your hand. He sits down by a sturdy tree, motioning for you to do the same."
    "Reaching into his back pocket, he pulls out a small pan flute and starts to play so serenely."

    #Argha-romance music start ???

    scene bg black
    with fade
    "Although it is just him playing, you can't help but feel, when you close your eyes, a phantom orchestra nowhere to be seen yet playing wonderfully as the two of you adorned in regal costume waltz across the grand ballroom of an empty palace."
    "You can almost feel the tickle of his hands on your sides, feeling his hands."
    "The plush skirt of your dress sways from the left to the right. As the speed picked up, your grip on his shoulders tightens, even though he did nothing but chuckle and pull you closer."
    "The fantasy was beautiful, yet short lived. The music soon stops, and you open your eyes."

    scene bg argha
    show argha blush
    with fade

    a.c "I… Want you to have this. Please, consider my name when you attend the bonfire."
    show argha sad
    menu:
        "Yes, of course!":
            jump arghasuccess
        "Arghawan, I’m sorry but I’m just not ready for that kind of a commitment.":
            jump arghafail

label arghasuccess:
    $ a.trust_ch(1)
    show argha blush
    "Arghawan gives you the biggest and most sincere smile, and he pulls you in for one more hug."
    a.c "Ah, I guess then, ahem…"
    "His blush brightens as he lets go because of your close distance."
    a.c "This belongs to you now."
    "He places the pan flute in your hand."
    $a.item = True
    show pipes at left
    #Panflute.png
    #Pickup.mp3
    "You graciously accept and put it along with the rest of your belongings."
    "The two of you sit in comfortable silence and eventually, you drift your eyes and fall asleep, listening to nothing but the sound of Arghawan’s breathing and the quiet chirp of the crickets surrounding you."
    "When the vanishrooms awake from their slumber, they sense a strange presence in their secret area. They shoot out a plethora of spores and fill your senses, making you recall friend who is now only a distant memory…"
    scene bg black
    with fade

    "Dear Jessica,

    I just want to let you know that you are a great friend. Every time I spend time with you is a good time, from hearing about all your amazing cats to helping you with math.
    You are an amazing, caring, and extremely interesting person and I can honestly say that to my knowledge you are my favourite lesbian on the planet.
    You’re also hilarious, and a pleasure to be around and interact with. I am so glad that I have met you, and I hope you have a simply wonderful (belated) birthday! /srs /gen /p

    Sincerely and with love /p,

    Amelia

    P.S. poly supremacy"
    jump day4begindorm

label arghafail:
    $ a.trust_ch(-3)
    $ a = Person(Character("Arghawan"), "Arghawan", route = True)
    show argha sad
    a.c "Oh, I see…"
    j.c "It’s not anything personal! It’s just, I’m not so ready for this…"
    stop music
    "Arghawan sighs and puts away the flute."
    show argha sad blink
    a.c "I’ve been ready for over a millenium, Jessica. I…I… I need to leave. Thank you, for showing me this place, but I think I’ll stick to my park bench."
    hide argha
    "Arghawan gets up and walks away swiftly. Before you know it, he’s gone, and you’re left alone. The forest no longer seemed lush and full of light, but rather dense and grim.
    You decide to go to the dorm and sleep there, instead of the now-dreary forest."
    scene bg dorm
    with fade
    jump day3enddorm

label keepdoris:
    $ a.trust_ch(-1)
    $ d.trust_ch(1)
    j.c "Oh, nevermind, haha."
    jump nowoods

label nowoods:
    j.c "This sucks… Sorry, I thought talking to the Headmaster would solve it, but I guess not."
    show argha neutral
    a.c "Nah, nah, don’t worry about it. I kind of figured this would’ve happened."
    j.c "But where are you gonna sleep now?"
    "Arghawan smirks at you and places a hand on your shoulder, leaning in. He whispers into your ear."
    show argha happy
    a.c "Maybe I can just sleep with you instead."
    "You gasp, mostly out of shock, as embarrassment rushes through your body."
    j.c "EXCUSE ME?!"
    a.c "Haha, relax! I didn’t mean it like that."
    a.c "Well, unless you want me to mean it like that-"
    j.c "No way!"
    "Arghawan just snickers and lets go of your shoulder."
    show argha neutral
    a.c "Hahaha! Thanks for all your help anyways. Seriously, you’re awesome."
    a.c "I’ve got other stuff to do though. I’ll see you tomorrow?"
    "Arghawan waves and walks away, relaxed."
    hide argha
    j.c "Bye…"
    "You go back to your dorm, still feeling a little flushed from Arghawan’s earlier comment, yet at the same time waving it off as just a dirty joke."
    scene bg dorm
    with fade
    jump day3enddorm

label day3enddorm:
    "At your dorm, you reach over to your night table, where the vanishrooms Doris gave you sit. You take a bite and sigh in pleasure. It’s just as good as you remember."
    "Eventually, you tire out and go to bed, dreaming of a distant friend due to the vanishrooms…"
    scene bg black
    with fade

    "Dear Jessica,

    I just want to let you know that you are a great friend. Every time I spend time with you is a good time, from hearing about all your amazing cats to helping you with math.
    You are an amazing, caring, and extremely interesting person and I can honestly say that to my knowledge you are my favourite lesbian on the planet.
    You’re also hilarious, and a pleasure to be around and interact with. I am so glad that I have met you, and I hope you have a simply wonderful (belated) birthday! /srs /gen /p

    Sincerely and with love /p,

    Amelia

    P.S. poly supremacy"
    jump day4begindorm

label day4begindorm:
    #i guess day 4 stuff goes here?
    stop music
    "You wake up in your dorm, a little hazy due to the events of the night before."
    "Regardless, you get ready for the new day, in a bit of a hurry. "
    if b.route:
        "Under the door, you notice a small note. Curious, you pick it up and gasp when you read the content of the note."
        "It says 'Jessica, I have something rather important I’d like to discuss with you. Please meet me as soon as you have time available.'"
        "You tuck the note into your pocket, as much as you’d like to see what Brennan needed from you, you’d have to attend your classes first."
    scene bg classroom
    with dissolve
    show cassidy happy
    "You walk into your music class and spot Cassidy, who seems a little less grouchier than usual."
    j.c "Hi, Cassidy. You look better than usual today."
    show cassidy neutral
    c.c "...Thanks"
    j.c "Did something good happen?"
    c.c "Well… I guess that depends on you."
    "Cassidy shifts in her seat nervously, she tugs on her collar a bit, as a means of fidgeting."
    show cassidy sad
    c.c "I’m going to be reading in the park later today…"
    "She falls silent for a second, before she coughs into her hands."
    show cassidy sad
    c.c "And it would be a pleasure if you could join me."
    j.c "Oh…"
    menu:
        "I’d love to join you.":
            "Cassidy pushes her glasses up her nose, pleased. "
            $ c.route = True
            show cassidy neutral blink
            c.c "Excellent, I’ll see you later today then."
            show cassidy happy
            $ c.trust_ch(1)
            "Cassidy shifts her attention back to the book she was reading, but she has a small smile on her face."
            jump classday4
        "Not today.":
            show cassidy sad
            $c.trust_ch(-1)
            c.c "That’s fine, I get it, I guess."
            "Cassidy looks back to her book, ignoring you."
            show cassidy mad
            c.c "And just so you know, I’m not upset or anything, so don't you dare get the wrong idea."
            jump classday4

label classday4:
    #idk sarv i trust u - ty ;)
    show cassidy neutral
    "Class passes by quickly, with you sneaking quick glances at Cassidy. As soon as the bell rings, Cassidy packs her things up quickly and makes a beeline straight for the door, out of your sight."
    "You enter English class and take your usual seat, not too far from Maggie."
    hide cassidy neutral
    "Class begins and the teacher instructs you all to take out your work. You felt a little more motivated than usual so you focused all your attention onto what you were currently writing. "
    show maggie sad
    "However, you kept getting the nagging feeling that somebody was watching you. The next time you felt it, you instantly looked up and caught Maggie staring at you from behind her shoulder"
    show maggie blush
    "She blushes, makes an indecipherable face, then turns back to her work."
    "You laugh quietly to yourself and carry on."
    "Eventually, English class ends and you go to your last class of the day, Biology."
    scene bg hall
    "You hurry through the halls, a little anxious to meet Doris. "
    show bg classroom
    "You walk into the Biology classroom and meet Doris’ eyes almost instantly, you gulp."
    #sorry if this is confusing i didn't want to make the if statements too long
    if (not d.route):
        jump dorisarg
    else:
        jump nodorisarg

label dorisarg:
    "She doesn't look happy… oh boy."
    "She stands furiously by the table, tapping her foot. Almost as if she was expecting you. Waiting for you."
    show doris sad
    d.c "Jessica."
    j.c "Hi, Doris."
    show doris mad
    d.c "Don’t you ‘hi’ me, how could you do this to me?!"
    "You shift your eyesight to the floor, kicking it a bit. It felt as if you were disappointing your own mother."
    d.c "How… Why?"
    "You look at her, and feel the guilt crush you once again."
    d.c "I showed you that place because I… I trusted you!"
    show doris sad
    d.c "I was such an idiot."
    j.c "Doris, I-"
    show doris mad
    d.c "No Jessica, you listen to me."
    j.c "Hey… that’s not true…"
    d.c "Oh, sure, cause you totally know him, right? His super tragic backstory which is just some weird justification for the way he treats girls?"
    d.c "He probably gave you the same routine he gives everybody. Haven’t you ever maybe realized he’s doing this just to get in your pants? He doesn't actually care about you, Jessica!"
    d.c "You're a bigger idiot than I thought you were."
    j.c "Okay, well, news flash for you, I don't care. Not about you or him."
    d.c "I don't want to speak to you… I don't know for how long, just don't talk to me and you can pass the message to Arghawan to stay away from me too. Enjoy your new little area."
    j.c "...Okay."
    show doris mad blink
    d.c "Bye."
    "Haha, nice going, bro."
    jump lunchday4
label nodorisarg:
    show doris happy
    "She smiles when she sees you and shyly waves you over."
    show doris neutral
    d.c "Jessica, I know a biology classroom is the least romantic place to do this but… here."
    "You look down at what Doris is offering you and you gasp pleasantly, it was a beautiful flower."
    show flower at right
    "Just as you reach your hands out to take it, Doris moves the flower out of your reach."
    d.c "Stay still for a minute. Oh and, close your eyes."
    "You did as you were told and you could feel something lightly graze your cheek, it sends shivers down your spine."
    scene bg classroom with fade
    show doris happy
    d.c "Okay, you can open them."
    j.c "...Where did the flower go?"
    d.c "It’s in your hair, silly."
    "You reach for your hair and sure enough, you could feel the presence of a delicate flower. "
    show doris happy blink
    d.c "It’s a gift… from me to you. I always looked at these flowers to feel at peace when I was in distress but now I don't need them anymore."
    j.c "Why?"
    show doris blush
    d.c "You seem to have the same effect on me."
    "You blush and Doris just laughs, grabbing your hand."
    d.c "“It would mean a lot if you would consider my name for the bonfire"
    menu:
        "Of course.":
            "Doris squeezes your hand, and you could only chuckle back. The two of you sit there, in an endearing silence before the teacher walks in."
            " Doris let’s go of your hand, but not without a quick kiss which makes the butterflies in your stomach go crazy."
            "You quickly walk back to your desk, smiling all the way there."
            $ d.trust_ch(1)
            $ d.item = True
            jump lunchday4
        "Sorry but...":
            "Doris instantly let's go of your hand immediately, she frowns. The embarrassment was written all over her face."
            d.c "Well… you can still keep the flower, what I said before hasn't changed."
            d.c "See you later."
            $ d.trust_ch(-1)
            jump lunchday4
label lunchday4:
    hide doris
    scene bg lunchroom
    "Class ends, which means it’s finally time for lunch."
    "The cafeteria is just as noisy as ever, and as usual, you can spot your friends."
    "Who will you sit with?"
    menu:
        "DORIS who’s sitting with MAGGIE, they both seem to be annoyed.":
            $d.trust_ch(1)
            $m.trust_ch(1)
            "You have an exhausting meal with Doris and Maggie, who’s decided to stop pestering each other and start pestering you instead much to your dismay. It’s hard to balance conversations with the two of them."
            jump maggiearghday4
        "ARGHAWAN who is loudly cracking up vulgar jokes with CASSIDY":
            $a.trust_ch(1)
            $c.trust_ch(1)
            "Arghawan tones down the jokes a little when you arrive, Cassidy on the other hand is relentless. Arghawan shoots you an apologetic smile while Cassidy loudly talks about vaginal discharge."
            jump maggiearghday4
        "BRENNAN LEE MULLIGAN.":
            $b.trust_ch(1)
            "You and Brennan enjoy another peaceful lunch period together. It feels as if with each passing day, the two of you get closer. It makes you feel warm inside."
            jump maggiearghday4
label maggiearghday4:
    " The rest of your classes blur by, and right when you’re about to make it to your dorm, you notice Arghawan and Maggie arguing again."
    show argha mad at left
    show maggie happy at right
    a.c "Are you saying I wouldn't beat you in a fight?"
    m.c "That’s exactly what I’m saying, twink."
    a.c "How many times do I have to tell you this? I know this is very disappointing to hear, but I’m not gay!"
    m.c "Shut up, Tutti Frutti."
    a.c "You’re awful."
    "Maggie just laughs manically. Oh god, they were going to have another brawl outside your dorm. You need to stop this, quickly!"
    menu:
        "Well, personally, I think Arghawan could totally kick your ass.":
            $a.trust_ch(1)
            $m.trust_ch(-1)
            "Arghawan flushes a little but puffs his chest out regardless, standing proud."
            show argha happy at left
            a.c "See? The people have spoken."
            show maggie mad at right
            "Good thing nobody asked you then, right Jessica?"
            show argha mad at left
            a.c "Hey, don’t talk to her like that!"
            show maggie happy at right
            m.c "Oh yeah? What are you gonna do about it?"
            "Wordlessly, Arghawan throws a hard punch at Maggie who slams against the wall. She cracks her bones before throwing another attack at Arghawan."
            "Anyways, they’re fighting again. "
            jump restoftheday
        "You’re so gay it hurts me, Arghawan.":
            $a.trust_ch(-1)
            $m.trust_ch(1)
            "Arghawan looks at you and pouts."
            show argha mad at left
            a.c "Not you too!"
            show maggie happy at right
            "Maggie laughs once again and pats Arghawan’s back in an attempt to console him."
            a.c "Ow, fuck, can you stop? You’re hurting me."
            m.c "..."
            "Maggie shoves Arghawan again a little harder."
            "And then she does it again."
            "I’ll save you some time, because as always, it escalated into a full on fight."
            jump restoftheday

label restoftheday:
    #what does jessica do for the rest of the day?
    if b.route:
        "Regardless, you make it back into your dorm in one piece and get ready for your plans for the rest of the day."
        jump brennanevent
    elif c.route:
        jump cassidyevent
    else:
        jump day5

label brennanevent:
    scene bg blmoffice
    "You quickly make your way to Brennan’s office, where he’s sitting at his office desk."
    show brennan neutral
    b.c "Ah, Jessica, glad you could make it."
    b.c "I’ll cut to the chase."
    show brennan happy
    b.c "Won't you stay here with me?"
    j.c "What?"
    show brennan sad
    b.c "In purgatory. I’ve seen the way you interact with others. Forgive me for saying this, but you don't seem to get along with anyone. Would you really be happy reincarnating?"
    j.c "I… I don't think so."
    b.c "Yes… That's what I believed as well."
    show brennan happy
    b.c "Not to worry, I’ve actually taken quite a liking to you"
    b.c "You could just stay here with me. You won’t have to do classes forever of course, I could arrange something for you but… if you’d like, we could have lunch together any time you’d like"
    j.c "I’d like that very much."
    b.c "I’m glad to hear it, Jessica."
    "Brennan smiles at you and hands you a pen."
    b.c "It’s nothing fancy, just something for you to throw into the bonfire."
    $ b.item = True
    show brennan blush
    b.c "I’m no soulmate but I’d like to think I’m a suitable companion. I’m looking forward to spending the rest of eternity with you, Jessica."
    "You blush, your heart racing faster. You quietly take the pen and tuck it into your pocket, alongside the note."
    b.c "Well, I’ll see you tomorrow at the bonfire then?"
    "He winks at you as you nod, flustered. You wave goodbye as you quickly exit the office, pleading your heart to stop beating so quickly."
    if c.route:
        jump cassidyevent
    else:
        jump day5

label cassidyevent:
    scene bg outside
    "You run to the park eagerly and grin when you already find Cassidy there."
    c.c "There you are, I was beginning to wonder when you’d show up."
    c.c "I’ve already chosen a lot of books for us to read together. I hope you find them suitable."
    "You look over to the books and cringe. You specifically remember Maggie pointing to those books and putting them in a list of books you should never read under any circumstances."
    "Well, either way, if it made Cassidy happy, then so be it."
    "The two of you read in silence for a good hour, it made you a little nervous but you notice Cassidy taking extra consideration not to turn the pages too fast."
    "You decide not to comment on it, knowing it would make Cassidy embarrassed."
    "After a while, you’ve finally finished the book, and Cassidy looks at you expectantly."
    "When you don't say anything, she speaks up again."
    c.c "The book, what did you think of the book?"
    "You fail to formulate words, not wanting to admit that you actually havent been paying attention to the book at all and you were using the novel as an excuse to stare at Cassidy for 2 hours."
    j.c "Oh, right! Of course, the book. I…"
    menu:
        "Oh, I actually prefer books that are written from a unique point of view than the social norm.":
            show cassidy neutral
            $ c.trust_ch(-2)
            c.c "Okay, well, I’m not even going to pretend I understood what the fuck you just said."
            show cassidy mad
            c.c "You’re totally full of shit."
            j.c "..."
            c.c "Whatever, onto the next book."
            "The two of you continue to read books until the sun goes down but the atmosphere completely changed. "
            c.c "...That sucked even more than I thought it would."
            c.c "God, you’re just like Maggie."
            "You stay silent, as Cassidy continues to hurl insults at you as she packs up her stuff. Before you fully notice, she’s already gone."
            jump day5
        "This book was awesome. Have you read his other book where those Nazi twins fall in love?":
            c.c "Right? Right?!"
            c.c "Maggie told me that it was gross and wrong but I just knew you would understand, Jessica."
            show cassidy blush
            c.c "Jessica, I’ve never connected with anyone in this entire school the way I have with you."
            c.c "Honestly, it makes me kind of scared. I've always been used to being in my own bubble for years, with no one ever understanding my struggles or problems but you changed all of that."
            c.c "This feeling is unfamiliar but… I want to know more of it."
            "Quietly, Cassidy reaches into her back pocket and hands you a music box."
            c.c "It would… be nice if you could consider my name for the bonfire."
            j.c "Oh, Cassidy, I-"
            $c.item = True
            show music box at right
            show cassidy neutral
            "Just like a ghost, Cassidy vanishes into thin air. Almost as if she was never there in the first place. You laugh a little to yourself, you didn't expect anything different from her"
            "Over the horizon, the sun slowly goes down, signaling for you to go back inside. Complying, you pick up Cassidy’s things and take it back with you into your dorm."
            jump day5
label day5:
    scene bg dorm with fade
    "You flop onto your bed exhausted, and before you know it, you’re already asleep."
    # thank fuck i am done - have fun ames i hope this code still makes sense

# This ends the game.
return
