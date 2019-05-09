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

# Pull in text and read text file, process and clean up the file
# so words can be counted.
def main():
    import string
    counts = dict()
    gba_file = open('gettysburg.txt', 'r')

    for line in gba_file:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

                # Descending sort the dictionary by value
                def add_words():
                    lst = list()
                    for key, val in list(counts.items()):
                        lst.append((val, key))
                    lst.sort(reverse=True)
                    for key, val in lst[:]:
                        print(key, val)
                #Output of dictionary total, count, and word
                def print_pretty():
                    print('Length of Dictionary:', (len(counts)))
                    print('Count', 'Word')

    print_pretty()
    add_words()

if __name__ == "__main__":
    main()

