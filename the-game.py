import random
import json
import os

save = ""

# json 
def autosave(flag):
    flag = json.dumps(flag)
    with open("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/autosave.json", "w") as save:
        save.write(flag)
        
def delete():
    os.remove("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/autosave.json")

#introduction to the game

print('Welcome to THE GAME, this is a text based adventure game, where YOU are the one who makes the decisions. The objective of this game is to find out what happened to all of your stuff.')
name = input('What is your name?  : ') 
age = input("What is your age  : ")
if int(age) >= 13:
    print("You can play the game")
if int(age) <=12:
    print("Stop going on the internet.")
    exit()
factuurtekst = "Hello " + str(name) + ", your choices have a huge impact on the game so be smart, enjoy. (when something is between '' please type that as your answer.)" 
print(factuurtekst)

#space between texts

print('')
print('')

#first choice from the player

print("The story begins here, you've just woken up in a tavern, you passed out drunk yesterday.")
print("You go to your house, all your stuff is gone, including all your furniture. ")
print("You wonder where all your stuff has gone, what do you do : 'Go look' for your stuff or 'Sleep' on the floor? (You have a 1/4096 chance to win by sleeping.)")
option1 = input("{").lower()
if option1 == 'sleep' or save == 1:
    autosave(1)
    number = random.randint(1, 4096)
    if number == 69:
        print("You got lucky, all your stuff came back, i guess it was just a dream. Goodjob")
        delete()
        exit()
    else:
        print("Did you really think  that this would work " + str(name) + ". You dumbass you died. ")
        delete()
        exit()

    #ending 

elif option1 == 'go look' or save == 2:
    print("Where do you start : 'The Tavern' or 'The Bandit Hideout'.")
    autosave(2)
    option2 = input('{').lower()

#tavern option

    if option2 == 'the tavern' or save == 3:
        autosave(3)
        print("You see a 'man' a 'woman'. Who do you talk to?")
        option3 = input("{").lower()

        #man option 

        if option3 == 'man' or save == 4:
            print("The man asks you what you want what do you answer : ")
            print("'A' Have you seen anyone with alot of furniture?")
            print("'B' Were you here yesterday night?")
            print("'C' What is your favorite drink here?")
            autosave(4)
            option4 = input('{').lower()

            if option4 == "a" or save == 5:  
                print("Yea, strangely enough i did see someone carrying alot of stuff yesterday night ")
                print("You can ask: ")
                print("'A': What did this man look like?  ")
                print("'B': Did you see where he went? ")
                autosave(5)
                option5 = input("{").lower()

                if option5 == "a" or save == 6:
                    print("The man had long hair and facial hair, he was wearing all black and he was wearing big boots")
                    print("Thank you for the info.")
                    print("What do you wanna say now?")
                    print("'A' Did you maybe see where he went")
                    print("'B' Could i get your number so i can contact u later?")
                    autosave(6)
                    option8 = input("{").lower()
                    if option8 == "a" or save == 7:
                        print("I think he went into the cave, but that could've just been me seeing things while being drunk")
                        print("You enter the cave and you see a turn do you turn 'Left' or 'Right'? ")
                        autosave(7)
                        opt2 = input("{").lower()
                        if opt2 == 'left' or save == 8:
                            print("You chose left and you see a long path down, where you see some light.")
                            print("When you're at the bottom you see someone, no something? sitting on YOUR furniture, you see it using your lamps.")
                            print("What do you do?")
                            print("'A' Go up to that thing and slap him.")
                            print("'B' Go up to it and ask it why it took YOUR stuff.")
                            autosave(8)
                            opt3 = input("{").lower()
                            if opt3 == 'a':
                                print("It looks and you and slaps you back even harder, you fall on a stone and break your neck. Try again.")
                                delete()
                                exit()
                            if opt3 == 'b' or save == 9:
                                print("It says: I'm so sorry i just needed it because i have no money and i just wanted to feel home for once. You can have your stuff back if you want.")
                                print("Do you 'Take your stuff' or do you let it 'Move in' with you?")
                                autosave(9)
                                opt4 = input("{").lower()
                                if opt4 == 'take your stuff':
                                    print("You leave the cave with all your stuff while you hear it crying from down the cave, you safely get home and you can finally watch tv again")
                                    print("You have succesfully beated The Game.")
                                    delete()
                                    #win screen

                                if opt4 == 'move in' or save == 10:
                                    print("You let it move in with you, you ask for its name, it say :'Mi neme ies Dobby.'")
                                    print("You say: 'Hi Dobby! Im glad to meet you, this is my house so please listen and respect my rules.'")
                                    print("Dobby says: 'Oka ie wiell listan. Tank u.'")                 
                                    print("After a while Dobby stops listening to you and you two get into an argument. Dobby gets mad and reaches for a knife.")
                                    print("What do you do?")
                                    print("'A' Run away.")
                                    print("'B' Try to fight Dobby.")
                                    autosave(10)
                                    opt5 = input("{").lower()
                                    if opt5 == 'a' or save == 11:
                                        print("You run away and see the 'police station' and a 'man' where do you go?")
                                        autosave(11)
                                        opt6 = input("{").lower()
                                        if opt6 == 'police station':
                                            print("You lead the police to your house and on your way there you tell them the story of what happened.")
                                            print("When you arrive at your house the police take Dobby with them.")
                                            print(str(name) + " survived the game. Great job.")
                                            delete()
                                            exit()
                                            #win screen

                                        if opt6 == 'man':
                                            print("You go up to the man but you're too late because Dobby is already behind you. It stabs you in your back and Dobby continues to live in your house")
                                            print( str(name) + " died, try again.")
                                            delete()
                                            exit()
                                    if opt5 == 'b':
                                        print("You try to fight with Dobby and it stabs you. Dobby keeps stabbing you until you die. Try again.")
                                        delete()
                                        exit()

                    if option8 == "b":
                        print("Are you dumb, you can't ask for someones number when you dont even have phones. Try again")
                        delete()
                        exit()
                        #ending

                if option5 == "b" or save == 11:
                     print("I believe he went into the cave, but i could be wrong about that.")
                     print("Do you wanna go to the 'cave' or go 'home'? ")
                     autosave(11)
                     option6 = input("{").lower()
                     if option6 == 'cave' or save == 12:
                         print("You enter the cave and you see a turn do you turn 'Left' or 'Right'? ")
                         autosave(12)
                         opt2 = input("{").lower()
                         if opt2 == 'left'or save == 13:
                             print("You chose left and you see a long path down, where you see some light.")
                             print("When you're at the bottom you see someone, no something? sitting on YOUR furniture, you see it using your lamps.")
                             print("What do you do?")
                             print("'A' Go up to that thing and slap him.")
                             print("'B' Go up to it and ask it why it took YOUR stuff.")
                             autosave(13)
                             opt3 = input("{").lower()
                             if opt3 == 'a':
                                 print("It looks and you and slaps you back even harder, you fall on a stone and break your neck. Try again.")
                                 delete()
                                 exit()
                             if opt3 == 'b' or save == 14:
                                 print("It says: I'm so sorry i just needed it because i have no money and i just wanted to feel home for once. You can have your stuff back if you want.")
                                 print("Do you 'Take your stuff' or do you let it 'Move in' with you?")
                                 autosave(14)
                                 opt4 = input("{").lower()
                                 if opt4 == 'take your stuff':
                                     print("You leave the cave with all your stuff while you hear it crying from down the cave, you safely get home and you can finally watch tv again")
                                     print("You have succesfully beated The Game.")
                                     delete()
                                     #win screen

                                                               
                                 if opt4 == 'move in' or save == 15:
                                     print("You let it move in with you, you ask for its name, it say :'Mi neme ies Dobby.'")
                                     print("You say: 'Hi Dobby! Im glad to meet you, this is my house so please listen and respect my rules.'")
                                     print("Dobby says: 'Oka ie wiell listan. Tank u.'")                 
                                     print("After a while Dobby stops listening to you and you two get into an argument. Dobby gets mad and reaches for a knife.")
                                     print("What do you do?")
                                     print("'A' Run away.")
                                     print("'B' Try to fight Dobby.")
                                     autosave(15)
                                     opt5 = input("{").lower()
                                     if opt5 == 'a' or save == 16:
                                         print("You run away and see the 'police station' and a 'man' where do you go?")
                                         autosave(16)
                                         opt6 = input("{").lower()
                                         if opt6 == 'police station':
                                             print("You lead the police to your house and on your way there you tell them the story of what happened.")
                                             print("When you arrive at your house the police take Dobby with them.")
                                             print(str(name) + " survived the game. Great job.")
                                             delete()
                                             exit()
                                             #win screen

                                         if opt6 == 'man' or save == 17:
                                             print("You go up to the man but you're too late because Dobby is already behind you. It stabs you in your back and Dobby continues to live in your house")
                                             print(str(name) + " died, try again.")
                                             autosave(17)
                                             exit()
                                     if opt5 == 'b':
                                         print(str(name) + " tried to fight with Dobby and it stabs you. Dobby keeps stabbing you until you die. Try again.")
                                         delete()
                                         exit()
                                         #ending
                         else:
                             print(str(name) + " chose right and slipped into a big hole. Try again")
                             delete()
                             exit()
                             #ending 

                     if option6 == 'home' or save == 18:
                         print("You went home and all your stuff suddenly appears, i guess it was just a bad dream? Or was something else going on.")
                         print("Do you wanna 'investigate' or just 'call it a day'")
                         autosave(18)
                         option7 = input("{").lower()
                         if option7 == 'investigate' or save == 19:
                             print("You investigate everything in your house and find nothing, you still find it weird what happened.")
                             autosave(19)
                         if option7 == 'call it a day' or save == 20:
                             print("You get tired and just want to go sleep, where do u sleep 'the couch' or 'your bed'? ")
                             autosave(20)
                             option8 = input("{").lower()
                             if option8 == 'the couch' or save == 21:
                                 print("You wake up from a strange sound, what do you do? 'Look' 'Continue sleeping'")
                                 autosave(21)
                                 option9 = input("{").lower()

                                
                                 if option9 == 'continue sleeping':
                                     print(str(name) + " wakes up because you feel someone touching you, its a person with a blade against your neck. You died, try again.")
                                     delete()  
                                     exit()

                                     #ending 

                                 if option9 == 'look' or save == 22:
                                     print("You see a weird figure standing outside. Do you go 'Look' or 'Grab a knife'")
                                     autosave(22)
                                     option10 = input("{").lower()

                                     #ending 

                                     if option10 == 'look':
                                         print("You go outside and see a man standing the man kills you. You died, try again.")
                                         delete()
                                         exit()
                                         #ending 

                                     if option10 == 'grab a knife':
                                         print("You see a HUGE man with a weapon coming towards you, what do you do 'Stab' him with the knife or 'Talk' to him")
                                         opt1 = input("{").lower()
                                         if opt1 == 'stab':
                                             print("You stabbed the man and killed him, the neighbors heard someone yelling and screaming from pain.")
                                             print("Your neighbors called the police and the police took you to a cell. You got life in prison, try again.")
                                             delete()
                                             exit()
                                             #ending 

                             if option8 == 'your bed':
                                 print("You sleep really nice and nothing happens, you wake up the next day and feel happy.")
                                 print("You won the game by being smart and sleeping in your bed :). ")
                                 delete()
                                 exit()
            if option4 == "b" or save == 23:
                print("No i was at home, i did see something strange though.")
                print("You ask the man: Could you describe what you saw yesterday?")
                print("The man answers and says: It looked like a huge man who looked very scary.")
                print("You say: Thank you for the information.")
                print("Do you:")
                print("'A' Look around for the man")
                print("'B' Go home and let it be.")
                autosave(23)
                opt3 = input("{").lower()
                if opt3 == 'a' or save == 24:
                    print("You look around in the whole city and you cant find him")
                    print("You come to an intersection do you:")
                    print("'A' Turn left")
                    print("'B' Turn right")
                    autosave(24)
                    opt4 = input("{").lower()
                    if opt4 == 'a' or save == 25:
                        print("You turn left and see your house do you:")
                        print("'A' Go to your house. ")
                        print("'B' Go straight.")
                        autosave(25)
                        opt5 = input("{").lower()
                        if opt5 == 'a':
                            print("You get home and all your stuff is back. You won The Game, good job.")
                            delete()
                            exit()
                        if opt5 == 'b':
                            print("You ran straight into the mans arms. He hugged you and then suffocated you. You died.")
                            delete()
                            exit()
                if opt3 == 'b':
                    print("You go home and think about what happened today. Suddenly you hear a loud knock on your front door.")
                    print("You go and check what it is, its ALL of your stuff right infront of your door.")
                    print("You were lucky and got all your stuff back, you beat The Game, good job.")
                    delete()
                    exit()

            if option4 == "c":
                print("What a weird question but its just the beer. Why do you wanna know")
                print("You asked the dumbest question and the game just crashed.")
                delete()
                exit()



         #woman option

        if option3 == 'woman' or save == 26:
            print('Hello there ' + str(name) + " can i help you?")
            print("'A' Did you seen anything strange yesterday")
            print("'B' *flirt* ")
            autosave(26)
            opt1 = input("{").lower()
            if opt1 == 'a' or save == 27:
                print("I did see something strange yea, i dont know how to describe what i saw though.")
                print("'A' Could you maybe try to draw what you saw yesterday?")
                print("'B' Say: Thats okay sorry for bothering. And go home.")
                autosave(27)
                opt2 = input("{").lower()
                if opt2 == 'a' or save == 28:
                    print("The woman tries her best to draw the thing she saw. From the drawing you can see someonw who looks like... like you..")
                    print("You look scared and ask her what do you mean?")
                    print("She says: It was you. YOU took all your stuff.")
                    print("What do you do:")
                    print("'A' Go back home.")
                    print("'B' Think about what happened.")
                    autosave(28)
                    op4 = input("{").lower()
                    if op4 == 'a':
                        print("You go back to your empty home. You get sad and cry. Eventually you die. Try again :( ")
                        delete()
                        exit()
                    if op4 == 'b':
                        print("You think so much that your head explodes. Try again u 5head L.")
                        delete()
                        exit()
                if opt2 == 'b':
                    print("You go home and all your stuff has returned. You think to yourself how did this happen, but you're happy everything is back. You have won the game.")
                    delete()
                    exit()
            if opt1 == 'b':
                number = random.randint(1, 3)
                if number == 1 or save == 29:
                    print("You are lucky and she flirts with you.")
                    print("Do you:")
                    print("'A' Stay in the tavern.")
                    print("'B' Take her to your house.")
                    autosave(29)
                    op1 = input("{").lower()
                    if op1 == 'a' or save == 30:
                        print("Would you like a drink? I'll pay.")
                        autosave(30)
                    if op1 == 'b' or save == 31:
                        print("You ask the lady her name while walking home.")
                        print("She says my name is Ashe.")
                        print("You say: Thats a nice name.")
                        print("You arrive at your house and she says: Where is all your stuff?")
                        print("You answer:")
                        print("'A' I just moved here.")
                        print("'B' Someone stole my all my stuff and i was trying to find it. But i'll let it be.")
                        autosave(31)
                        op2 = input("{").lower()
                        if op2 == 'a' or save == 32:
                            print("Oh well lets go to my house she says.")
                            print("You say:")
                            print("'A' Okay sounds good.")
                            print("'B' I'd rather stay here. Sorry.")
                            autosave(32)
                            op3 = input("{").lower()
                            if op3 != 'b' or save == 33:
                                print("You guys walk to her house, on your way there you think of things you two can do.")
                                print("You come up with a game with dice. You two arrive at her house and you guys look for dice.")
                                print("You guys start playing and its your turn")
                                autosave(33)
                                number1 = random.randint(1, 6)
                                if number1 < 4:
                                    print("You lost try again.")
                                    delete()
                                    exit()
                                    
                                    #ending

                                if number1 > 3:
                                    print("You won The game")
                                    print("Goodjob im proud of you, also you married Ashe and lived together with her and got kids.")
                                    delete()
                                    exit()

                                    #winscreen

                            if op3 != 'a':
                                print("Thats okay i'll leave she says.")
                                print("You lost a beautiful girl you dumbass go try again.")
                                delete()
                                exit()
                        if op2 == 'b' or save == 34:
                            print("She puts a bag over your head and takes you with her.")
                            print("She flips a coin to descide if you live or die.")
                            print("Do you choose 'Heads' or 'Tails'  : ")
                            autosave(34)
                            coin = input("{").lower()
                            if coin == 'or':
                                print("You win.")
                                delete()
                                exit()

                                #winscreen
                            else:
                                print("You lost The Game, try again " + str(name))
                                delete()
                                exit()

                                #ending
                if number == 2:
                    print("You are unlucky and she slaps you across your face and you break your neck. You died, try again.")
                    delete()
                    exit()
                if number == 3:
                    print("You are unlucky and she slaps you across your face and you break your neck. You died, try again.")
                    delete()
                    exit()

#bandit hideout option

    if option2 == 'the bandit hideout' or save == 35:
             print("You arrive at the Bandit Hideout.")
             print("You see many people who are all wearing the same outfit")
             print("What do you do:")
             print("'A' Leave.")
             print("'B' Go ask one of the people if they know anything about your furniture.")
             autosave(35)
             op1 = input("{").lower()
             if op1 == 'a':
                 print("You leave the Bandit Hideout, and when you walk outside you get robbed and stabbed. You died. Try again.")
                 delete()
                 exit()

                 #ending

             if op1 == 'b' or save == 36:
                 print("You can choose from two people who u want to ask You can choose '1' or '2'.")
                 autosave(36)
                 op2 = input("{").lower()
                 if op2 == '1' or save == 37:
                     print("The man turns around angry and he beats you up before you can even talk. The other people just look a you as if nothing is happening.")
                     print("You start seeing some light but then someone comes and saves you from those people.")
                     print("You start to feel something touching you but you dont see it, someone says CRAZY DIAMOND. ")
                     print("You are fully healed out of nowhere. You walk away from the Hideout. Where do you go?")
                     print("Go to: Your 'house' or 'Go back'")
                     autosave(37)
                     op3 = input("{").lower
                     if op3 == 'house':
                         print("You go home and all your stuff is back. I guess that guy also fixed your house.")
                         print("You got your stuff back and won the game. Good job :).")
                         delete()
                         exit()
                 def fun_op2():         
                    if op2 == '2' or save == 38:
                        print("The woman is friendly and she greets you with a lovely smile. She says : Hello how can I help you?")
                        print("You ask:")
                        print("'A' Do you know anyone who might've stolen all of my stuff?")
                        print("'B' Do you recognise me?")
                        autosave(38)
                        op3 = input("{").lower()
                    def fun_op3():
                        if op3 == 'a':
                            print("She says she doesn't know.")
                            print("You lost because I said so and I made The Game")
                            delete()
                            exit()    
                        if op3 == 'b' or save == 39:
                            print("No i do not im sorry, is something wrong?")
                            print("Yea there is, i went home this morning and all my stuff was gone. Could you help me?")
                            print("She says sure i'll help you.")
                            print("You guys go out and try to find who or what took your stuff. After some time you guys finally find something.")
                            print("Its a painting that is from your house. You keep finding more and more stuff from your house and eventually you find everything.")
                            print("You guys go back to your house and place back everything. You ask her what her name is. She says: Maria")
                            print("You say: What a lovely name. Do you two:")
                            print("'A' Say Goodbye Maria.")
                            print("'B' Ask if she would like something to drink.")
                            autosave(39)
                            op4 = input("{").lower()
                        def fun_op4():
                            if op4 == 'a':
                                print("You see Maria walking away and you go back to your house. Atleast you got your stuff back.")
                                print("You won The Game because you got your stuff back. Good job " + str(name))
                                delete()
                                exit()
                            if op4 == 'b':
                                print("Maria says: Sure why not. You two have some drinks and you guys feel happy. You're also happy because all your stuff just came back")
                                print("You win because you got your stuff and you're happy with Maria. :) ")
                                delete()
                                exit()
                                #ending

if save == 1:
