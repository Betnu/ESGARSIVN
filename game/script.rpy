# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Catherine", color="#ffff00")

define m = Character("Marinha", color="#ffcccc")

define mc = Character("[povname]")

define eyeopen = ImageDissolve("eyesopen.jpg", 1.5, 100)
define eyeclose = ImageDissolve("eyesopen.jpg", 1.5, 100, reverse=True)

# The game starts here.

label start:
    #INICIO ESCENA 1
    "..."

    show bg classroom with eyeopen

    "Wh-where am I?"

    hide bg classroom with eyeclose

    "The voice of a professor, my own hand trying too hard to take notes…"

    show bg classroom with eyeopen
    #un sfx aqui tal vez en plan clink y empezar el bgm?
    "Oh, yeah, I’m in class."
    "And once again I’ve managed to lose my focus."

    $ povname = renpy.input("Well done,") #Cambiar la forma de introducir el nombre
    $ povname = povname.strip()

    "As if you could afford it."
    "Professor" "And this was today’s lecture, I hope everything was clear."
    #Revisar el texto cuando tengamos background bien
    "And once again, it wasn’t."
    "I haven’t skipped a single class, I’ve gone through a lot of the bibliography, but none of this is making sense to me."
    "It all seems to be going in circles, pointlessly."
    "But what I think of it doesn’t matter. I need to understand all this if I want to pass this subject, so I slowly raised my hand."
    "{i}The professor let out a big sigh.{/i}"
    "Professor" "You again? What haven’t you understood this time?"
    #hay que decidir el color del prota
    mc "I-I’m still having trouble grasping some of the essential concepts and how they relate to this."
    "He gave me a stern look, which made me cower a bit."
    "Professor" "Look, I don’t want to sound mean, but you really don’t seem to have understood any word I’ve said for the entire semester."
    "Professor" "And it really shows in the assignments you’ve turned in."
    "Professor" "If you’re unable to do anything well then I think you’d be better not coming back."
    "Professor" "It’s ok not to be competent, just go do something else that fits you better instead of wasting both your and our time in here and let the people who really want to learn do their work."
    "Each of his words felt like a dagger in my back."
    "There was some truth in them, but… No, that’s not it. I am not smart, that’s true, but that’s no way of talking to someone."
    "I tried to talk, but no voice came out of my mouth." 
    "It was as if there was nothing inside of me that could go out."
    "I seemed to have run out of will, out of thoughts. The only thing I could feel was a void inside of me, as well as something wet hitting my cheeks."
    "Oh."
    "No, I can’t let anyone see me like this."
    "I ran out of the class and went to the bathroom, where I could openly cry all I wanted." #hay que cambiar texto
    "Maybe he was right after all, it would be better if I didn't come again…"
    #en vez de ponerlo de golpe negro igual alguna transicion
    hide bg classroom
    #inventar una forma de poner transicion aqui
    play sound "tower_clock.ogg"
    show bg room
    "H...hnnnng…"
    "That dream again…"
    "It’s been two months already, and I haven’t gone back to class since. Friendless and dumb, what a joke would it be."
    "…"
    "I can’t keep thinking like that. The second semester has barely started, if I go back now there’s still time to catch up."
    "Different subjects, different teachers, it may not be too late."
    "This second opportunity… Brace yourself, university, this time will be the one!"
    $ renpy.movie_cutscene("opening.webm")

    #FIN ESCENA 1

    #INICIO ESCENA 2
    
    "I gathered all my courage and finally decided to go back to class."
    "Since it was the second week of the semester and I ran away in the middle of the first one it was quite hard to keep up, but putting up all my attentional abilities the first classes of the morning were finished before I had time to realise it. After all, I’ll have to redo the first semester again next year, so my priority right now isn’t to do academically well, but trying to keep up with the pace and getting myself in a good position. And speaking of that, I should really do something about my social relationships. There’s no way I can keep this up for four years just by myself."
    mc "Ugggggh…"
    "I’ve neglected my social abilities for so long… Where do I even start? How do people even meet each other? Maybe joining a club would be my best option…"


    # This ends the game.
    #c "%(player_name)s hijo de puta"
    return
