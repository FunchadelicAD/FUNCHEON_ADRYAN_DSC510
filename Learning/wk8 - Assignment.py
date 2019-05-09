import string
gba_file = open('gettysburg.txt', 'r') #pulling in txt file
counts = dict() #creating the dictionary
for line in gba_file: #process_lines
    line = line.translate(str.maketrans('', '', string.punctuation)) #removing spaces and puntuation
    line = line.lower() #converting to lowercase
    words = line.split()
    for word in words:  #add_words
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

def print_pretty():
    lst.sort(reverse=True)
    print('Length of dictionary:',sum(counts.values()))
    print('Count', 'Word')

    for key, val in lst[:]:
        print(key, val)
    return print_pretty()
