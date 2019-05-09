'''
Name - Adryan Funcheon
Date - 04/04/2019
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


#apply bulk discount rate "tier" using the ft input
def bulk_cost():

    tiers = [.87, .80, .70, .50] # Bulk discount cost tiers
    if ft <= 100:
        return tiers[0]

    elif ft <= 250:
        return tiers[1]

    elif ft <= 500:
        return tiers[2]

    elif ft >= 501:
        return tiers[3]

#determine costs using bulk discount entered from customer
def calc_cost(ft, bulk_cost):
    cost = float(ft * bulk_cost())
    return cost

#output receipt to customer
print('Thank you, your order has been processed.\n')
print('Company:', company_name)
print('Fiber optic cable ordered (ft):',ft )
print('Your calculated cost:', ft, 'x', format(bulk_cost(),',.2f'))
print('Your total installation cost: $', format(calc_cost(ft,bulk_cost),",.2f"))




