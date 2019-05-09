def menu():
    # print what options you have
    print('Welcom to calculator')
    print ('your options are')
    print ("1 Add")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")

    return input("Choose your option: ")


# this adds two numbers given
def add(a, b):
    print
    a, "+", b, "=", a + b


# this subtracts two numbers given
def sub(a, b):
    print
    b, "-", a, "=", b - a


# this multiplies two numbers given
def mul(a, b):
    print
    a, "*", b, "=", a * b


# this divides two numbers given
def div(a, b):
    print
    a, "/", b, "=", a / b


# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == '1':
        add(input("Add this: "), input("to this: "))
    elif choice == '2':
        sub(input("Subtract this: "), input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "), input("by this: "))
    elif choice == 4:
        div(input("Divide this: "), input("by this: "))
    elif choice == 5:
        loop = 0

print("Thankyou for using calculator.py!")

# NOW THE PROGRAM REALLY FINISHES