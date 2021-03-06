# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define mc = Character("[povname]", color="#ffffff")
define zach = Character("Prof. Nabradia", color="#800080")
define zen = Character("Z’enyth", color="#ff0000")
define gwyn = Character("Gwyneth", color="#ffff00")
define betnu = Character("Betnu", color="ffffff")
define eyeopen = ImageDissolve("eyesopen.jpg", 1.5, 100)
define eyeclose = ImageDissolve("eyesopen.jpg", 1.5, 100, reverse=True)
define genderflag = False
define s = "s"
define povname = ""
define povsurname = ""
# The game starts here.

label start:
    #INICIO ESCENA 1
    screen nombre():
        frame:
            xalign 0.5 ypos 50
            vbox:
                text "Enter your name"
                input default "Name":
                    value VariableInputValue("povname")
                textbutton "Continue" action Return(True)
    screen apellido():
        frame:
            xalign 0.5 ypos 50
            vbox:
                text "Enter your family name"
                input default "Last Name":
                    value VariableInputValue("povsurname")     
                textbutton "Continue" action Return(True)           
    call screen nombre() 
    call screen apellido()                 
    #$ povname = renpy.input("Your name") #Cambiar la forma de introducir el nombre
    #$ povname = povname.strip()
    #$ povsurname = renpy.input("Your surname")
    #$ povsurname = povsurname.strip()
    menu gender:
        "Choose your pronouns"
        "He/him":
            $ povpronoun1 = "he"
            $ povpronoun2 = "him"
            $ povpronoun3 = "himself"
        "She/her":
            $ povpronoun1 = "she"
            $ povpronoun2 = "her"
            $ povpronoun3 = "herself"
        "They/them":
            $ povpronoun1 = "they"
            $ povpronoun2 = "them"
            $ povpronoun3 = "themselves"
            $ s = ""
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
    "Well done, %(povsurname)s. As if you could afford it."
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
    "Professor" "If you’re unable to do anything well then I think you’d better not be coming back."
    "Professor" "It’s ok not to be competent, just go do something else that fits you better instead of wasting both your and our time in here. Let the people who really want to learn do their job."
    "Each one of his words felt like a dagger in my back."
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
    show bg tablondeanuncios with fade
    "I gathered all my courage and finally decided to go back to class."
    #ejemplo texto que se sale fuera
    "Since it was the second week of the semester and I ran away in the middle of the first one it was quite hard to keep up, but putting up all my attentional abilities the first classes of the morning were finished before I had time to realise it. After all, I’ll have to redo the first semester again next year, so my priority right now isn’t to do academically well, but trying to keep up with the pace and getting myself in a good position. And speaking of that, I should really do something about my social relationships. There’s no way I can keep this up for four years just by myself."
    mc "Ugggggh…"
    "I’ve neglected my social abilities for so long… Where do I even start? How do people even meet each other? Maybe joining a club would be my best option…"
    
    "I headed towards the bulletin board in the middle of the hallway."
    "I never bothered giving it a look before, and all my expectations of silly, amateur flyers were shattered by the incredibly colourful, professional-looking designs that decorated the board."
    
    "Huh… The sport teams are way too intense for me, and at this point their level is incredibly high…"
    "Maybe I should go for something calmer, that lets me talk to people more easily, like the literature club or…"

    "???" "What are you looking for?"

    "I heard a deep, soothing voice talking behind me."
    "It took me a few seconds to realise the question was directed to me."
    "I turned around and saw a tall, long-haired man. Just by his face I wouldn’t say he was that much older than me, he looked just like one of the senior students. His clothes, however, were too stereotypically professorish for a student to wear."
    show zac
    mc "O-oh, I was just looking at the clubs. I know it’s a bit late, but it would be nice to find some place to fit in, any interesting club could do…"

    "???" "Any could do? Non non non non non. You got it all wrong."
    "???" "Do you really want a place to fit in? Do you honestly think any place “could do”? You don’t just fit in any place you shove your head into!"
    "???" "If you want to succeed you can’t expect to keep a passive attitude! Fitting in… Creating bonds… It is all about passion!"
    "???" "You need to find something you’re passionate about! A place where you and your comrades share that same fire, where you pour all of your energies. It is under that shared passion that bonds are created!" #si la sumaba a la de arriba quedaba raro

    "I didn’t know how to react. Either this man had reached the truth of the universe or he was completely full of bullshit."
    "Whatever it was, he said all that with such confidence it was very hard not to think it was sincere."
    show zac at left
    show zac at center
    mc "S-so what do you recommend me…?"
    "???" "Ideally, you should be the one to find your own passion and pursue it, but if you really are so lost let me light the way up for you. This one!" #Igual separar el this is the one

    "He pointed at the corner of the bulletin board, where a cute hand-drawn flyer, much humbler than the other ones, laid without calling anyone’s attention."
    "It had the word “ESGARSI” written on it, and by its design it wasn’t clear at all what it was all about."

    "???" "In this world we live in, we have developed so many fields of study, of knowledge, of entertainment… There are so many things that can be the focus of our passion, but maybe because of that same reason, it can be so hard to decide for just one."
    "???" "However, there’s a single aspect that has been able to fire up young blood throughout all of history."
    "???" "Rebellion! When we see power being abused, when we see suffering and injustice… we want to act against it!"
    "???" "And this is no different in the academic world. A lot of professors, now sitting comfortably in their positions of power would rather keep knowledge stale than questioning the old knowledge, so clearly outdated." 
    "???" "And we, as people of truth have a duty to fight against that."
    "???" "It’s the way of nature! And that is what the ESGARSI strives for. Dedicated not to any single field, but for the advancement of all knowledge, there’s no better place for a lost student to awaken their passion."

    "W-what was that? Anyway, it sounds way too academic for me, I don’t think I’m that smart… But it may be an easy way to talk to new people."

    mc "T-thank you, sir, I-"
    zach "Oh, please, don’t call me sir, my name is Zach. Zach Nabradia. But I’d rather have you refer to me as Professor Nabradia, PhD."
    mc "O-ok, thank you, Professor Nabradia, I-"
    zach "PhD."
    mc "Yes, sorry. Professor Nabradia, PhD. I’ll take it into consideration, but if you excuse me I should start going to my next class."
    zach "Of course. Take this with you, it will tell you all the information you’ll need."
    show zac at right
    "He looked into his pocket and took out a completely wrinkled piece of paper. It was another copy of the ESGARSI flyer, also hand-drawn."
    "It seemed a bit disrespectful to whomever drew it, but saying anything about it would probably only get me another long monologue, so I let it be. I took it with me and headed to my next class."
    hide zac
  
    "While walking, I couldn’t help but keep staring at that piece of paper."
    "While amateurish and inconspicuous when compared to the ones that filled the board, it certainly had a unique charm that you could only appreciate when looking at it closely."
    "It felt… I know it’s weird for me to say this about a piece of paper, but in some way it felt like home. Whatever the reason, looking at it just made me smile." 
    "It feels like it could be a warm place to join, but Professor Nabradia’s talk about academicism… I’ve just come back and my grades have never been something to brag about."
    "I should do as I said and aim lower. %(povname)s, don’t go getting your hopes up all by yourself…"
    
    "*THUMP*"#sfx aqui obvio
    show zen at right with vpunch
    "I bumped into someone, making both of us drop everything we were carrying. I was so busy looking at this dumb scrap of paper, thinking about what-ifs and what-nots… Why do I have to be so embarrassing, stupid stupid stupid stupiiiiiiiid."
    "I slowly opened my eyes, ready to face the consequences. In front of me, a catboy was kneeling on the ground, hurriedly picking his books up."
    "His kind face and his hair, all tied up, made him look so soft that I could only feel worse for having inconvenienced such a person. Before I could say anything, he noticed the flyer I just dropped and suddenly started staring at me, his eyes shining."
    
    "???" "Have you just…?"

    mc "Y-yes! I have just b-bumped into you, I’m so sorry! Please let me finish picking up your stuff, it’s the least thing I can d-"
    show zen at center
    "He looked at me with a confused innocent face, as if he had no idea what I was talking about."

    "???" "Huh? But it was me who wasn’t paying attention! When I’m in a rush I always get this tunnel vision and just can’t notice my surroundings. Anyway, that’s not important. This flyer… Are you thinking about joining the ESGARSI?"

    mc "Uh… I, I don’t know. This flyer kind of makes me think this is the place I was looking for, but…"

    "???" "Really? You like it? I made it myself!"

    "His smile when he said that was so bright I couldn’t help but blush."

    mc "It’s great! I love it! But other than that it feels like a too formal club, I don’t think I’m smart enough for it…"

    "???" "No! Don’t say that! It is true that the boss takes it very seriously and is always thinking about academic stuff, but she never forces anyone to be as involved if they don’t want to."
    "???" "Just the opposite, everybody is really nice there, and there’s nobody who isn’t smart enough to join us!"
    "???" "That’s our thing! There’s so many people in uni trying to discourage people, telling them they are not worth enough… And that’s not true! We help give people the small push they need to really start thinking. So, please, don’t dare call yourself stupid!"

    "Such kindness… I gave him my most honest smile back. Why can’t I find people like him in my class?"

    mc "W-well, thank you. I’ll consider it. To be honest, I was a bit creeped out by this... There was this weird but smart looking professor that liked to talk a lot…"

    "???" "Oh, yes, Professor Nabradia. A bit of a peculiar guy, but he’s probably the smartest person I know."
    "???" "And the ESGARSI would not be able to exist without him! Well, I guess I gave you quite the monologue too…"
    "???" "For all that talk I’m actually just quite new there, and not great at academic stuff either, I’m much better at the arts, so it would be great to have someone like me in there."
    
    "???" "Oh, by the way, I haven’t introduced myself! I’m Z’enyth, a first year in Fine Arts, majoring in music, but you can call me Zen."
    "???" "We have a meeting today, so it’d be great if you could come by, it’s open to everybody, no need to commit yet!"

    mc "Thanks, I’m %(povname)s. I guess I’ll come by, but now I should be getting back to class."

    "Z’enyth’s face changed quickly once again, as if he suddenly remembered the rush he said he was in at the start, as he quickly finished picking up his books and started walking, almost running."
    hide zen with moveoutright
    zen "Yes, classes, true, gottagotooseeyouatthemeeting!"

    #FIN ESCENA 2

    #INICIO ESCENA 3

    "The remaining classes went through pretty easily too, with the biggest problem being me getting too distracted thinking about this ESGARSI thing."
    "I was lucky to have met Z’enyth, because the flyer, unlike what professor Nabradia told me, definitely didn’t have all the information I needed."
    "Professor Nabradia… An interesting fellow, I didn’t get to ask him what he teaches."
   
    "Maybe I’ll get to have him in one of my subjects. Anyway, classes have ended, so I should go check out the ESGARSI’s meeting room. I’m a bit nervous."

    "As I got out of classes I headed to the Faculty of History, where their meeting room is supposed to be. It’s a big, old building, built in stone and with an air of majesty."
    "It’d certainly be nice to come to a place like this regularly, without the worries I’d have if I studied here. The problem is that old as it is, its corridors are labyrinthic and poorly indicated."
    "It’s a bit embarrassing, but I guess I have no other option than asking someone where the meeting room is. I approached one of the students in the main corridor."

    mc "E-excuse me. Do you know where I could find this classroom…?"

    "He turned around and stared down at me. He already had a pretty scary face, but it only got worse when he saw the piece of paper I was holding."
    show rudeman
    "Rude man" "Huh? Why would you want to go there?"

    mc "I-I’m thinking about joining, so I wanted to check them up…"

    "Rude man" "Oh, so they managed to get another one. You must not be very smart then, right? What do you plan to do then? Going to conferences to waste all of our time? Hah, pathetic."

    "I didn’t know what to answer. I don’t really know anything about what they do, but this doesn’t sit right with me, that’s just not how you should treat anybody… I wanted to tell him something, but my mouth opened only for my voice not to come out."
    "Well, maybe he’s right after all, I don’t know anything about these people. I must have been fooled into joining some fishy organisation…"
    "I can’t believe that, once again, I’ve been so stupid. Why do I even keep trying? But that Z’enyth guy seemed really sweet… would he really want to swindle someone? I-I-I"
   
    "Rude man" "What’s the matter, cat got your tongue? Or is it that you don’t have anything good to say about your new friends, because there’s nothing?"
    "Rude man" "Hey, guys! A new member for that EMGARZI bullshit! Look at %(povpronoun2)s, they didn’t seem to have got a bright one this time either."
    
    "The few people around started staring at me, some of them chuckling."
    "This… this can’t be ok, it doesn’t matter what kind of people they are, why should they be humiliated… And why am I the one being humiliated, I haven’t even joined, he knows, I told him."
    
    "I… As I was starting to tear up, I saw something approaching from the corner of my eye. It was a young, white haired man, wearing some traditional japanese-looking clothes and a huge sheath on his back."
    "He got closer to us, and as soon as he saw me almost crying he stared angrily at the rude man."
    
    show betnu angry at left
    "???" "…"
    #if genderflag == False:
    "Rude man" "What do you want? I’m just telling someone off because %(povpronoun1)s deserve%(s)s it, so please, leave me alone."
    #else:
        #"Rude man" "What do you want? I’m just telling someone off because %(povpronoun1)s deserve it, so please, leave me alone."

    "???" "{i}*sigh*{/i}"
    show bg tableros with vpunch
    "After sighing, the white-haired man quickly opened the sheath he was carrying, dropping it as he took his weapon out, immediately striking our impolite fellow."
    "I closed my eyes, scared at how fast this escalated, and when I opened them I found that this rude guy had fallen on the ground while the white-haired man had his hand up in the air, completely empty, and started laughing."
    "Looking down, I could see that the sheath was on the floor, with a kendo sword still inside it. I had never before seen such a masterful feint pulled off in real life, and while I can’t say it was in good taste, the scare he gave him was certainly satisfying."

    "Rude man" "Y-you guys are just doing this because you aren’t able to back your ideas up with words. P-pathetic."
    hide rudeman with moveoutright
    "He got up on the floor and hurried away. The same people that seconds before were laughing at me were now giggling at him."
    "The white-haired man turned around to face me, with a big smug grin. He stared at the flyer I was holding in my hands, pointed at it, then pointed at himself and gave me a thumbs up."
    
    mc "O-oh. Thank you so much, that guy seemed dangerous… A-are you an ESGARSI member? I was looking for the meeting room."
    show betnu happy at center
    "He nodded, pointed upwards and raised three fingers."

    mc "Huh? What does that mean, second floor class 3?"

    "After hearing my question he just shrugged and turned back, walking off to probably change back to his normal clothes."
    "There are some weird people in this ESGARSI thing, but they all seem to be nice. I guess I’ll see him at the meeting if he truly was a member..."
    hide betnu moveoutright
   
    #FIN ESCENA 3

    #INICIO ESCENA 4
    show bg base
    "Following that guy’s instructions I was able to find the meeting room. The door was half open, leading into a pretty small classroom, fitting for the renown they seem to have."
    "And in front of the window there was a young woman, neatly dressed in a suit and vest. She couldn’t be more than three years older than me, but she had an air of much more importance than I would ever have."
    "This must surely be the person Z’enyth referred to as “boss”."
    show gwyn 
    mc "H-hello? T-this is the ESGARSI meeting room, right?"

    "She turned around as she heard my voice and stared down on me with the most terribly stern eyes I had ever seen."
    show gwyn angry
    "Boss" "Yes, it is. And be welcome to join me in discussion, be it slander or mockery. I’ll take you on with more dignity than you could ever muster."

    "I gulped down. This day had started so well, why do I have to keep finding myself in situations like this?"

    mc "I-I’m so sorry, I didn’t want to offend you, I just saw the flyer earlier today, and met some of the members an-and thought I could come to the meeting, b-but I didn’t know I’d be such an inconvenience I’m so sorryyyyyyyyyyy"

    "I gave my deepest bow of apology, almost starting to shake. You idiot, how many times can you screw up in a day?" 
    "However, when I said that her face immediately softened, and the stern stare she wore became one of regret."
    show gwyn
    "Boss" "Oh no, no, no, no, no. I’m sorry, I’m the one that’s sorry. We’re just used to getting people with not so nice intentions."
    "But oh, please, don’t get scared, it’s usually a pretty nice place, it’s just that there’s rude people everywhere, right? But we would love to have you with us!"
    
    "She gave me quite an awkward smile, realising her mistake and not really knowing how to get out of the situation. After all the accumulated tension from today I couldn’t help but chuckle."

    mc "It’s fine, it’s fine. There was a lot happening today, but I met that Professor Nabradia guy, Z’enyth, and a white haired kendo club member that I think is also a member here, and they all seemed nice."

    "Boss" "They all seemed nice? Even…? Nevermind, I’m glad you had a good impression. That’s actually all of us, the three official members: Z’enyth, Betnu, and me, Gwyneth Purrsen. And of course, Zach, our… {i}benefactor{/i}."

    "She said that last word under her breath, clenching her teeth."    

    gwyn "So please, stay during our meeting and seriously consider joining. I’m being completely honest when I say we’d love to have you here."

    mc "Yes, I want to be at the meeting, but honestly, I…"

    "My voice started breaking a bit. She looks like a smart person, really invested in her club, and I… Well, there’s no way of denying the truth."

    mc "I’m not very smart, and academically… I had a very rough start, almost dropped out. I’m constantly being told by the teachers that I’m not going to achieve anything at this rate… I don’t think I would be of much help to a place like this…"

    "Gwyneth gave me a stern look again, but this time she wasn’t looking down on me. She was serious, even angry, but not the kind of anger directed at me."
    
    gwyn "Do you know what we do here? We talk about things that are considered to be the truth. Immutable, unshakable. The pillars of knowledge everything rests on. And we try to deny them."
    gwyn "But don’t get it wrong, it isn’t a mere exercise of denial, but a struggle against power. "
    gwyn "We take the truths that people in power have built their castles on, where they rest, unmovable, rejecting any discussion so they can comfortably keep their positions, not letting knowledge advance, and we take those truths down." 
    gwyn "It’s only when discussion is truly open for everybody to participate in that knowledge will truly advance."
    "And not only knowledge. It is our dream to level it down so the elitism and mysticism of academia disappears, to make people realise that everybody can think, everybody can have good ideas."
    
    "She looked at me dead in the eye and smirked." 

    gwyn "Do you know why some professors have been questioning your worth instead of helping you and boosting your confidence?" 
    gwyn "It’s all for the same reason. You can only be on top when you have people below you. They call themselves an elite, but are just a bunch of bullies."
    gwyn "And I can assure you, you’re not dumb, you’re not stupid, you just haven’t been taught in the proper way, because that wouldn’t be good for them. But we’ll accept your opinions here." 
    #cambiar la de arriba
    gwyn "Your alleged inferiority is the fake truth they build their thrones on. And that’s the kind of fake truth we are ready to take down at any moment!"

    "As she said this, she seemed so bright, so dazzling… And not only her. Z’enyth, who offered me his kindness. Betnu, who came to help me even before realising the fight was about the ESGARSI."
    "I know I won’t be of much help, but… Maybe I can change. That’s the reason I came back, isn’t it? This is the place I want to be in."
    "A tear fell off my cheek, this time a happy one. I don’t even need the meeting, I want to join!"

    "While I was thinking this, someone knocked on the half open door, showing his face with an apologetic look."
    show zen at left
    zen "Sorry, I’m late! I was a bit busy and got distracted… Oh! I see %(povname)s is here! Are you joining us then?"

    "I nodded."
    show betnu at right
    "Betnu came in after him. The meeting wasn’t much of a meeting, they just wanted to know me a little better, and also talked about themselves and what they do. And when I say they, I mean Z’enyth and Gwyneth, as Betnu just stayed quiet, smiling."
    "I think he might be unable to speak. We just had a nice talk and then left, planning to also meet on another day. Guess that makes me an official member now. I wonder what will happen from now on, but for the first time in so long, I had hope."

    #FIN ESCENA 4

    #INICIO ESCENA 5

    "It’s been a week since I’ve joined the ESGARSI. With everybody’s schedules being so busy, we haven’t been able to meet again, but today is finally the day!" 
    "Classes aren’t going great, I’m still lost over quite a few things, but it’s become more bearable. And the feelings of expectation for today have certainly helped make it so."
    "With that said, my last class for the day just finished, so it’s time to get to the club!"
    "Excited, I hurried to the Faculty of History. There are voices coming from the inside, so I guess everybody got here faster than me."
    "As soon as I opened the door, I was greeted by some silly discussion, which seemed to be giving poor Z’enyth a bit of distress."
    show gwyn at right
    show zen at left
    gwyn "And what if the Moon isn’t real?"
    zen "W-whaaat? How could the Moon not be real? It’s always up there!"
    gwyn "Just a hologram."

    zen "Just a-? No, no, no, I don’t think that’s right. We got up there, after all! Well, not we as in *us*, I meant we as in, you know…"

    gwyn "Those pictures were also a hologram."

    zen "Ok that’s some conspiracy talk you’re doing right now, I’m not falling for that."
    show gwyn solemne at right
    gwyn "Ah, I see, you call it a conspiracy and expect to just close the conversation like that, no proof given."
    gwyn "That’s some really cheap strategy, Zen."
    gwyn "To think you would stoop so low… It’s really easy to accept everything you’ve been told, without putting any thought into it, but at the moment of truth you realise you don’t actually have any arguments, and have no choice but to resort to telling empty words."
    zen "I… uh, I never thought about it like that. You’re right, I haven’t been thinking. And there’s a lot of weird things about the Moon, so maybe…"

    "Quicker than my eyes could say, Zen received a flick on the forehead."

    zen "Aw!"
    show gwyn smirk at right
    gwyn "Bad thinking there, Zen."
    zen "Why was it exactly this time? I thought all that about the Moon was… not true, at least, but your talk after that…"
    gwyn "No, that was all bullshit."
    zen "Everything? Even the…"
    gwyn "Everything. Utter, complete rubbish, from start to finish. And what’s worse, you were completely aware, at least at the start. You are just too weak to pressure, Zen, need to work on that. And now, the next question: Is gravity real?"
    "An eraser flew across the room, until it hit Gwyneth’s head. I looked to the direction it came from, and I found Betnu smiling confidently."
    show betnu smirk at center
    betnu "…"
    "Gwyneth was wincing slightly because of the hit, but she seemed to have taken the joke well, since she was laughing."
    gwyn "Ok, ok, I concede that one. That was a painfully convincing argument."
    "At this moment, she turned towards the door, seeing me standing there."
    hide betnu
    gwyn "Oh, %(povname)s, how long have you been waiting there? We were so engrossed in our dumb game we didn’t notice you were, I’m so sorry. But still, next time just tell us, you don’t need to act shy with us."
    mc "Oh, no. I was interested in the conversation myself, it looked like it would be a pity to interrupt. But I-I’ll take that into consideration, thank you. But, huh, what- what were you doing?"
    gwyn "I thought we could just take it easy today, so we’re playing some silly games that let our reasoning skills not get rusted. Right now, I was doing my best to try and deny things that very obviously exist while the other two tried to counter-argument. Do you want to try? For example… hm.... Betnu doesn’t exist!"
    "I quickly looked behind me, where Betnu was supposed to be. There was nothing over there. I guess he must have moved quickly… I turned around quickly, looking all over the small room, but there was nothing. Oh no, it can’t be… or can it?"
    menu:
        "Betnu does not exist!":
            $ flag_betnuexiste = "a"
        "P-please, don’t try to fool me":
            $ flag_betnuexiste = "b"
            jump betnuexiste1
#DecA.betnuexist

    "I looked at Gwyneth with horror. It was the only explanation"
    mc "H-have I just been hallucinating…? Betnu truly does not exist!"
    jump comun1
#DecB.fool
    label betnuexiste1:
    "No, of course it can’t. I’m sure he’s just hiding somewhere…"
    mc "P-please, don’t try to fool me."
    show gwyn smirk at right
    gwyn "Oh, good, I like that. But if you are trying to defy me, you better give me some proof."
    mc "I d-don’t have any…"
#comun
    label comun1:
    "This time it was me who got a flick on the forehead. Even though it was quick and precise, it was actually completely harmless."
    gwyn "Bad thinking. Come on, give me a more proper answer, where could he be?"
    mc "I-I have no idea… he’s just gone! And the door is closed!"
    "Gwyneth sighed and pointed towards the table."
    gwyn "Isn’t it obvious? He…"
    zen "Became the table!"
    if flag_betnuexiste == "b" :
        jump betnuexiste2
#DecA.betnuexist
    "As soon as Z’enyth said those words Betnu quickly jumped from below the table, trying to put on a scary face, just before bursting into laughter."
    show betnu scary face at center
    show betnu laugh at center
    betnu "…"
    "Gwyneth and Z’enyth were laughing too. It felt a bit embarrassing, but they seemed to be having fun so it was ok, especially Betnu."
    "But, even though Gwyneth was laughing it looked like she would have wanted me to figure it out, even if it was a dumb joke. While I was thinking that, Betnu, who still hadn’t completely stopped laughing, even when the others already did, gave me a thumbs up."
    betnu "…"
    "Well, he sure looks happy to have pulled it off, so I guess it’s fine."
    jump comun2
#DecB.fool
    label betnuexiste2:
    mc "No he didn’t!"
    "When Gwyneth pointed towards the table, I finally realised it, his shoes were showing below the table."
    mc "He’s just under the table, you can see his shoes if you pay attention. But he’s really good at hiding, I would never have found him by myself…"
    show betnu dissapointed at center
    "When I said that, Betnu slowly came out of his hiding spot. He seemed really disappointed, I bet he was really looking forward to pulling it off. And it was so close too…"
    gwyn "That was a pretty good attitude to start with, but you need to polish it a lot more. And that’s what we’re here for."
    "Ahhhhh, I was so close. But still, she liked it, I’m starting to feel a bit better, even if it was all pretty silly. Poor Betnu, however… I’m kinda feeling bad, if I had known he wanted to pull this off so much I may have played along with him."
#comun
    label comun2:
    gwyn "Well, I’ve been doing this for too long, now please, it’s time for someone else to take the lead. Come on, Zen, make a proposal and have us refute it."
    zen "Hm… what can I say, what can I say…"
    "He seems to be taking a lot of time thinking, maybe he’s not too good at this, or doesn’t fare too well under pressure."
    zen "Ah! I know! I don’t think the concept of language as we understand it today has a solid ontological basis. Understanding a language as a single structured unity mutable only under normative changes is nothing but an open pathway for linguistic colonialism."
    gwyn "…"
    betnu "…"
    mc "…"
    gwyn "That was… pretty smart, actually. I was thinking of this exercise to be more like a game, but now that you talk about that I’m currently working on a very similar proposition th-"
    show zen grin at left
    zen "I know! I read it when you left your notes here, it’s pretty interesting!"
    "Gwyneth let out a big sigh."
    gwyn "Fine, fine, I’ll let it slide for now, but next time come up with your own."
    zen "You know I’m much better at practical stuff… But I’ll try to do my best! Oh, yeah, I’ve been thinking about how music genres have changed so much and have so many different ramifications and subdivisions that the concept of genres is kinda losing its meaning, maybe you could help me write something about that?"
    gwyn "Sure! I’ll be checking for free time in my schedule and I’ll let you know when I have some time. That’s actually pretty interesting and connects with a theory that…"
    show betnu shrug at center
    "While the two of them kept talking about that, Betnu, who was apparently understanding as little as me about the conversation, looked at me and shrugged."
    show betnu at center
    betnu "…"
    "I couldn’t help but chuckle. I’m not sure about whatever we are doing here, but they seem to be fun people."
    gwyn "Oh, sorry, we got a bit carried away here. So, %(povname)s, what do you think of how we work here?"
    "Of how they work here? She means those silly games? Well, actually…"
    menu:
        "I don't think these games are of much help...":
            $ flag_juego = "a"
        "I really like learning new things!":
            $ flag_juego = "b"
            jump juegob
        "I may not get much, but I’m having a lot of fun!":
            $ flag_juego = "c"
            jump juegoc

#DecA.dumbgames
    mc "Well… I-I don’t think these games are actually of much help. I-I mean, it s-sure is fun, but… If we want to learn how to argue, shouldn’t we learn more proper things?"
    "Gwyneth smirked as soon as she heard me complain."
    gwyn "Oh, we got a defiant one, huh. I like it."
    gwyn "I am, however, hoping to change your mind. Why must academic things always be so serious and self-important? Is having fun not allowed?"
    gwyn "Of course, doing proper research and putting up some good amounts of studying is important, but I think it’s equally important to be able to take things lightly. To see that what we are doing isn’t all that serious as people make it to be. A lot of academic talks are actually just like these games, including the ones I love so much. Just a bunch of people just talking bullshit, trying to feel important. Only difference is that we aren’t allowed to have a laugh in those."
    "Is that so? I’ve always seen my studies as something incredibly serious, and the professors certainly seem to take it that way too… The professors… Maybe they are not the best example, at least not the one I want to follow. Maybe she’s right after all, I just should relax more."
    jump comun3
#DecB.lovelearning
    label juegob:
    mc "T-there’s still a lot of things I don’t get, but I really enjoy learning new things!"
    zen "I know, right? I also have trouble trying to understand what the boss and Professor Nabradia talk about sometimes, but that feeling of finally getting something… It’s just the best!"
    "When he puts it like that, and with such a bright smile, you just can’t avoid getting confident. I wonder if I’ll be able to have an attitude like that too."
    gwyn "I’m glad you’re enjoying it. These games are really fun and even if they don’t look like it they help improve our communication abilities. But please, don’t forget that doing proper research and studying are equally important. And also, if you ever feel stressed by complicated-sounding academic talk, don’t forget that it’s actually very similar to games like this. The things Zen and I were talking about seemed complicated and important, and so do the big talks and conferences professors give."
    gwyn "But in the end, we’re all just a bunch of idiots talking bullshit, trying to feel important."

    "Is that so? Maybe looking at it like that things aren’t as intimidating as I thought. And even Z’enyth, who looks pretty competent, has his fair share of trouble too… I still have trouble with a lot of things, but I feel like I can do this!"
    jump comun3
#DecC.gamesbefun
    label juegoc:
    mc "I-I’m barely understanding anything, but it just looks like a lot of fun!"
    "Betnu poked my shoulder, and when I looked at him he gave me a thumbs up, smiling."
    betnu "…"
    "I replied with just a nod, also smiling. He seems to be such a fun, easygoing person… How does it feel to be so free, doing whatever you enjoy, having no fear or shame? I’m a bit jealous, but when I’m here, I feel like I can do more than usual. Maybe I can change too."
    gwyn "Yes, playing these games can be a lot of fun, but please, and I say this to both of you, don’t neglect your studies. There’s a lot of things that change when we change our perspective of it. For example, academic talks and conferences seem really intimidating, with people saying big words and feeling oh-so-important. But the truth is, those things are just like these games, including all those complicated things Zen and I were talking about before. Just a bunch of idiots talking bullshit just to feel more important. If you understand the rules of the game and learn a few words, everybody can play too."
    "I see… I just have to look at academic stuff the same way I look at these games? I’m sure that won’t make the actual studying easier, but it can give me some motivation. I want to participate in this with everybody after all! Yes, I’ll just keep trying my best!"

#comun
    label comun3:
    zen "Changing the topic, having new members feel so nice, everything is so lively now. Thanks for joining us, %(povname)s!"
    "Aw, he’s making me blush. Heh heh, I know it just means that he likes to be around people, nos specifically me, but still, it’s nice to feel welcome for once."
    mc "Y-yeah, it would be nice if we could gather more people…"
    zen "Yes! It’s something I never really thought about, but it would be nice. Problem is, we don’t exactly have the best reputation as of now… I wonder if there was something we could do to make people interested."
    gwyn "Oh, I know! We could have Zen end all his sentences with nya! People seem to be really into that lately."
    "Z’enyth ending his phrases with nya… That would certainly be interesting."
    zen "What? Why would I do that? That would just be embarrassing, in any case people would run away from our club even more than they do now!"
    gwyn "Are you sure it’s not just you who’s running away? From your destiny, that is."
    zen "I am fairly sure! Don’t try to turn this around with your over-dramatic words, I’m not doing it!"
    betnu "Nya, nya, nya, nya, nya!"
    "Huh? What was that? Can he talk after all? Maybe he’s just able to repeat easy sounds, but has trouble making sentences… In any case, I need to position myself. Having him say nya is very interesting, but… is it really ok to pressure him into that?"
    menu:
        "Nya, nya, nya, nya, nya!":
            $ flag_nya = "a"
        "Please, don’t bully him!":
            $ flag_nya = "b"
            jump nya

#DecA.nya

    "No, I have to follow my feelings. Following Betnu is the correct decision here!"
    mc "Nya, nya, nya, nya, nya!"
    "Z’enyth looked a bit frustrated, but… Not in an actually angry way? I’m sure he actually wants to say it…"
    zen "I-I’m not doing it."
    gwyn "Awwww, come onnnn, are you too serious and formal to do it, nya? Are you too old for these things, you university guy, nya?"
    betnu "…"
    betnu "…"
    betnu "… nya"
    mc "C-come on, do it, nya, nya!"
    "He looked like he couldn’t hold it in anymore. We got him through the breaking point!"
    zen "I would never say that, nya!"
    "A few seconds after saying it, his face changed to a shocked expression. Did he say it without realising? But after seeing everyone’s friendly smiles, with no sign of mockery anymore, and after making sure he hadn’t died for saying nya, he changed back to a smile."
    zen "I don’t really think doing this will attract any member, nya!"
    gwyn "Ehhhh? But it’s so cute, nya!"
    zen "And if it did, I’m not sure we would want them in, nya!"
    "At this point, we just burst out in laughter. We may not be doing real club stuff, but being here is so nice..."
    jump comun4
#DecB.protecc
    label nya:
    "Z’enyth has always been so nice to me, it’s time to repay it!"
    mc "P-please, stop with the bullying! Don’t you see he doesn’t want to say it?"
    zen "T-thank you, we are lucky to have someone sensible here…"
    "He looked down as he said that. Those may have been those words, but he looked disappointed. Could it be… he actually wanted to say that but was just too embarrassed? There was an awkward silence after that. Looking tired of it, Gwyneth put her hand under her own chin, as if she was trying to look interesting, and got close to Z’enyth, moving her arm around his shoulder."
    gwyn "Ah, you’re right, it was wrong of us to try and force you, Zen-nya… After all, no member of this prestigious organisation would stoop to that point, nya."
    "Betnu, while nodding, also started grabbing his chin, while putting the other arm around his friend’s shoulder."
    betnu "..."
    betnu "…"
    betnu "… nya."
    zen "G-geez! Stop with that, I’m nyat saying that!"
    "Betnu and Gwyneth immediately grinned after hearing that. I couldn’t hold back a giggle either. He looks so embarrassed, but I guess he actually did want to say that."
#comun
    label comun4:
    "After this bout of silliness, Gwyneth looked at the clock and called our attention to it. Time really had passed faster than I thought."
    gwyn "Oh, look at the time! Ah… it’s so late, I’m going to have to call it a day. Well, I really enjoyed today’s meeting, if we can call it that. %(povname)s, I hope you had fun too!"
    mc "I-I did, thank you! Will we be meeting next week at the same time?"
    gwyn "Oh, I almost forgot! There’s a festival in town next week, so we could all go together as next week’s club activity."
    "I’m not sure going out for fun counts as a club activity, but I’m also not sure I care."
    mc "Sure! It sounds fun!"
    zen "Yes, it’s been so long since we did anything together, and it can serve as a celebration for our new member!"
    betnu "…"
    gwyn "In that case, see you then!"
    "And just like that, the day ended. I… I’ve been invited. To go out. With friends. Not exactly friends. I’m still just a newcomer from their club. But still. Invited. They could have gone by themselves as friends. But I’m invited. %(povname)s, today’s been a victory for you! My new university life is just getting better!"

    # This ends the game.
    #c "%(povname)s hijo de puta"
    return
