'''
shoplist = ['cat', 'dog','ferret']
myIndex = input('enter a index:')
myIndex = int(myIndex)
myElement = shoplist[myIndex]
print('the element at index', myIndex, 'is,', myElement)

'''


'''
values =  ['cat', 'dog','ferret']

for i in range(len(values)):
    print(i, values[i])
'''
'''
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
'''
'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
'''
'''
word = 'banana'
if word < 'banana':
    print('word', word, ' after')
elif word > 'banana':
    print('word', word, ' whatevs')
else:
    print('fuck yeah, bananas!')
'''
'''
word = 'banana'
new_word = word.upper()
print(new_word)
'''
'''
camels = 43
'%d' % camels
print(camels)
'''
cheeses = ['cheddar', 'edam', 'gouda']
for cheese in cheeses:
    print(cheese)
