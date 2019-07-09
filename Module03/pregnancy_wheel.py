import datetime # imports the datetime fields needed for the game
print('---------------------------------')
print('          DUE DATE APP         ') # gives name of the game
print('---------------------------------')
print()
def lmtd_date(): # defining function to get last menstration
    lmtd=input('Type in the date that you last had menstration in the form [mm-dd-yyyy]:')
    parts=lmtd.split('-') # splits the delimeter from entered text
    if len(parts)!=3: # checks for a failure and reasks the user to enter with a correct delimeter
        print('you had incorrect date fomrat',lmtd)
        return lmtd_date() # recursive statement if the user incorrectly types in date
    year=int(parts[2])
    month=int(parts[0])
    day=int(parts[1])
    lmtday=datetime.date(year,month,day) # creates the date
    return lmtday # return date as an output
def main():
    lmtdate=lmtd_date()
    gest_length = datetime.timedelta(days=281) # creates the span length
    gest_std = datetime.timedelta(days=13) # creates the standard deviation
    exp_due_date = lmtdate + gest_length # creates time for expedted date
    min_due_date = exp_due_date - gest_std # gives aminimum most likely range
    max_due_date=exp_due_date + gest_std # gives an upper range
    print('You will most likely deliver on:'+exp_due_date.strftime('%a %b %d %Y')) # outputs the range and expected date
    print('you may deliver as early as: '+min_due_date.strftime('%a %b %d %Y'))
    print('you may deliver as late as: ' + max_due_date.strftime('%a %b %d %Y'))
main()
