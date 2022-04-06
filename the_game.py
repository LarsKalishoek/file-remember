import random
import json
import os


check = ""
save = ""
score = 0


# user defined function
with open("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/highscore.json", "r") as file:
    highscore = file.read()
    highscore = json.loads(highscore)


def checkScore():
    for x in range(1, 11):
        if score > highscore[str(x)]["score"]:
            return x
    return False


def checking():
    check = checkScore()
    if check != False:
        updateHighscore(check)


def fun_intro()->bool:
    global name
    print('Welcome to THE GAME, this is a text based adventure game, where YOU are the one who makes the decisions. The objective of this game is to find out what happened to all of your stuff.')
    name = input('What is your name?  : ') 
    age = input("What is your age  : ")
    if int(age) >= 13:
        print("You can play the game")
        factuurtekst = "Hello " + str(name) + ", your choices have a huge impact on the game so be smart, enjoy. (when something is between '' please type that as your answer.)" 
        print(factuurtekst)
        doorgaan = True
    else:
        print("Stop going on the internet.")
        doorgaan = False
    return doorgaan
        

def fun_op(vraagNmr, vraag, progAntwoord):
    autosave(vraagNmr)
    print(vraag)
    global score
    opt1 = input(" {").lower()
    if opt1 == "a":
        print(progAntwoord)
        delete()
        checking()
        exit()
    elif opt1 == "b":
        score += 1
        if score == 6:
            checking()

def autosave(flag):
    flag = json.dumps(flag)
    with open("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/autosave.json", "w") as save:
        save.write(flag)

    
def updateHighscore(rank):
    global highscore
    z = 10 - rank
    s = 10
    for x in range(z):
        d = s - 1
        highscore[str(s)] = {'name': highscore[str(d)]["name"], 'score': highscore[str(d)]["score"]}
        s -= 1
    highscore[str(rank)] = {'name': str(name), 'score': score}
    with open("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/highscore.json", "w") as file:
        save = json.dumps(highscore, indent= 2)
        file.writelines(save)
    

#autosave
def saveCheck():
    path = os.path.dirname(os.path.abspath(__file__))
    return os.path.exists(path + "/autosave.json")

    
# json 

def delete():
    os.remove("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/autosave.json")


with open("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/vraagnmr.json", "r") as vragenJSON:
    vragenDict = json.load(vragenJSON)


if saveCheck() == True:
    print("Do you want to continue your last story, type Y or N" )
    check = input("{").lower()
    if check == "y":
        with open("C:/Users/larsk/OneDrive/Documenten/Projecten/file-remember/autosave.json", "r") as file:
            save1 = file.read()
            save1 = json.loads(save1)
    if check == "n":
        delete()    

    
if check == "y":
    for x in range(save1, len(vragenDict)+1):
        fun_op(x, vragenDict[str(x)]["vraag"], vragenDict[str(x)]["progAntwoord"])
    delete()


elif fun_intro():
    for (k,v) in vragenDict.items():
        fun_op(int(k), vragenDict[k]["vraag"], vragenDict[k]["progAntwoord"])
    delete()

