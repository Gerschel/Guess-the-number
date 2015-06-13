__author__ = 'essa'
from Tkinter import *
import random

ran_num = 100
limit = 7

app = Tk()
app.title(string="Guess The Number Game")


def new_game():
    global secret_number, app

    Label(app, text="New Game. Range is from 0 to" + str(ran_num)).pack()

    Label(app, text="Number of remaining guesses is" + str(limit)).pack()
    secret_number = random.randrange(0, ran_num)

def range100():
    global ran_num, limit
    limit = 7
    ran_num = 100
    new_game()

def range1000():
    global ran_num, limit
    limit = 10
    ran_num = 1000
    new_game()

def input_guess():#change 6 by @Gerschel
    global limit, app
    guess = int(user_guess.get()) #change 3 by @Gerschel

    gw = Label(app, text="Guess was" + str(guess)).pack()

    limit = limit - 1
    if guess < secret_number:

        ph = Label(app, text="Higher!").pack()
        nrg = Label(app, text="Number of remaining guesses is " + str(limit)).pack()
    elif guess > secret_number:

        pl = Label(app, text="Lower!").pack()
        nrg = Label(app, text="Number of remaining guesses is" + str(limit)).pack()
    elif guess == secret_number:

        pc = Label(app, text="Correct!").pack()
        range100()
    if limit <= 0:

        urg = Label(app, text="You run out of guesses. the number was" +  str(secret_number))
        if ran_num == 100:
            range100()
        else:
            range1000()

new_game()
user_guess = StringVar() # ghange 1 by @gerschel
################################################################
but100 = Button(app, text="Range: 0 - 100", command=range100)
but1000 = Button(app, text="Range: 0 - 1000", command=range1000)
gs = Entry(app, textvariable=user_guess)#change 2 by @gerschel
guess_button = Button(app, text="Guess!", command=input_guess) #change 4 by @gerschel
#################################################################
but100.pack()
but1000.pack()
gs.pack()
guess_button.pack() #change 5 by @gerschel
#################################################################
mainloop()
