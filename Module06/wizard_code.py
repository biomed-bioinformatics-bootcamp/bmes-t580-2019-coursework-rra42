import random #imports random library for random dice roll

class Creature(object): # creates class of creatures
    def __init__(self, name, level): # takes in slef and name of the creature as well as level
        self.name = name# initializes name of the object
        self.level = level# initializes level of the object
    def print(self):
        print('Name:', self.name, 'Level:', self.level) # prints out the name of the creature when called upon
    def print_creature(Creature):# used in upstream classes for printing their creature
        print('Name;', Creature.name, 'Level:', Creature.level)
    def attack_roll(self): # attack roll of the creature
        die = random.randint(1, 20) # attack vlaue
        return die * self.level # return attack value scaled to level
    def defense_roll(self): # defense value of the creature
        die = random.randint(1, 20) # defense value
        return die * self.level # return scaled value of the defense of creature

class Wizard(Creature): # imports all methods defined in the creature class
    def __init__(self, name, level, typ=None): # overrides creature class method to allow for making type of the object
        self.name = name # initializes name of the object
        self.level = level# initializes level of the object
        self.typ = typ# initializes type of the object
    def print(self): # again made to allow for printing of name type and level
        print('Name:', self.name, 'Level:', self.level, 'Type:', self.typ)

    def level_up(self): # allows user, whicheve class they are other than creature to level up
        self.level += 1 # increases user level
#All subsequent classes import same methods as the Wizard but change the type of their object

class IceWizard(Wizard):
    def __init__(self, name, level, typ='ice'):
        self.name = name
        self.level = level
        self.typ = typ
class FireWizard(Wizard):
    def __init__(self, name, level, typ='fire'):
        self.name = name
        self.level = level
        self.typ = typ
class ELF(Wizard):
    def __init__(self, name, level, typ='ELF'):
        self.name = name
        self.level = level
        self.typ = typ
class ORCS(Wizard):
    def __init__(self, name, level, typ='ORC'):
        self.name = name
        self.level = level
        self.typ = typ
class Dwarf(Wizard):
    def __init__(self, name, level, typ='Dwarf'):
        self.name = name
        self.level = level
        self.typ = typ
