# help (__builtins__)

# help('modules')

# import sys
# print(sys.builtin_module_names)
'''
def arg_three(one, two, *args):
    print(one)
    print(two)
    for stuff in args:
        print(stuff)

my_list = ['honda', 'toyota','BMW','ford','chevy']

arg_three('Required 1','Required 2', *my_list)
'''


def kwarg_one(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)


d_example = {'Key1': 'Value1', 'Key2': 'Value2', 'Key3': 'Value3'}
kwarg_one(**d_example)
#kwarg_one(Key1 = 'Value1', key2 = 'Value2', Key3 = 'Value3')

