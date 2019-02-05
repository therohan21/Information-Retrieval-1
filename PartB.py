import sys

list = set()														#defining a set

# Time complexity Analysis - addToSet()
# O(nmp) 
# n - number of lines in the file
# m- number of words in the line
# p - number of characters in words with bad inputs
# O(1) - adding to the set
#hence polynomial runtime

def addToSet(fname1):
	try:	
		with open(fname1,"r") as f:										#open a file in read mode
			for line in f:												#read the file line by line
				words = line.lower().split()							#split the line based on spaces after converting it to lowercase to get a word list
				#print(len(words))
				#print(words)
				for s in words:											#traverse through the word list
					if s.isalnum():										#check if the word is alphanumeric
						list.add(s)										#add the word to a set if it is alphanumeric
					else:
						p = ""
						for a in s:										#traverse character by character if the word is not alphanumeric
							if a.isalnum():
								p = p+a 								#append the alphanumeric characters to an empty string
							else:
								if p not in list and p!="":									
									list.add(p)								#add the word to the set if it doesn't exist
								p =""
						if p not in list and p!="":
							list.add(p)

	except:
		print('Enter Proper Filename 1')
	finally:
		f.close()

# Time complexity Analysis - commonWordCount()
# O(nmp) 
# n - number of lines in the file
# m- number of words in the line
# p - number of characters in words with bad inputs
# O(1) - removing common words from the set and incrementing the counter
#hence polynomial runtime


def commonWordCount(fname2):
	count = 0
	p = ""
	try:

		with open(fname2,"r") as f:										#open a file in read mode
			for line in f:												#read the file line by line
				words = line.lower().split()							#split the line based on spaces after convreting it to lowercase to get a word list
				for s in words:											#traverse through the word list
					if s.isalnum():										#check if the word is alphanumeric
						if s in list:									#chceck if the same word is present in the set
							list.remove(s)								#if the word is present in the set, then remove it
							count += 1									#and increment the count by 1
					else:
						p = ""
						for a in s:										#traverse character by character if the word is not alphanumeric
							if a.isalnum():
								p = p+a 								#append the alphanumeric characters to an empty string
							else:
								if p in list:							#if tbe word is present in the set, then remove it
									list.remove(p)
									count += 1
								p = ""
						if p in list:
							list.remove(p)
							count +=1
						p=""
		print(count)
	except:
		print('Enter proper Filename 2')													#print the final count of words that were common to both the files
	finally:
		f.close()


def main():															#main function definition
	if len(sys.argv)!=3:											#Command-line arguments for file names
		print('Enter both python file and text file name separated by space')
		sys.exit()
	fname1 = sys.argv[1]											#Command-line argument 1 is the filename 1
	fname2 = sys.argv[2]											#Command-line argument 2 is the filename 2
	addToSet(fname1)												#create a set with all the words in file1
	commonWordCount(fname2)											#count all the words that are common in file1 and file2 by removing common words from set and counting it


main()


					







