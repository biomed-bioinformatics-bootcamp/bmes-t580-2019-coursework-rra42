print('-------------------------------------')
print('       REAL ESTATE ANALYZER APP      ')
print('-------------------------------------')
import csv # Made by Rahul Akkem
import os # imports the libraries needed

def main():
    filename = get_filename()
    [price_min, price_max] = price_cutoff()
    beds=bed_cutoff()
    [lower_sqf, upper_sqf]=get_sqf()
    type_of=get_type()
    out_filename=filename+'.filtered'
    counter = 0
    # initializes the variables
    list_price=[]
    list_2_price=[]
    list_2_beds=[]
    list_2_baths=[]
    list_big_sqf = 0
    list_price_max =0
    list_low_price=10000000000000000000000000000000000000000000
    mp_price = 0
    mp_bed = 0
    mp_bath = 0
    mp_loc = ''
    lp_price = 0
    lp_bed = 0
    lp_bath = 0
    lp_loc = ''
    ms_price = 0
    ms_bed = 0
    ms_bath = 0
    ms_loc = ''
    list_avg_beds=[]
    list_avg_baths=[]
    # Open file and start reader
    with open(filename,mode='r') as handle: # reads the files
        reader = csv.DictReader(handle) # DictReader will give header names to columns

        with open(out_filename, mode='w') as out_handle: # writes a new file and outputs it
            fields=['street','city','zip','state','beds','baths','sq__ft','type','sale_date','price','latitude','longitude']
            writer= csv.DictWriter(out_handle,fields)
            writer.writeheader() # headers need to be told to be written
            for rowi in reader:
                list_bed_num = int(rowi['beds']) # finds the rows of the beds and all other criteria being filtered with
                list_sqft = int(rowi['sq__ft'])
                list_prices = int(rowi['price'])
                list_type= str(rowi['type'])
                match_prices=True
                if price_min!=None and price_max!=None:
                    match_prices =((list_prices >= price_min) and (list_prices <= price_max))
                match_sqft = True
                if lower_sqf!=None and upper_sqf!=None:
                    match_sqft =((list_sqft >= lower_sqf) and (list_sqft <= upper_sqf))
                match_beds=True
                if list_bed_num!=beds:
                    match_beds=False
                match_type=True
                if type_of!= None:
                    match_type = (list_type == type_of)
                # criteria filters for what houses needed and filters them out to then later be analyzed and output
                # in a new file
                if match_type and match_prices and match_sqft and match_beds:
                    counter += 1 # counter for number of houses that qualify
                    writer.writerow(rowi)
                    # below is filtration and certain characteristic s of certain criteria like average house size
                    # average price , average price of two beds, and other statistics
                if int(rowi['price']) > list_price_max:
                    list_price_max = int(rowi['price'])
                    mp_price = int(rowi['price'])
                    mp_bed = int(rowi['beds'])
                    mp_bath = int(rowi['baths'])
                    mp_loc = str(rowi['city'])
                if int(rowi['price']) < list_low_price and int(rowi['price']) != 0:
                    list_low_price = int(rowi['price'])
                    lp_price = int(rowi['price'])
                    lp_bed = int(rowi['beds'])
                    lp_bath = int(rowi['baths'])
                    lp_loc = str(rowi['city'])
                if int(rowi['sq__ft']) > list_big_sqf:
                    list_big_sqf = int(rowi['sq__ft'])
                    ms_price = int(rowi['price'])
                    ms_bed = int(rowi['beds'])
                    ms_bath = int(rowi['baths'])
                    ms_loc = str(rowi['city'])
                if int(rowi['beds']) == 2:
                    list_2_price.append(int(rowi['price']))
                    list_2_beds.append(int(rowi['beds']))
                    list_2_baths.append(int(rowi['baths']))
                list_price.append(int(rowi['price']))
                list_avg_beds.append(int(rowi['beds']))
                list_avg_baths.append(int(rowi['baths']))

# this prints out criteria the user has chosen
    print('Based on the following criteria:')
    print(' - Price Cutoff: [%i, %i]' % (price_min, price_max))
    print(' - SQF filtration: [%i, %i]' % (lower_sqf, upper_sqf))
    print(' - Bedrooms number cutoff: %i' % int(beds))
    print(' - Type of home %s' % type_of)
    print('There are %i eligible homes from the given criteria' % counter)
    print('Highest priced house with %i -beds %i -baths and costs: %i $ and is located in %s' %(mp_bed,mp_bath,mp_price,mp_loc))
    print('Least priced house with %i -beds %i -baths and costs: %i $ and is located in %s' %(lp_bed,lp_bath,lp_price,lp_loc))
    print('Biggest house with %i- square feet with %i -beds %i -baths and costs: %i $ and is located in %s' %(list_big_sqf,ms_bed,ms_bath,ms_price,ms_loc))
    print('2 Bedroom house average price:%i $ and %f beds and %f baths' % ((sum(list_2_price)/len(list_2_price)),round((sum(list_2_beds)/len(list_2_beds)),2),round(sum(list_2_baths)/len(list_2_baths),2)))
    print('Overall houses average : %i $ and %f baths and %f beds' % (sum(list_price)/len(list_price),round(sum(list_avg_baths)/len(list_avg_baths),2),round(sum(list_avg_beds)/len(list_avg_beds),2)))


# gets the filename from user to use to extract the data of houses
def get_filename():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename

# this requires user to input price ranges desired and filtered by
def price_cutoff():

    price_min, price_max = None, None
    while price_min is None:
        price_min_val = input('What is the lowest price you are willing to go? ')
        # checks if what the user input is actually a integer if not this will reask them to input a valid answer
        try:
            price_min = int(price_min_val)
        except ValueError:
            print(price_min_val + ' is not a number. Please try again')
            continue

    while price_max is None:
        price_max_val = input('What is the highest price you are willing to go?')
        try:
            price_max = int(price_max_val)
        except ValueError:
            print(price_max_val + ' is not a number. Please try again')
            continue

    return int(price_min_val), int(price_max_val)


# this asks user to choose to filter by beds number
def bed_cutoff():
    beds=None
    while beds is None:
        beds_inp = input('What is the number of beds desired? ')
        try:
            beds = int(beds_inp)
        except ValueError:
            print(beds_inp + ' is not a number. Please try again')
            continue
    return int(beds_inp)


# this gives function makes the user input criteris for lower and upper bounds of sq ft of house
def get_sqf():

    sqf_lower, sqf_upper = None, None
    print('Now enter the bounds for square feet you want in the house')
    while sqf_lower is None:
        sqf_lower_val = input('Enter the lower bounds for square feet you want in the house:')
        try:
            sqf_lower = int(sqf_lower_val)
        except ValueError:
            print(sqf_lower_val + ' is not a number. Please try again. Must give a valid lower bound')
            continue


    while sqf_upper is None:
        sqf_upper_val = input('Enter the upper bounds for square feet you want in the house')
        try:
            sqf_upper = int(sqf_upper_val)
        except ValueError:
            print(sqf_upper_val + ' is not a number. Please try again. Must give a valid upper bound')
            continue

    return int(sqf_lower_val),int(sqf_upper_val)

# this gives user option to filter what type of house desired
def get_type():

    type = None
    while type is None:
        type_inp= input('What type of house do you want. [r]esidential,[c]ondo,[m]ulti-family, [a]ll types')
        try:
            type=str(type_inp)
        except ValueError:
            print(type_inp+' is not one of the choices. Please type in a credible answer')
            continue
        if type_inp== 'a':
            break
        elif type_inp=='c':
            type_inp='Condo'
            break
        elif type_inp=='m':
            type_inp='Multi-Family'
            break
        elif type_inp=='r':
            type_inp ='Residential'
            break
    return type_inp

if __name__ == '__main__':
    main()