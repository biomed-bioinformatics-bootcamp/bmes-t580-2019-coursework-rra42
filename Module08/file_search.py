print('-------------------------------------')
print('           SEARCHING APP             ')
print('-------------------------------------')

# imports all required libraries
import os
import time

arb=None

# main function
def main():
    filename = None
    while filename is None:
# asks for the name and directory of the file
        filename = str(input("What is the /path/to/the/file? "))
        # Check if the filename exists.
# checks if the directory exists
        if not os.path.exists(filename):
            print("That file could not be found. Try again.")
            filename = None
    while arb is None: # asks for the word desired to be searched from suer
        string_search=str(input("Type in the words that are desired to be searched within the file"))
        if len(string_search)==0:
            print("You cannot search without criteria or words to searhc for")
            continue
        if string_search!=0:
            break
            # lists all directories
    filenames_list=os.listdir(filename)
    print(filenames_list) # prints directories
    col=0
    while col <len(filenames_list): # runs as many times as files found in directory
        files=os.path.join(filename,filenames_list[col])
        [line,lines_num]=word_searcher(files,string_search)
        if len(line)==0: # prints out the line with the word within the file
            print("found nothing within the file: %s" %(filenames_list[col]))
        else:
            print("found %i mathes in the file: %s"%(len(line),str(filenames_list[col])))
            x=1
            while x<=len(line):
                time.sleep(1) # time stop 1 sec for delay so you can read the line
                print("found %s in line %s with the line containing the string: %s" %(string_search,lines_num[x-1],str(line[x-1])))
                x+=1
        col+=1
    print("Thanks for searching")

def word_searcher(files,string_search):
    lines=[]
    lines_num_arr=[]
    line_num: int=1
    #print(files)

    with open(files,mode='r') as handle: # opens the file as a read file to see matching words
        for liner in handle:

            liner=str(handle.readline())
            #print(liner) # opens and reads teh file and finds matching word within that file
            if liner.find(string_search)>=0:
                lines.append(liner)
                lines_num_arr.append(line_num)
            line_num+=1

    return [lines,lines_num_arr] # returns line and the line number

if __name__ == '__main__':
    main()