from Bio import SeqIO # imports all of the libraries needed
import os
import csv
# Rahul Akkem

print('---------------------------------')
print('      Summarize Genbank File     ')
print('---------------------------------')
print() # prints our the title for the app

def get_aa(seq): # gets the translated expanded view of the sequence inputed
    transc=seq.transcribe()
    transl=transc.translate()
    return transl


def get_genbank_path(): # gets the file directory to where the file is located

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/genbank/file?') # asks user foro the file directory

        # Check if the filename exists.
        if not os.path.exists(filename): # checks if this file directory exists, just as a check
            print('That file could not be found. Try again.')
            filename = None

    return filename # returns file directory

def write_path(): # gets the output file location of the user, which can be modified to write a different name

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/genbank/file you want to write to and create?') # user input

    return filename  # file directory output

def print_genbank_record(gb_record): # looks at the record
    print('Found Sequence:', gb_record.id)
    print(gb_record.description)

    print('It starts:', gb_record.seq[:10])
    print('It ends:', gb_record.seq[-10:])
    print('It has %i nucleotides' % len(gb_record.seq))

    print('It has %i features.', len(gb_record.features))

    for feat in gb_record.features:
        print("Type:", feat.type)
        print("Location:", feat.location)


def find_orfs(seq): # this functions finds all of the open reading frames

    start = 0
    forward_orf_count = 0
    while start < len(seq):

        pos = seq.find('ATG', start)
        if pos == -1: #Found no more starts
            break

        start += pos

        forward_orf_count += 1

    reverse_orf_count = 0
    start = 0
    nseq = seq.reverse_complement()
    while start < len(nseq):

        pos = nseq.find('ATG', start)
        if pos == -1: #Found no more starts
            break

        start += pos
        reverse_orf_count += 1

    print('There are a total of %i forward ORFs and %i reverse ORFs' % (forward_orf_count, reverse_orf_count))

def main():

    gb_path = get_genbank_path() # gets the output of file directory to be read
    write_path_name=write_path() # gets output
    #get_aa()
    with open(gb_path) as handle:
        for seq_record in SeqIO.parse(handle, 'genbank'):
            print_genbank_record(seq_record)
            find_orfs(seq_record.seq) # gets the open reading frames
            aa=get_aa(seq_record.seq) # gets the amino acid translation
        with open(write_path_name, mode='a') as handle: # opens the ne file to write
            handle.write(str(seq_record.translate())) # writes the description of the file and amino acid
            handle.write('\n Expanded view translation: \n')
            handle.write(str(aa)) # prints expanded view of the amino acid

if __name__ == '__main__':
    main()