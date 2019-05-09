'''
def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)


#print(hello_func('hi', name = 'Bob'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'Bob', age = 21)

#DRY - don't repeat yourself

import random

for i in range(10):
     x = random.random()
     print(x)
'''
'''
def greet_customer(company_name):
    print("Great, thank you", company_name)

company_name = str(input('Hello and welcome to the Fiber Optic Farm. Please enter your company name so we can better assist you?\n'))
greet_customer(company_name)


#validate numeric value of requested input
ft = input('Please enter the amount of fiber optic cable (ft) you need installed.\n')
try:
    ft = int(ft)
except:
    print('Please enter a numeric value.')
'''


def performCalculation():
    choice = input("Enter choice(add/sub/multi/div):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    cont = 'y'
    while cont.lower() == "y":

        if choice == 'add':
            print(num1, "+", num2, "=", (num1 + num2))
        elif choice == 'sub':
            print(num1, "-", num2, "=", (num1 - num2))
        elif choice == 'multi':
            print(num1, "*", num2, "=", (num1 * num2))
        elif choice == 'div':
            print(num1, "/", num2, "=", (num1 / num2))
        else:
            print("Invalid input")
        cont = input("Continue?y/n:")
        if cont == "n":
            break
performCalculation()
