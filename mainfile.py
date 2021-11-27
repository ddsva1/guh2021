#global vars:
#level:0
#number of lives:1
hearts = 1
#gameover = false

#imported libraries:
#pygame?? or tkinter if need be
#
#
#WHY U SO STUPID

def level1():
    print("level1")
    print("*the first date*")

def gameovergood():
    print("you became a zombie!")

def gameoverbad1():
    #play song - really really american one - name??
    print("wow you killed a zombie")
    print(":O")
    print('youre a murderer')
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
        print('a: gin')
        print("b: gun")
        print("c: crossbow")
        print("d: nothing")
        print('choose an object:')
        weapon = ''
        while weapon != 'gun':
            weapon = input("what do you do?")



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
