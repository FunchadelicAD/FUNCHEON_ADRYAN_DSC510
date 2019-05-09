'''
target = input('Enter a target number: ')
target = int(target)
total = 0
nextNumberToAddIn = 1
while nextNumberToAddIn <= target:
# add in the next value
    total = total + nextNumberToAddIn #add in the next number
    print('Added in:', nextNumberToAddIn, 'Total so far is:', total)
nextNumberToAddIn = nextNumberToAddIn + 1

print('The sum of the numbers from 1 to', target, 'is:', total)
'''

'''
sum = 0
current = 1
n = input('Enter value: ')
while current  <=  int(n):
    sum = sum + current
    print("Sum: ", sum)
    current = current + 1
    print("Current: ", current)
'''
'''
x = input('Wanna run the program, "y" ')

while x != 'Y':
    x = input("Enter 'Y' to run")
    if x == 'Y':
        print('You ran it!')

'''

'''
def calculateAverage(avg):
    numValues = int(input("enter numbers:"))
    listValues = []
    for i in range(0,numValues):
        entValue = int(input('Enter value: '))
        listValues.append(entValue)
    avg=sum(listValues)/numValues
    return avg
print('Average of values entered', round(avg,2))
'''

def performCalculation():
    calcFunc = str(input('Enter the function you want preformed: ', funcTypes))
    funcTypes = [add, sub, div, multi, avg]
    print(calcFunc)
    return funcTypes
