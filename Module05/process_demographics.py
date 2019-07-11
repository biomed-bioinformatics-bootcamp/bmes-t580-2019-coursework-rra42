import csv # Made by Rahul Akkem 
import os
def main():
    # these below lines call the functions to get criteria from user to filter out patients by criteria
    print_the_header()
    filename = get_filename()
    age_min, age_max = get_age_cutoff()
    sex=get_sex_om()
    lower_inf,upper_inf=get_infec_length()
    therapy=get_on_therapy()
    coinfect=get_coinfected()
    out_filename=filename+'.valid'
    num_pats = 0

    # Open file and start reader
    with open(filename,mode='r') as handle:
        reader = csv.DictReader(handle) # DictReader will give header names to columns

        with open(out_filename, mode='w') as out_handle:
            fields=['PAT_NUM','SEX','AGE','INFECTION_LENGTH','ON_THERAPY','COINFECTION']
            writer= csv.DictWriter(out_handle,fields)
            writer.writeheader() # headers need to be told to be written
            #raise SystemExit

            # filters out patients by users input criteria and outputs a file with filtered patients
            for row in reader:
                pat_age = int(row['AGE'])
                sex_col=str(row['SEX'])
                pat_on_therapy=str(row['ON_THERAPY'])
                pat_coin=str(row['COINFECTION'])
                inf_len=int(row['INFECTION_LENGTH'])
                #infection_len=int[row['Infection_age']]
                # Seperate out the long logic for clarity
                match_age =  (pat_age > age_min) and (pat_age < age_max)
                match_inf_len = (inf_len > lower_inf) and (inf_len < upper_inf)
                match_sex=True
                if sex!=None:
                    match_sex=(sex_col==sex)
                match_therapy = True
                if therapy!= None:
                    match_therapy = ( pat_on_therapy == therapy)
                match_coin = True
                if coinfect!= None:
                    match_coin = (pat_coin == coinfect)
                #add the
                if match_age and match_sex and match_therapy and match_coin and match_inf_len:
                   num_pats += 1 # counter for number of patients that qualify
                   # this deletes old file and force writes the filter patients in this new file
                   writer.writerow(row)
# this prints out criteria the user has chosen
    print('Based on the following criteria:')
    print(' - Age: [%i, %i]' % (age_min, age_max))
    print(' - Infection Length: [%i, %i]' % (lower_inf, upper_inf))
    print(' - Gender %s',sex)
    print(' - Therapy %s',therapy)
    print(' - Coinfection %s',coinfect)
    print('There are %i eligible patients' % num_pats)

# prints the headrr
def print_the_header():
    print('---------------------------------')
    print('       Process Demographics')
    print('---------------------------------')
    print()

# gets the filename from user to use to extract patient data from
def get_filename():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename

# this requires user to input patients age ranges they want to filter
def get_age_cutoff():

    age_min, age_max = None, None
    while age_min is None:
        age_inp = input('What is the youngest age for the study? ')
        # checks if what the user input is actually a integer if not this will reask them to input a valid answer
        try:
            age_min = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again')
            continue

        if age_min < 18:
            print('Ethics boards require special permission for youth cohort. Please pick an older age')
            age_min = None

    while age_max is None:
        age_inp = input('What is the oldest age for the study? ')
        try:
            age_max = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again')
            continue

    return age_min, age_max


# this asks user to choose to filter patients by gender
def get_sex_om():

    sex_g = None
    while sex_g is None:
        gender= input('would you like to filter by gender? [m]ale or [f]emale or [n]o')
        try:
            gender=str(gender)
        except ValueError:
            print(gender + ' is not one of the choices. Please type in a credible answer')
            continue
        #if gender!='n' or gender!='m' or gender!='f':
        if gender == 'n':
            break
        if gender=='m':
            sex_g='Male'
        if gender=='f':
            sex_g='Female'
    return sex_g


# this gives function makes the user input criteris for lower and upper bounds of infection length
def get_infec_length():

    years_lower, years_upper = None, None
    print('Now enter the lower bounds for patients you want to see who have had the infection for a certain number of years')
    while years_lower is None:
        age_inp = input('Enter the lower bounds for patients you want to see who have had the infection for a certain number of years :')
        try:
            years_lower = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again. Must give a valid lower bound')
            continue


    while years_upper is None:
        age_inp = input('Enter the upper bounds for patients you want to see who have had the infection for a certain number of years')
        try:
            years_upper = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Please try again. Must give a valid upper bound')
            continue

    return years_lower,years_upper

# this gives user option to filter patients by whether they are on therapy
def get_on_therapy():

    therapy_lev = None
    while therapy_lev is None:
        therapy= input('What level of treatment involvement do you want to filter patients by. [n]o treatment,[y]es treatment, [a]ll patients')
        try:
            therapy=str(therapy)
        except ValueError:
            print(therapy+' is not one of the choices. Please type in a credible answer')
            continue
        if therapy == 'a':
            break
        elif therapy=='n':
            therapy_lev='No'
        elif therapy=='y':
            therapy_lev='Yes'
    return therapy_lev

# this function allows user to filter by coinfected patients or not
def get_coinfected():
    coin_lev = None
    while coin_lev is None:
        coinfection = input('What level of coinfection do you want to filter patients by. [n]o coinfection,[y]es coinfection, [a]ll patients')
        try:
            coinfection = str(coinfection)
        except ValueError:
            print(coinfection + ' is not one of the choices. Please type in a credible answer')
            continue
        if coinfection == 'a':
            break
        elif coinfection == 'n':
            coin_lev = 'No'
        elif coinfection == 'y':
            coin_lev = 'Yes'
        return coin_lev

if __name__ == '__main__':
    main()