import datetime # imports the datetime fields needed for the game
print('---------------------------------')
print('            BIRTHDAY APP') # gives name of the game
print('---------------------------------')
print()

year= int(input('what year were you born in [YYYY]:')) # asking for year of birth
month = int(input('what month were you born in [MM]: ') )# asking for month of birth
day = int(input('what day were you born in [DD]: ') )# asking for the day of birth

date_birth=datetime.date(year,month,day) # makes the date of birth
date_today_orig=datetime.date.today() # gets todays date
date_today=datetime.date(date_birth.year,date_today_orig.month,date_today_orig.day) # normalizes today's date to the
# year the person is born so years will not be counted in the days
num_days_between=date_birth-date_today # takes the difference in days
if num_days_between.days > 0: # checks for days left until birthday
        print('There are %i days left until your birthday' %num_days_between.days) # outputs the number of days left
        # until the person's birthday
        print('I hope you are looking forward to your birthday')
elif num_days_between.days < 0: # checks for how many days passed after birthday occured
        print('your birthday was %i days ago'%abs(num_days_between.days))# outputs the number of days since the persons
        # birthday
        print('I hope you enjoyed your birthday')
else: # checks if the date is the person's birthday
    print('Today is your birthday. Happy birthday.')