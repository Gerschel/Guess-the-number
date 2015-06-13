__author__ = 'essa'
from Tkinter import *
import random

ran_num = 100
limit = 7

app = Tk()
app.title(string="Guess The Number Game")
app.geometry("202x125")


def new_game():
    global secret_number, app, status_message
    status_message.set("New Game. Range is from 0 to %d.\nNumber of remaining guesses is %d." % (ran_num, limit))
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


def input_guess():
    global limit, app, status_message, extra_message
    guess = int(user_guess.get())

    ex = Label(app, text="Guess was" + str(guess)).grid()  # todo.

    limit = limit - 1
    if guess < secret_number:
        status_message.set("Higher!\nNumber of remaining guesses is %d" % (limit))

    elif guess > secret_number:
        status_message.set("Lower\nNumber of remaining guesses is %d." % (limit))

    elif guess == secret_number:
        extra_message = Label(app, text="Correct!").grid()  # todo.
        # status_message.set("Correct!")
        range100()
    if limit <= 0:

        urg = Label(app, text="You run out of guesses. the number was" + str(secret_number))  # todo.
        if ran_num == 100:
            range100()
        else:
            range1000()


user_guess = StringVar()
################################################################
but100 = Button(app, text="Range: 0 - 100", command=range100, width=12)
but1000 = Button(app, text="Range: 0 - 1000", command=range1000, width=12)
gs = Entry(app, textvariable=user_guess, width=15)
guess_button = Button(app, text="Guess!", command=input_guess, width=12)
#################################################################
but100.grid(row=0, column=1, sticky='e')
but1000.grid(row=1, column=1, sticky='e')
gs.grid(row=0, column=0, sticky='w')
guess_button.grid(row=1, column=0, sticky='w')
# Status Bar
status_message = StringVar()
status_message.set("")
status_bar = Label(app, textvariable=status_message, relief=SUNKEN, anchor='sw', width=28,
                   height=3)  # By character width height
status_bar.grid(row=3, columnspan=2, sticky='s')
#################################################################
new_game()
mainloop()
