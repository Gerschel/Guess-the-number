import simplegui
import random

ran_num = 100
limit = 7
def new_game():
    global secret_number
    print ""
    print "New Game. Range is from 0 to", ran_num
    print "Number of remaining guesses is", limit
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
    
def input_guess(guess):
    global limit
    guess = int(guess)
    print ""
    print "Guess was", guess
    limit = limit - 1
    if guess < secret_number:
        print "Higher!"
        print "Number of remaining guesses is", limit
    elif guess > secret_number:
        print "Lower!"
        print "number of remaining guess is", limit
    elif guess == secret_number:
        print "Correct!"
        range100()
    if limit <= 0:
        print "You run out of guesses. the number was", secret_number
        if ran_num == 100:
            range100()
        else:
            range1000()
    
frame = simplegui.create_frame("guess the number", 200, 200)
frame.add_button("Range: 0 - 100", range100, 100)
frame.add_button("Range: 0 - 1000", range1000, 100)
frame.add_input("guess", input_guess, 100)

new_game()

