def greet(name):
    return f'Привет, {name}!'


def greet_print(name):
    print(f'Привет, {name}!')
    
    
x = greet('Alex')
y = greet_print('Claude')

print(x)
print(y)