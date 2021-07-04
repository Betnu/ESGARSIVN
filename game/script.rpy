# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[povname]", color="#ffffff")
define zach = Character("Prof. Nabradia", color="#800080")
define zen = Character("Z’enyth", color="#ff0000")
define eyeopen = ImageDissolve("eyesopen.jpg", 1.5, 100)
define eyeclose = ImageDissolve("eyesopen.jpg", 1.5, 100, reverse=True)
define genderflag = False

# The game starts here.

label start:
    #INICIO ESCENA 1
    $ povname = renpy.input("Your name") #Cambiar la forma de introducir el nombre
    $ povname = povname.strip()
    $ povsurname = renpy.input("Your surname")
    $ povsurname = povsurname.strip()
    menu gender:
        "Choose your pronoun"
        "He/him":
            $ povpronoun1 = "he"
            $ povpronoun2 = "him"
        "She/her":
            $ povpronoun1 = "she"
            $ povpronoun2 = "her"
        "They/them":
            $ povpronoun1 = "they"
            $ povpronoun2 = "them"
            $ genderflag = True
    "..."

    show bg classroom with eyeopen

    "Wh-where am I?"

    hide bg classroom with eyeclose

    "The voice of a professor, my own hand trying too hard to take notes…"

    show bg classroom with eyeopen
    #un sfx aqui tal vez en plan clink y empezar el bgm?
    "Oh, yeah, I’m in class."
    "And once again I’ve managed to lose my focus."
    "Well done, %(povsurname)s As if you could afford it."
    "Professor" "And this was today’s lecture, I hope everything was clear."
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
    #en vez de ponerlo de golpe negro igual alguna transicion, se puede aumentar el tiempo que esta en negro
    hide bg classroom with Pause(1.0)
    play sound "tower_clock.ogg"
    show bg room with fade
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
    #ejemplo texto que se sale fuera
    "Since it was the second week of the semester and I ran away in the middle of the first one it was quite hard to keep up, but putting up all my attentional abilities the first classes of the morning were finished before I had time to realise it. After all, I’ll have to redo the first semester again next year, so my priority right now isn’t to do academically well, but trying to keep up with the pace and getting myself in a good position. And speaking of that, I should really do something about my social relationships. There’s no way I can keep this up for four years just by myself."
    mc "Ugggggh…"
    "I’ve neglected my social abilities for so long… Where do I even start? How do people even meet each other? Maybe joining a club would be my best option…"
    
    "I headed towards the bulletin board in the middle of the hallway."
    "I never bothered giving it a look before, and all my expectations of silly, amateur flyers were shattered by the incredibly colourful, professional-looking designs that decorated the board."
    
    "Huh… The sport teams are way too intense for me, and at this point their level is incredibly high…"
    "Maybe I should go for something calmer, that lets me talk to people easier, like the literature club or…"

    "???" "What are you looking for?"

    "I heard a deep, soothing voice talking behind me."
    "It took me a few seconds to realise the question was directed to me."
    "I turned around and saw a tall, long-haired man. Just by his face I wouldn’t say he was that much older than me, he looked just like one of the senior students. His clothes, however, were too stereotypically professorish for a student to wear."

    mc "O-oh, I was just looking at the clubs. I know it’s a bit late, but it would be nice to find some place to fit in, any interesting club could do…"

    "???" "Any could do? Non non non non non. You got it all wrong."
    "???" "Do you really want a place to fit in? Do you honestly think any place “could do”? You don’t just fit in any place you shove your head into!"
    "???" "If you want to succeed you can’t expect to keep a passive attitude! Fitting in… Creating bonds… It is all about passion!"
    "???" "You need to find something you’re passionate about! A place where you and your comrades share that same fire, where you pour all of your energies. It is under that shared passion that bonds are created!" #si la sumaba a la de arriba quedaba raro

    "I didn’t know how to react. Either this man had reached the truth of the universe or he was completely full of bullshit."
    "Whatever it was, he said all that with such confidence it was very hard not to think it was sincere."

    mc "S-so what do you recommend me…?"
    "???" "Ideally, you should be the one to find your own passion and pursue it, but if you really are so lost let me light the way up for you. This one!" #Igual separar el this is the one

    "He pointed at the corner of the bulletin board, where a cute hand-drawn flyer, much humbler than the other ones laid without calling anyone’s attention."
    "It had the word “ESGARSI” written on it, and by its design it wasn’t clear at all what it was all about."

    "???" "In this world we live in we have developed so many fields of study, of knowledge, of entertainment… There are so many things that can be the focus of our passion, but maybe because of that same reason, it can be so hard to decide for just one."
    "???" "However, there’s a single aspect that has been able to fire up young blood throughout all of history."
    "???" "Rebellion! When we see power being abused, when we see suffering and injustice… we want to act against it!"
    "???" "And this is no different in the academic world. A lot of professors, now sitting comfortably in their positions of power would rather keep knowledge stale than questioning the old knowledge, so clearly outdated. And we, as people of truth have a duty to fight against that." 
    #Queda muy muy justo
    "???" "It’s the way of nature! And that is what the ESGARSI strives for. Dedicated not to any single feel, but for the advancement of all knowledge, there’s no better place for a lost student to awaken their passion."

    "W-what was that? Anyway, it sounds way too academic for me, I don’t think I’m that smart… But it may be an easy way to talk to new people."

    mc "T-thank you, sir, I-"
    zach "Oh, please, don’t call me sir, my name is Zach. Zach Nabradia. But I’d rather have you refer to me as Professor Nabradia, PhD."
    mc "O-ok, thank you, Professor Nabradia, I-"
    zach "PhD."
    mc "Yes, sorry. Professor nabradia, PhD. I’ll take it into consideration, but if you excuse me I should start going to my next class."
    zach "Of course. Take this with you, it will tell you all the information you’ll need."

    "He looked into his pocket and took out a completely wrinkled piece of paper. It was another copy of the ESGARSI flyer, also hand-drawn. It seemed a bit disrespectful to whomever drew it, but saying anything about it would probably only get me another long monologue, so I let it be. I took it with me and headed to my next class."
    #queda justo tambien
    "While walking I couldn’t help but keep staring at that piece of paper."
    "While amateurish and inconspicuous when compared to the ones that filled the board, it certainly had a unique charm that you could only appreciate when looking at it closely."
    "It felt… I know it’s weird for me to say this about a piece of paper, but in some way it felt like home. For whatever it was, looking at it just made me smile." 
    "It feels like it could be a warm place to join, but Professor Nabradia’s talk about academicism… I’ve just come back and my grades have never been something to brag about, I should do as I said and aim lower, %(povname)s, don’t go getting your hopes up all by yourself…"

    "*THUMP*"#sfx aqui obvio

    "I bumped into someone, making both of us drop everything we were carrying. I was so busy looking at this dumb scrap of paper, thinking about what-ifs and what-nots… Why do I have to be so embarrassing, stupid stupid stupid stupiiiiiiiid."
    "I slowly opened my eyes, ready to face my consequences. In front of me, a catboy was kneeling on the ground, hurriedly picking his books up. His kind face and his hair tied up made him look so soft that I could only feel worse for having inconvenienced such a person. Before I could say anything, he noticed the flyer I just dropped and suddenly started staring at me, his eyes shining."
    #se sale
    "???" "Have you just…?"

    mc "Y-yes! I have just b-bumped into you, I’m so sorry! Please let me finish picking up your stuff, it’s the least thing I can d-"

    "He looked at me with a confused innocent face, as if he had no idea what I was talking about."

    "???" "Huh? But it was me who wasn’t paying attention. When I’m in a rush I always get so focused that I can’t just notice my surroundings. Anyway, that’s not important. This flyer… Are you thinking about joining the ESGARSI?"

    mc "Uh… I, I don’t know. This flyer kind of makes me think this is the place I was looking for, but…"

    "???" "Really? You like it? I made it myself!"

    "His smile when he said that was so bright I couldn’t help but blush."

    mc "It’s great! I love it! But other than that it feels like a too formal club, I don’t think I’m smart enough for it…"

    "???" "No! Don’t say that! It is true that the boss takes it very seriously and is always thinking about academic stuff, but she never forces anyone to be as involved if they don’t want to."
    "???" "Just the opposite, everybody is really nice there, and there’s nobody who isn’t smart enough to join us! That’s our thing! There’s so many people in uni trying to discourage people, telling them they are not worth enough… And that’s not true! We help give people the small push they need to really start thinking. So, please, don’t dare call yourself stupid!"
    #la de arriba tambien se pasa
    "Such kindness… I gave him my most honest smile back. Why can’t I find people like him in my class?"

    mc "W-well, thank you. I’ll consider it. To be honest, I was a bit creeped out by this, there was this weird but smart looking professor that liked to talk a lot…"

    "???" "Oh, yes, Professor Nabradia. A bit of a peculiar guy, but he’s probably the smartest person I know."
    "???" "And the ESGARSI would not be able to exist without him! Well, I guess I gave you quite the monologue too… For all that talk I’m actually just quite new there, and not great at academic stuff either, I’m much better at the arts, so it would be great to have someone like me in there."
    #se pasa
    "???" "Oh, by the way, I haven’t introduced myself! I’m Z’enyth, a first year in Fine Arts, but you can call me Zen. We have a meeting today, so it’d be great if you could come by, it’s open to everybody, no need to commit yet!"

    mc "Thanks, I’m %(povname)s. I guess I’ll come by, but now I should be getting back to class."

    "Z’enyth’s face changed quickly once again, as if he suddenly remembered the rush he said he was in at the start, as he quickly finished picking up his books and started walking, almost running."

    zen "Yes, classes, true, gottagotooseeyouatthemeeting!"

    #FIN ESCENA 2

    #INICIO ESCENA 3

    "The remaining classes went through pretty easily too, with the biggest problem being me getting too distracted thinking about this ESGARSI thing."
    "I was lucky to have met Z’enyth, because the flyer, unlike what professor Nabradia told me, definitely didn’t have all the information I needed. Professor Nabradia… An interesting fellow, I didn’t get to ask him what he teaches."
    #Cambiar la de arriba creo 
    "Maybe I’ll get to have him in one of my subjects. Anyway, classes have ended, so I should go check out the ESGARSI’s meeting room. I’m a bit nervous."

    "As I got out of classes I headed to the Faculty of History, where their meeting room is supposed to be. It’s a big, old building, built in stone and with an air of majesty."
    "It’d certainly be nice to come to a place like this regularly without the worries I’d have if I studied here. The problem it has is that, old as it is, its corridors are labyrinthic and it’s poorly indicated where each classroom is supposed to be. It’s a bit embarrassing, but I guess I have no other option than asking someone where the meeting room is. I approached one of the students in the main corridor."
    #cambiar la de arriba
    mc "E-excuse me. Do you know where I could find this classroom…?"

    "He turned around and stared down at me. He already had a pretty scary face, but it only got worse when he saw the piece of paper I was holding."

    "Rude man" "Huh? Why would you want to go there?"

    mc "I-I’m thinking about joining, so I wanted to check them up…"

    "Rude man" "Oh, so they managed to get another one. You must not be very smart then, right? What do you plan to do then? Going to conferences to waste all of our time? *chuckle* Pathetic."

    "I didn’t know what to answer. I don’t really know anything about what they do, but this doesn’t sit right with me, that’s just not how you should treat anybody… I wanted to tell him something, but my mouth opened only for my voice to not come out."
    "Well, maybe he’s right after all, I don’t know anything about these people. I must have been fooled into joining some fishy organisation… I can’t believe I’ve been so stupid once again, why do I even keep trying? But that Z’enyth guy seemed really sweet… would he really want to swindle someone? I-I-I"
    #cambiar el de arriba
    "Rude man" "What’s the matter, cat got your tongue? Or is it that you don’t have anything good to say about your new friends, because there’s nothing? Hey, guys! A new member for that EMGARZI bullshit! Look at %(povpronoun2)s, they didn’t seem to have got a bright one this time either."
    #cambiar el de arriba
    "The few people around started staring at me, some of them chuckling. This… this can’t be ok, it doesn’t matter what kind of people they are, why should they be humiliated… And why am I the one being humiliated, I haven’t even joined, he knows, I told him."
    #cambiar el de arriba
    "I… As I was starting to tear up, I saw something approaching from the corner of my eye. It was a young, white haired man, wearing some traditional japanese-looking clothes and a huge sheath on his back. He got closer to us, and as soon as he saw me almost crying he stared angrily at the rude man."
    #cambiar el de arriba
    "???" "…"
    if genderflag == False:
        "Rude man" "What do you want? I’m just telling someone off because %(povpronoun1)s deserves it, so please, leave me alone."
    else:
        "Rude man" "What do you want? I’m just telling someone off because %(povpronoun1)s deserve it, so please, leave me alone."

    "???" "*sigh*"

    "After sighing, the white-haired man quickly opened the sheath he was carrying, dropping it as he took his weapon out, immediately striking our impolite fellow."
    "I closed my eyes, scared at how fast this escalated, and when I opened them I found that this rude guy had fallen on the ground while the white-haired man had his hand up in the air, completely empty, and started laughing."
    "Looking down, I could see that the sheath was on the floor, with a kendo sword still inside it. I had never before seen such a masterful feint pulled off in real life, and while I can’t say it was in good taste, the scare he gave him was certainly satisfying."

    "Rude man" "Y-you guys are just doing this because you aren’t able to back your ideas up with words. P-pathetic."

    "He got up on the floor and hurried away. The same people that seconds before were laughing at me were now giggling at him. The white-haired man turned around to face me, with a big smug grin. He stared at the flyer I was holding in my hands, pointed at it, then pointed at himself and gave me a thumbs up."
    #cambiar el de arriba
    mc "O-oh. Thank you so much, that guy seemed dangerous… A-are you an ESGARSI member? I was trying to look for the meeting room."

    "He nodded, pointed upwards and raised three fingers."

    mc "Huh? What does that mean, second floor class 3?"

    "After hearing my question he just shrugged and turned back, walking off to probably change back to his normal clothes. There are some weird people in this ESGARSI thing, but they all seem to be nice, I guess I’ll see him at the meeting if he truly was a member..."
    #cambiar el de arriba
    #FIN ESCENA 3

    #INICIO ESCENA 4

    # This ends the game.
    #c "%(player_name)s hijo de puta"
    return
