name = "Jackie"
food = "burger"

print('Hey {name}, that {food} is ready!'.format(name= name, food = food))

a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')


def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

print(greet('Jackie', 'going'))