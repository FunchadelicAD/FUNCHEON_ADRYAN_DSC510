
'''
language = str(input('what language do you speak?:'))

if language == 'Spanish':
    print('Bob speaks a second lang')
elif language == 'Murican':
    print ('Bob speaks Murican')
elif language == 'Stupid':
    print('duuuh!')
else:
    print('nada!')
'''
# Greeting and product inputs to calculate installation costs
print("Hello, and welcome to Frankies fiber optic farmhouse!")

company_name = str(input('Please enter your company name so we can better assist you?\n'))
print('Great! Thank you,', company_name)

#validate numeric value of requested input
ft = input('Please enter the amount of fiber optic cable you need installed.\n')
try:
    ft = int(ft)
except:
    print('Please enter a numeric value.')

# request to upsell customer if under 100 ft.
if (ft <= 99):
    upsell = input('We offer a discounts for purchases over 100ft. Do you want to change your order?:\n')
    print(upsell)
    if (upsell == 'Y' or upsell == 'yes' or upsell == 'Yes' ):
        ft_upsell = input('Please enter the amount of fiber optic cable you need installed:\n')
        print(ft_upsell)
    else:
        print('Not a problem. Let\'s get you checked out then')

# Bulk discount cost tiers
t1FiberOptic = float(ft * .87)
t2FiberOptic = float(ft * .8)
t3FiberOptic = float(ft * .7)
t4FIberOptic = float(ft * .5)


#Apply 'Bulk Rate teir' based on 'ft'. Outputting customer reciept w/requested amount and costs
if (ft <= 100):
    print('Thank you. Your order has been processed.\n'
      'Below you will find your receipt:\n'
      '****Business name:',company_name,'\n'
            '****Fiber optic cable orderd (ft):', ft,'\n'
                '****Calculated cost:',ft,'x $.87\n'
                    '****Total installation cost: $',format(t1FiberOptic, ",.2f"),
      '\n Thank you for your order!')
elif (ft <= 250):
    print('Thank you. Your order has been processed.\n'
      'Below you will find your receipt:\n'
      '****Business name:',company_name,'\n'
            '****Fiber optic cable (ft):',ft,'\n'
                '****Calculated cost:' ,ft,'x .80\n'
                    '****Total installation cost: $',format(t2FiberOptic,",.2f"),
      '\n Thank you for your order!')
elif (ft <= 500):
    print('Thank you. Your order has been processed.\n'
      'Below you will find your receipt:\n'
      '****Business name:',company_name,'\n'
            '****Fiber optic cable (ft):',ft,'\n'
                '****Calculated cost:',ft,'x .70\n'
                    '****Total installation cost: $',format(t3FiberOptic,",.2f"),
      '\n Thank you for your order!')
elif (ft >= 501):
    print('Thank you. Your order has been processed.\n'
      'Below you will find your receipt:\n'
      '****Business name:',company_name,'\n'
            '****Fiber optic cable (ft):',ft,'\n'
                '****Calculated cost:',ft,'x .50\n'
                    '****Total installation cost: $',format(t4FIberOptic,",.2f"),
      '\n Thank you for your order!')
