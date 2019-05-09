'''
Name - Adryan Funcheon
Date - 05/03/2019
Course - DSC - 510, Intro to Programming
File - Assignment 8.1
Purpose - This program will perform three essential operations:
1. Process the Gettysburg.txt.
2. Calculate the total words.
3. Output the number of occurrences of each word in the file

'''

import string
gba_file = open('gettysburg.txt', 'r') #pulling in txt file
counts = dict() #creating the dictionary
for line in gba_file: #process_lines
    line = line.translate(str.maketrans('', '', string.punctuation)) #removing spaces and puntuation
    line = line.lower() #converting to lowercase
    words = line.split()
    for word in words:  #Counting the values in the dictionary
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)

# Print the occurrences
print('Length of Dictionary:', (len(counts)))
print('Count', 'Word')
for key, val in lst[:]:
    print(key, val)
