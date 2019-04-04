'''
def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)


#rint(hello_func('hi', name = 'Bob'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'Bob', age = 21)

#DRY - don't repeat yourself
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




