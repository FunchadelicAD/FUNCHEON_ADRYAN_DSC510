'''
Name - Adryan Funcheon
Date - 03/25/2019
Course - DSC - 510, Intro to Programming
File - Assignment 4.1
Purpose - Create a program using funcitons with 2 variables requesting the amount of fiber optic cable to be installed and applying a
 "bulk rate" and outputting the costs and receipt.
'''

# Greeting and product inputs to calculate installation costs
print("Hello, and welcome to Frankies fiber optic warehouse!")
company_name = str(input('Please enter your company name so we can better assist you?\n'))
print('Great! Thank you,', company_name)

#validate numeric value of requested input
ft = input('Please enter the amount of fiber optic cable you need installed.\n')
try:
    ft = int(ft)
except:
    print('Please enter a numeric value.')


# Bulk discount cost tiers
tiers = float[.87, .80, .70, .50 ]

def bulk_cost():
    if ft <= 100:
        return tiers[0]

    elif ft <= 250:
        return tiers[1]

    elif ft <= 500:
        return tiers[2]

    elif ft >= 501:
        return tiers[3]

def calc_cost(ft, bulk_cost):
    cost = float(ft * bulk_cost())
    return cost

def reciept():
    print('Thank you, your order has been processed.\n')
    print('Company:', company_name)
    print('Fiber optic cable ordered (ft):',ft )
    print('Your calculated cost:', ft, 'x', bulk_cost())
    print('Your total installation cost: $', format(calc_cost(ft,bulk_cost),",.2f"))

print(reciept())


