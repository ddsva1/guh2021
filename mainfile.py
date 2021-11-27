#global vars:
#level:0
#number of lives:1
hearts = 1
#gameover = false

#imported libraries:
#pygame?? or tkinter if need be
#
# Why u so clever?

def gameover():
    exit()

def gameovergood():
    print("You became a zombie!")
    print("You and Tom the zombie got married")
    print("You and Tom got a house on a fixed inerest mortgage rate!")
    print("You've had a child! how is that possible!?")
    print("Both you and tom have lived happily ever after")
    print("while the world decayed into ruins,")
    print("you two are still going strong")
    print("well done!")
    print("humanity lost but you two sure won!")
    print("the end")

def gameoverbad1():
    #play song - really really american one - name??
    print("wow you killed a zombie... his name was Tom")
    print("*child runs in the scene")
    print(":O")
    print('youre a murderer!')
    #zombie kid bit
    print("game over")
    gameover()

def gameoverbad2():
    print("you've been cancelled on twitter")
    print("A large karen voice")
    print("game over")
    gameover()

def gameoverbad3():
    print("Cow just killed you. Well he was holding a gun")
    print("game over")
    gameover()

def gameoverbad4():
    #No heart is left
    print("print you are eaten alive!!")
    print("At least you are tasty")
    gameover()

def level3():
    print("(You say to yourself) Oh maybe love cures zombie?")
    print("You get closer to the zombie")
    print("Bite!!")
    print("Oh nevermind zombie bit you..")
    global hearts
    if hearts <2:
        gameoverbad4()
    else:
        gameovergood()

def level2():
    global hearts
    print("Date 2")
    print("*The Second Date")
    print("You and Zombie is going to cemetery")
    print("Look!! a cow in a coat. It's holding a gun!!")
    print("It seems like you have a gun with you. What would you do?")
    print("a: shoot the cow")
    print("b: run away")
    print("c: don't shoot. It can be friendly")
    c = input("action choice:")
    if c == "a":
        hearts += 1
        print("You and the zombie is having some burgers for dinner")
    elif c =="b":
        hearts -= 1
        print("You are shot! But still got away from the nasty cow.")
    elif c == "c":
        print("The cow attacks you!")
        gameoverbad3()
    else:
        print("You did nothing")

def level1():

    global hearts
    print("Date 1")
    print("*The First Date*") #make this text big
    print("awwwww") #make this text small
    print("choose a movie")
    print("a: twilight")
    print("b: world war z")
    print("c: garfield 3 the movie")
    c = input("movie choice: ")
    if c == "a":
        print("Zombie loves this movie!")
        print("shares some of their brainy popcorn")
        print("zombie and you had a great movie date")
        hearts = hearts + 1
    elif c == "c":
        print("zombie thinks you are immature")
        print("zombie want to go over relationship boundries")
        print("zombie and you had an meh movie date")
        hearts -= 1
    elif c == "b":
        print("zombie thinks youre insensitive (yikes)")
        print("Oh No! zombie took out their phone and tweeted!")
        print("Zmobie storms out of theatre")
        print("Oh no your boss is on the phone! You've been cancelled!")
        gameoverbad2()
    else:
        print('get error checking - note')

def level0():
    global hearts
    print("There are weapons on the ground! quick choose!")
    print('a: bat')
    print("b: gun")
    print("c: crossbow")
    print("d: bare! hands!")
    print('choose an object:')
    weapon = ''
    while weapon == "" or weapon == 'a' or weapon == 'c':
        weapon = input("what do you do? ")
        if weapon == "a":
            print("You chose bat!")
            print("You ht the zombie!")
            print("boink!") #zombie is hit
            print("Didn't work... zombie is mildly annoyed")
        elif weapon == "b":
            print("You chose a gun")
            print("You shoot the zombie!")
            print("Blood is splattered!")
            print("Zombie lifeless body falls to the floor")
            hearts = 0
        elif weapon == "c":
            print("You chose a crossbow")
            print("You are inexprinced!")
            print("You shot yourself in the foot")
            print("zombie smells your blood, looks hungry")
        elif weapon == "d":
            #wow brave choice etc etc
            #write a awkard hug
            print("you're going into this empty handed")
            hearts += 1
        else:
            print("sorry try again, that wasnt one of the options?")

def decison():
    print("[boo!]")#actual jump scare noise
    print('*DANGER*')
    print('a zombie is approaching you')
    print('What do you do? press a: Fight or  b: Run')
        


def start():
    global hearts
    print("press a, b, c for each option choice")
    inp = input("press enter key to start game ")
    if inp == "":
        print(":D")
        print("the background!")
        #print stuff here - mention food supply issues?
        print('--------------------------------------------')
        #meet zombie n decide
        decison()
        dc = input
        #i just. put all the functions in for ease of testing
        level0()
        if hearts == 0:
            gameoverbad1()
        else:
            level1()
            level2()
            level3()
    else:
        print('wow')
        print("coward")
        exit()

start()

x = input("")
if input == input:
    exit()
