import sys                                                                          #importing sys to read command line arguments as filenames
list = dict()                                                                       #define a dictionary
    
#Time complexity Analysis for tokenizing
# O(nmp)
# n- number of lines in the file
# m- number of words in the line
# p - number of characters in words with bad inputs
# O(1) - to add a word to the dictionary
#hence polynomial runtime

def createDictionary(fname):
    try:
        with open(fname,"r") as f:                                                      #open a file in read mode
            for line in f:                                                              #traverse the file line by line
                words = line.lower().split()                                            #split the line based on spaces after converting it to lowercase to get a word list
                #
                for s in words:                                                         #traverse the word list
                    if s.isalnum():                                                     #check if the words are alpha numeric
                        if s in list:                                                   #adding the word to the dictionary if it is alphanumeric
                            list[s] += 1                                                #increment the count if the word already exists
                        else:
                            list[s] = 1                                                 #add the word and set count =1 if seen for the first time
                    else:
                        p = ""
                        for a in s:                                                     #traverse character by character if the word is not alphanumeric
                            if a.isalnum():
                                p = p+a
                            else:
                                if p in list:                                           #adding the alphanumeric part to the dictionary
                                    list[p] += 1
                                elif p!="":
                                    list[p] = 1
                                p =""
                        if p in list:                                                   #adding rest of the string to the dictionary after the nom-alphanumeric character
                            list[p] += 1
                        elif p!="":
                            list[p] = 1
    except:
        print('Enter proper Filename')
    finally:
        f.close()

#Time complexity for sort the dictionary
# O(nlogn)
# n - number of records in the dictionary

def printOutput():                                                                  #printing the dictionary. We sort the words based on frequency from hight to low. Words of same frequency are stored alphabetically
    x = sorted(list.items(), key=lambda x:(-x[1],x[0]))
    for i in x:
        print("%s\t%s" %i)


def main():                                                                         #main function

    if len(sys.argv)!=2:                                                            #command-line arguments for file name inputs
        print('Enter both python file and text file name separated by space')
        sys.exit()
    fname = sys.argv[1]                                                             #using the second argument as the filename 
    createDictionary(fname)
    printOutput()

main()