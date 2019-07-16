import random

class creature(object):
   def __init__(self,name,level):
      self.name=name
      self.level=level
   def print(self):      # this is a method which is a function attached to an object
        print('Name:', self.name,'Level:', self.level)

def print_creature(creature):
    print('Name;',creature.name,'Level:',creature.level)
def attack_roll(self):
    die=random.randint(1,20)
    return die*self.level
def defense_roll(self):
    die =random.randint(1,20)
    return die*self.level

class Wizard(creature): # subclass creature so behind the scenes whatever the creature can do then the #creature can also do it
    def __init__(self,name,level,typ=None):# the type is to know which type the object is and is called overloading where the init in the wizard class override the one in creature so this init will be used
      self.name=name
      self.level=level
      self.typ=typ
    def print(self):
        print('Name:',self.name,'Level:',self.level,'Type:',self.typ)
    def level_up(self):
      self.level+=1

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



