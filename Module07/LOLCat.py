print('-------------------------------------')
print('         CAT FACTORY APP             ')
print('-------------------------------------')


# below imports all files needed as well as other which i tried to use but couldn't and found another way to solve
import os
import urllib.request
#import Image
#import cv2
import shutil
#import numpy as np


def main():
    filename = get_filename() # gets filename
    folder_name=get_folder_name() # gets folder directory
    url_name=get_url() # gets url from user
    num=get_num() # get numebr of pictures desired
    file_destination=os.path.join(filename,folder_name) # file destination conjoined
    os.mkdir(file_destination) # makes folder with directory
    i=1
    names=['cat1.png','cat2.png','cat3.png','cat4.png','cat5.png','cat6.png','cat7.png','cat8.png','cat9.png','cat10.png','cat11.png','cat12.png','cat13.png','cat14.png','cat15.png']
    while i<=num: # while loop to run through and get the pictures and place in the folder
        # picture = requests.get(url_name, stream=True)
        #picture =urllib.request.urlretrieve(url_name)
        picture = urllib.request.urlopen(url_name) # opens and parses the website for the picture
        file_pic=os.path.join(file_destination,names[i-1])
        #io.imsave(file_pic,picture)
        #image.save(picture)
        #cv2.imshow('URL image',picture)
        #cv2.imwrite(file_pic, picture)

        with open(file_pic,'wb') as handle: # opens and writes the files and pictures in the folder directory
            shutil.copyfileobj(picture,handle)
        picture=0
        i+=1 # counter


def get_filename():

    filename = None
    while filename is None:
# gets filename
        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            # error message and reasks for filename
            print('That file could not be found. Try again.')
            filename = None

    return filename

def get_folder_name():
    file_name='CAT_PICS_PYTHON_FOLDER'
    files=None
    # gets folder name with error and otehr queries and gives choise to user
    while files is None:
        decision = input('Current default folder name is: %s would you like to use this name or not [y]es or [n]o' % file_name)
        try:
            files= str(decision)
        except ValueError:
            print(files + ' is not a string. Please try again. Must give a valid string answer')
            continue
        if decision=='n':
            inp=input('Enter in your filename: ')
            try:
                files = str(inp)
            except ValueError:
                print(files + ' is not a string. Please try again. Must give a valid string')
                continue
            file_name=files

    return file_name

def get_url():
    # has a default url and asks for user if they want to use another and if so they can input
    url_name='http://consuming-python-services-api.azurewebsites.net/content/cats/lolcat2.jpg'
    d_try=None
    while d_try is None:
        decision = input('Current url is: %s would you like to use this url or not: [y]es or [n]o' % url_name)
        try:
            d_try = str(decision)
        except ValueError:
            print(d_try + ' is not a string. Please try again. Must give a valid string answer')
            continue
        if decision == 'n':
            inp = input('Enter in your url: ')
            try:
                file_name = str(inp)
            except ValueError:
                print(file_name + ' is not a string. Please try again. Must give a valid string')
                continue
            url_name=file_name
    return url_name

def get_num():
    num=None
    # asks the user for a number of pictures desired in the folder
    while num is None:
        decision = input('Enter in how many cat pics you want within the folder. The max number of pictures you can store is 15.')
        try:
            num = int(decision)
        except ValueError:
            print(num + ' is not a number. Please try again. Must give a valid number answer')
            continue
    return num

if __name__ == '__main__':
    main()