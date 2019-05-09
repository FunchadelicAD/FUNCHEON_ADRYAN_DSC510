# name = "Jackie"
# food = "burger"
#
# print('Hey {name}, that {food} is ready!'.format(name= name, food = food))
#
# a = 5
# b = 10
# print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')
#
#
# def greet(name, question):
#     return f"Hello, {name}! How's it {question}?"
#
# print(greet('Jackie', 'going'))

import string
gba_file = open('gettysburg.txt', 'r')  # pulling in txt file
counts = dict()  # creating the dictionary

def process_line(gba_file):
    for line in gba_file:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1