'''
Name - Adryan Funcheon
Date - 04/14/2019
Course - DSC - 510, Intro to Programming
File - Assignment 5.1
Purpose - Create a program using for and while loops. The program will include an average function and a calculator function
based on the the values users input and the calculation operator chosen.

'''


def calculateAverage():
    print('Welcome to the average function!')
    #ask for the nubmer values to be entered
    vals = int(input("Enter the number of values you want evaluated: "))
    valList = []

    for i in range(0, vals):    #evaluate the number of values requested
        nums = int(input("Enter a number: "))
        valList.append(nums) #append each number/value to list to be evalueated
    avg = sum(valList) / vals
    print("Awesome! The average of values you entered is:", round(avg, 2))

calculateAverage()

#perform a calculation based on the operator and two valued defined by user, loop back if user wants to do a new calc.
def performCalculation():
    loop = "y"
    while loop.lower() == "y": #return loop in lowercase
        print('Welcome to the calc function!')
        print("Select operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

        choice = input("Enter choice(1, 2, 3, or 4):") #

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", (num1 + num2))

        elif choice == '2':
            print(num1, "-", num2, "=", (num1 - num2))

        elif choice == '3':
            print(num1, "*", num2, "=", (num1 * num2))

        elif choice == '4':
            print(num1, "/", num2, "=", (num1 / num2))
        else:
            print("Invalid input")
        loop = input("Do you want to try another? y/n:")
        if loop == "n":
            print('Thanks for trying out our calculator function. Goodbye!')
            break
performCalculation()