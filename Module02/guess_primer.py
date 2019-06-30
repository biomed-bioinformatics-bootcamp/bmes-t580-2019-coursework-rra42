import random # imports the random library for use later
print('---------------------------------')
print('   GUESS THAT PRIMER  GAME') # gives the name of the game
print('---------------------------------')
print()
#GOAL= random.randint(0, 100)
GOAL=random.choice('ACGT') # creates the first letter for the random primer with letter of A,G,C, and\ or T
GOAL+=random.choice('ACGT') # next for lines subsequently add on to the primer to create a random primer
GOAL+=random.choice('ACGT')
GOAL+=random.choice('ACGT')
GOAL+=random.choice('ACGT')
guess = 'NNNNN' # initial dummy guess string
name = input('Player what is your name? ') # asks for players name
forcedquit='Quit' # gives the player the option to force quit
while guess != GOAL: # while loop to run until guess from the user equals the random primer generated
    guess = input('Guess a 5 base primer containing letters of A,G,C,T: ') # guess taken as an input from the user
    if guess==forcedquit:
        print('You quit. The primer is %s' %GOAL)
        break
    misses=0 #number of wrong letters counter
    for i in range(len(guess)): # for loop to check how many misses are between guess and random primer generated
        if guess[i]!=GOAL[i]:
            misses+=1

    if misses>0:
        print('sorry, you guuessed %i bases wrong.Play again. Or type "Quit" to force quit and output the primer' % misses)
        # allows for retry if more than 1 wrong
    else:
        print('%s you got the correct primer: %s' % (name , guess)) # outputs persons name and the correct primer
    #if guess != GOAL:
        # print('Your guess of ' + guess + ' was too LOW.')
     #   print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
   # elif guess > GOAL:
    #    print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    #else:
     #   print('Excellent work {}, you won, it was {}!'.format(name, guess))

print('done')