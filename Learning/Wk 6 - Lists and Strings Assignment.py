'''
Name - Adryan Funcheon
Date - 04/21/2019
Course - DSC - 510, Intro to Programming
File - Assignment 6.1
Purpose - Create a program taking in a list of temperatures inputted by a user.
The user will enter in a sentinal value to break the loop.

'''

count = 0
temperatures = []
while (True):
    nums = int(input('Enter a temperature. Enter 00 when finished:'))
    if nums == 00:  #sentinal value to break the loop
        break
    value = int(nums)
    count = count + 1 # incrementally count values entered by user
    temperatures.append(nums) # add values to the temperature list
    temperatures.sort() # sort values Ascending.

print('Here\'s a list of the temperatures entered:',temperatures, "\n"
 "You entered total of", count,'temperatures.')
print('Your MAX temp is:', max(temperatures))
print('Your MIN temp is:', min(temperatures))
