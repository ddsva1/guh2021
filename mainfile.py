#global vars:
#level:0
#number of lives:1
hearts = 1
#gameover = false

#imported libraries:
#pygame?? or tkinter if need be
#
# Why u so clever?

def level2():
    print("Date 1")
    print("*The First Date*") #make this text big
    print("awwwww") #make this text small
    print("Choose a movie")


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

"""
def checkhearts(x):
    if hearts == 0 and x == 1:
        print('the zombie doesnt like you and eats you.')
        print("game over")
"""
def start():
    global hearts
    hearts = 1
    print("press a, b, c for each option choice")
    inp = input("press enter key to start game ")
    if inp == "":
        print(":D")
        print("the background!")
        #print stuff here - mention food supply issues?
        print('--------------------------------------------')
        #meet zombie n decide
        print("[boo!]")#actual jump scare noise
        print('*DANGER*')
        print('a zombie is approaching you')
        print('a: bat')
        print("b: gun")
        print("c: crossbow")
        print("d: bare! hands!")
        print('choose an object:')
        weapon = ''
        weapon = input("what do you do? ")
        if weapon == "a":
            print("you chose bat!")
            #print stuff here
        elif weapon == "b":
            print("you chose a gun")
            #print stuff here
        elif weapon == "c":
            print("you chose a crossbow")
            #something something shoot foot was mentioned?
        elif weapon == "d":
            #wow brave choice etc etc
            print("you're going into this empty handed")
        else:
            print("blah")

        print("ok time to go up to the zombie")
        print('a: attack the zombie with your '+weapon)
        print('b: turn and run')
        print("c: Make Friends Like A Good Person TM")
        action = input("what do you do? ")


    else:
        print('wow')
        print("coward")
        exit()

start()
