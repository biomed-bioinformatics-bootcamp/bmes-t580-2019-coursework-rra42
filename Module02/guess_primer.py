
import random

print('---------------------------------')
print('   GUESS THAT PRIMER  GAME')
print('---------------------------------')
print()

#GOAL= random.randint(0, 100)
GOAL=random.choice('ACGT')
GOAL+=random.choice('ACGT')
GOAL+=random.choice('ACGT')
GOAL+=random.choice('ACGT')
GOAL+=random.choice('ACGT')


guess = 'NNNNN'

name = input('Player what is your name? ')

while guess != GOAL:
    guess = input('Guess a 5 base primer containing letters of A,G,C,T: ')

    misses=0
    for i in range(len(guess)):
        if guess[i]!=GOAL[i]:
            misses+=1

    if misses>0:
        print('sorry, you guuessed %i bases wrong.Play again' % misses)
    else:
        print('%s you got the correct primer: %s'% name,% guess)




    #if guess != GOAL:
        # print('Your guess of ' + guess + ' was too LOW.')
     #   print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
   # elif guess > GOAL:
    #    print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    #else:
     #   print('Excellent work {}, you won, it was {}!'.format(name, guess))

print('done')