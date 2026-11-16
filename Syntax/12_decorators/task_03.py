def shout(func):
    print("start")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def greet(name):
    return f"Привет, {name}"

greet = shout(greet)
print(greet("Аня"))

@shout
def greet_two(name):
    return f"привет, {name}"
print(greet_two("Alex"))