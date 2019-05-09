#def hello_function (userName):
 #   print('hllow', userName, 'welcom to fiber store')

#userName = input('what is yoiur name?:\n')
#hello_function(userName)

print("Welcome to Dianna\'s Fiber Optic Cable Sales! \nPlease fill out the order form below.\n")  # welcome message
company_name = input("What's the name of your company?\n")  # user input for company name with linebreak
length = input("How many feet of fiber optic cable would you like to install?\n")  # user input for no. feet of product
length = length.replace(',', '')  # get rid of user input commas
new_length = int(length)
pricing = [0, .87, .80, .70, .50]


def calculate_cost(new_length, specific_pricing):
    cost = (new_length * specific_pricing())
    return cost


def specific_pricing():
    if new_length < 100:
        return pricing[1]

    elif 250 > new_length >= 100:
        return pricing[2]

    elif 500 > new_length >= 250:
        return pricing[3]

    elif new_length >= 500:
        return pricing[4]



print(calculate_cost(new_length, specific_pricing))
