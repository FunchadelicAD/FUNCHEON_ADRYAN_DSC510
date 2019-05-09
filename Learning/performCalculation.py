def calculateAverage():
    print('Welcome to the average function!')
    vals = int(input("Enter the number of values you want evaluated: "))
    valList = []

    for i in range(0, vals):
        nums = int(input("Enter a number: "))
        valList.append(nums)
    avg = sum(valList) / vals
    print("Awesome! The average of values you entered is:", round(avg, 2))

calculateAverage()


def performCalculation():
    loop = "y"
    while loop.lower() == "y":
        print('Welcome to the calc function!')
        print("Select operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

        choice = input("Enter choice(1, 2, 3, or 4):")

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

