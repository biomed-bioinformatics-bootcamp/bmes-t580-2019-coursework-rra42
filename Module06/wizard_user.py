import wizard_code
from wizard_code import Creature,Wizard,IceWizard,ORCS,ELF,FireWizard,Dwarf # imports each class from the code with
# class definitions
import random # imports random for random choice of villains

try: # this try is here to import a code as a shoretened version of the name just for practice
    import wizard_code as wc
except ImportError:
    import Module06.wizard_code as wc # this is what python thinks this is the way things should be done(forcing line)

if __name__ == '__main__':
    creatures_to_fight=[ # initializes the opponents names and levels
        Wizard('Gandalf the White',100),
        IceWizard('Gandalf the Grey', 20),
        ELF('Elf King', 500),
        ELF('Legolas', 9000),
        FireWizard('Ra', 50),
        FireWizard('Bran The Broken', 30),
        ORCS('Orc 1', 30),
        ORCS('Orc commander', 100),
        ORCS('Orc General 1', 1000),
        ORCS('Orc General 2', 1000),
        ORCS('Orc General 3', 1000),
        ORCS('Orc General 4', 1000),
        Dwarf('Tyrian', 20),
        Dwarf('Bilbo Baggins', 500),
        Dwarf('Thorin', 1000),
        Dwarf('Balin', 1000),
        Dwarf('Gimli', 1000),
        Dwarf('Mr.Gamgee', 1000),
        Creature('bat', 1),
        Creature('dragon', 10),
        Creature('wolf', 50)
    ]
    name=input('Type in the name of your Champion:') # asks user to input their name to be used as the champions name
    me=ELF(name,10) # initializes the player starting at level ten with a TYPE of ELF

    while True:
        turn_creature=random.choice(creatures_to_fight) # randomly chooses the opponent from the list above
        print('An {} emerges from the forest.'.format( turn_creature.name)) # prints the creatures name and level
        len_vill=len(creatures_to_fight) # gets the number of villains left
        if me.level>turn_creature.level: # checks and suggests what to do when faced with a greater or lesser opponent
            print('kill this thing. Its level {}'.format(turn_creature.level))
        else:
            print('Watch out its level {}'.format(turn_creature.level))
        print('What do you want to do')
        action=input ('[a]ttack,[r]un,[q]uit: ') # asks user for an input to play quit or run
        if action =='q': # if user hits q then they can quit
            print('See ya')
            raise SystemExit # force quits program
        elif action =='a': # if user hits attack
            my_roll=me.attack_roll() # retrieves attack roll
            creature_roll=turn_creature.defense_roll() # retrieves opponent defense roll
            print('you got: ',my_roll,'They got,',creature_roll) # tells user what they got and what opponent got
            if my_roll >=creature_roll: # checks if user killed opponent
                print('yay killed it')
                for i in range(turn_creature.level): # allows user to absorb all the levels of the slain opponent
                    me.level_up()
                print('Your level now is : {}'.format(me.level)) # outputs user level
                creatures_to_fight.remove(turn_creature) # removes the creature to fight because it was slain
                print('There are still: %i to fight\n' % len_vill) # tells how many villains left
            elif my_roll <creature_roll: # no kill
                print('you didnt kill it and you were spared from the wrath of {}'.format(turn_creature.name)) # tells user they didn't kill
                print('Your level is still: {} '.format(me.level))# again tells level and number of villains left
                print('There are still: %i to fight\n' %len_vill)
        elif action=='r':# if user chooses to run
            print('You ran and hid . Maybe a cool idea ') # tells them they ran
            print('Your level is still: {} '.format(me.level))# again tells level and number of villains left
            print('There are still: %i to fight\n' %len_vill)
            continue
        if action!='q' and action!='a' and action!='r': # requires user to enter a valid input
            print('please enter a valid input')
            continue
        if len_vill==1:
            print('You have slain all opponents you are now the protector of the realm') # ends the game if no villains left
            raise SystemExit