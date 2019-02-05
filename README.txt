PART - A Tokenizer and Word Frequencies
1. Read an input file passed as a command line argument
2. Tokenize the text of the file. A token is a sequence of alphanumeric characters
(a-zA-Z0-9), independent of capitalization (so “Apple” and “apple” are the
same token)
3. Counts the number of occurrences of each word in the tokens generated
4. Print out the word frequency counts onto the screen. The print out should be
ordered by decreasing frequency. (so, highest frequency words first). Resolve ties alphabetically in ascending order.

Input:
Here’s a fun-fact! White tigers live mostly in “India”. Wild lions live mostly in “Africa”.

Output:
in 2 live 2 mostly 2 a1 africa 1 fact 1 fun 1 here 1 india 1 lions 1 s 1 tigers 1 white 1 wild 1



PART B - Intersection of Two Files

Write a program that takes two text files as arguments and outputs the number of tokens they have in common. Here is an example of input/output:

Input file 1:
We reviewed the trip and credited the cancellation fee. The driver has been notified.

 Input file 2:
If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply.

Output
 6