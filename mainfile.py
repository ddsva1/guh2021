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
        print("d: nothing")
        print('choose an object:')
        weapon = ''

        weapon = input("what do you do? ")
        if weapon == "a":
            print("You chose bat!")
            print("You ht the zombie!")
            print("boink!") #zombie is hit
            print("Didn't work... zomvie is mildly annoyed")

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
            print("you're going into this empty handed")
            hearts = 2
        else:
            print("blah")

        #
        if hearts == 2:
            level2()#to date 1
        elif hearts == 0:
            gameoverbad1()

    else:
        print('wow')
        print("coward")
        exit()

start()


 


