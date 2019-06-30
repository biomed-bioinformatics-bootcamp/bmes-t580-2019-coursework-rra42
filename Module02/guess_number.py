import random # imports the random fiels needed for the game
print('---------------------------------')
print('   GUESS THAT NUMBER GAME') # gives name of the game
print('---------------------------------')
print()
GOALNUM = random.randint(0, 100) # creates a random number to be guessed
guess = -1 # creates a dummy initial guess
name = input('Player what is your name? ') # asks for player name
forcedquit=3141592653589793238# creates a quit number to be typed if the player wants to quit
while guess != GOALNUM:
    guess_text = input('Guess a number between 0 and 100: ') # guessin text input
    guess = int(guess_text) # makes the string of number into an integer to be interpreted later
    if guess==forcedquit: # quit statement
        print('You quit. Thanks for playing %s'%name)
        break # breaks from while loop
    if guess < GOALNUM:
        # print('Your guess of ' + guess + ' was too LOW.')
        print('Sorry %s, your guess of %i was too LOW. Try again and if not type %i to quit'%(name, guess, forcedquit))
        # if the player guesses low then the statement will tell them so and will ask to guess again or quit
    elif guess > GOALNUM:
        print('Sorry %s, your guess of %i was too HIGH.Try again and if not type %i to quit'%(name, guess, forcedquit))
        # if the player guesses high then the statement will tell them so and will ask to guess again or quit
    else:
        print('Excellent work %s, you won, it was %i!'%(name, guess)) # the statement tells them if they get it correct
print('done')