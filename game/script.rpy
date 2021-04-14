# The script of the game goes in this file.

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

# The game starts here.

label start:

    $ b = Person(Character("Brennan Lee Mulligan"), "Brennan Lee Mulligan")
    $ j = Person(Character("Jessica"), "Jessica")
    $ c = Person(Character("Cassidy"), "Cassidy")
    $ a = Person(Character("Arghawan"), "Arghawan")
    $ d = Person(Character("Doris"), "Doris")
    $ m = Person(Character("Maggie"), "Maggie")
    $ love_candidates = [b, c, a, d, m]

    scene blm office
    with dissolve

    "Hello? Hello! Can you hear me? Ah you’re awake."

    show brennan neutral
    with dissolve

    "A strange figure stands tall in front of you. The body odd, yet the face seems.. Familiar."

    b.c "Hello there!"

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
        #$ b.trust_ch(1)
        $ option1 = True
        jump soul

    "What do you mean purgatory? Why am I not in heaven? Or uhh…":
        #$ b.trust_ch(-1)
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
    #$ b.c("My trust for you is " + str(b.trust))
    b.c "Alright so, I’m a very busy headmaster. I trust that you won’t get into trouble if you look around on your own.
    Class starts in a half hour, you best not be late!"

    'Trembling, you get up from the chair, still shaken up, you head towards the door and murmur a weak “alrighty then.”'

    play sound "audio/Door.mp3"
    scene hall
    with dissolve
    #add hallway music later

    j.c "How the hell am I supposed to know what class to go to? That creepy guy didn’t even give me a schedule…"
    "You realize, while you may be some… monkey beast… you are wearing a school uniform.
    Quickly, you check your pockets and pull out a slip of paper, somehow, it appears to be untouched,
    even though it was just shoved in your pocket.."

    j.c "Period 1… Math class. Second floor, all right."

    #stop hallway music

    scene staircase
    with dissolve

    "You locate the staircase, and start to walk up, but you see a panting figure."

    #show cassidy neutral bling

    j.c "whoa! Are you okay?! You’re so out of breath! Is someone chasing you?"

    #show cassidy mad
    #play cassidy theme

    "The girl glares slightly at you."

    c.c "Yes, I’m fine. I just.. Have difficulty walking up stairs sometimes.
    Its normal this is a normal thing for people with normal bodies to do."

    menu:
        "Do you want some water?":
            #show cassidy happy
            c.c " Thanks, but I'm not really a ‘water’ kind of girl. If you have any whisky I’ll take some. The name’s Cassidy."
            $ c.trust_ch(1)
            # show cassidy happy blink
            "Unfortunately for the two of you, neither of you have any whisky on hand, but you feel content that you may have made your first friend."
            jump library
        "It's… just a flight of stairs.. This shouldn’t be hard for you.":
            #show cassidy mad
            c.c "Yes. It is just a flight of stairs. *grumbles* You are also just a bitch. Funny how things workout that way. My name is Cassidy, but I doubt we’ll see each other often."
            "Cassidy storms away, you fear you’ve made a bad choice."
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



    # This ends the game.
    return
