print('---------------------------------') # made by Rahul Akkem
print('        JOURNAL ENTRY APP        ') # gives the name of the game
print('---------------------------------')
print()
inw='O' # initial variable for the inward variable
while inw!='e': # while loop to go until e is hit for exit
    inw = input('What do you want to do. [a]dd, [l]ist, [e]xit,[c]lear all entries so far') # gives instructions
    if inw=='l': # if statement to list all entries to date
        with open('journal.txt') as handle:
            for line in handle: # prints all entries in the text journal
                print(line)
    elif inw=='a':
        with open('journal.txt') as handle:
            for line in handle:
                print(line)
        with open('journal.txt',mode='a') as handle: # calls add ability to the journal to add after naming as handle
            handle.write(input('Type what you want to enter')) # # asks user for prompt to enter
            handle.write('\n') # journal goes to the next line automatically
    elif inw=='c': # gives user the opportunity to clear the journal
        with open('journal.txt') as handle: # displays what is in the journal so far
            for line in handle:
                print(line)
        with open('journal.txt', mode='w') as handle: # this deletes the journal entries
            print('nothing in journal') # this prints to tell user all entries are deleted
print('your entries so far is:') # after exiting it shows what is entered in the journal.txt file so far
with open('journal.txt') as handle: # this lists what is in the journal file
    for line in handle:
        print(line)