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
    print('--------------------------------------------')
    exit()

def gameovergood():
    print('--------------------------------------------')
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
    print('--------------------------------------------')
    #play song - really really american one - name??
    print("wow you killed a zombie... his name was Tom")
    print("*child runs in the scene")
    print(":O")
    print('youre a murderer!')
    #zombie kid bit
    print("game over")
    gameover()

def gameoverbad2():
    print('--------------------------------------------')
    print("you've been cancelled on twitter")
    print("A large karen voice")
    print("game over")

def gameoverbad3():
    print('--------------------------------------------')
    #death by angry cow
    print("death by angry cow i guess!!")


def level2():
    print('--------------------------------------------')
    print("Date 1")
    print("*The First Date*") #make this text big
    print("awwwww") #make this text small
    print("choose a movie")
    print("a: twilight")
    print("b: world war z")
    print("c: garfield 3 the movie")
    c = input("movie choice: ")
    if c == "a":
        print("zombie and you had a great movie date")
        hearts = hearts + 1
    elif c == "b":
        print("zombie thinks you are immature")
        hearts = hearts
    elif c == "c":
        print("zombie thinks youre insensitive (yikes)")
        gameoverbad2()
    else:
        print('get error checking - note')

def start():
    global hearts
    hearts = 1
    print("press a, b, c for each option choice")
    inp = input("press enter key to start game ")
    print('--------------------------------------------')
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
        while weapon == "":
            weapon = input("what do you do? ")
            if weapon == "a":
                print("You chose bat!")
                print("You ht the zombie!")
                print("boink!") #zombie is hit
                print("Didn't work... zombie is mildly annoyed")
                hearts = 1
            elif weapon == "b":
                print("You chose a gun")
                print("You shoot the zombie!")
                print("Blood is splattered!")
                print("Zombie's lifeless body falls to the floor")
                hearts = 0
            elif weapon == "c":
                print("You chose a crossbow")
                print("You are inexperienced!")
                print("You shot yourself in the foot")
                print("zombie smells your blood, looks hungry")
                hearts = 1
            elif weapon == "d":
                #wow brave choice etc etc
                print("you're going into this empty handed")
                #the zombie approves etc and thinks youre being friendly
                hearts = 2
            else:
                print("sorry try again, that wasnt one of the options?")


    else:
        print('wow')
        print("coward")
        print('--------------------------------------------')

start()

x = input("")
if input == input:
    exit()
