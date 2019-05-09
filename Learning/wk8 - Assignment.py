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

# Sort the dictionary by value
def add_word(list):
    lst = list()
    for key, val in list(counts.items()):
        lst.append((val, key))
def print_pretty(lst):
    lst.sort(reverse=True)
    print('Length of dictionary:',sum(counts.values()))
    print('Count', 'Word')

    for key, val in lst[:]:
        print(key, val)

def main():
    process_line()
    add_word()



