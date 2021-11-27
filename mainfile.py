#global vars:
#level:0
#number of lives:1
hearts = 1
#gameover = false

#imported libraries:
#pygame?? or tkinter if need be
#
# Why u so clever?

def level1():
    print("Date 1")
    print("*The First Date*") #make this text big
    print("awwwww") #make this text small 

def gameovergood():
    print("You became a zombie!")
    print("You and Tom the zombie got married")
    print("You and Tom got a house on a fixed inerest mortgage rate!")
    print("You've had a child! how is that possible!?")
    print("Both you and tom have lived happily ever after")
    print("the end")
    print("you became a zombie!")
    print("while the world decayed into ruins,")
    print("are still going strong")
    print("well done!")
    print("humanity lost but you two sure won!")

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
    print("press a, b, c for each option choice")
    inp = input("press enter key to start game ")
    if inp == "":
        print(":D")
        print('--------------------------------------------')
        #meet zombie n decide
        print("[boo!]")#actual jump scare noise
        print('*DANGER*')
        print('a zombie is approaching you')
        print('a: bat')
        print("b: gun")
        print("c: crossbow")
        print("d: nothing")
        print('choose an object:')
        weapon = ''
        weapon = input("what do you do? ")
        if weapon == "a":
            print("you chose bat!")
        elif weapon == "b":
            print("you chose a gun")
        elif weapon == "c":
            print("you chose a crossbow")
        elif weapon == "d":
        else:
            print("blah")


        #
        if hearts == 2:
            level1()
        elif hearts == 0:
            gameoverbad1()

    else:
        print('wow')
        print("coward")
        exit()

start()
