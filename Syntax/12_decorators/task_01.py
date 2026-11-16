def len_(func, value):
    return func(value)

word = "Hello"
print(len_(len, word))


lst = [str.upper, str.lower, str.title]
word = "Good night"
for el in lst:
    print(el(word))

def apply(func, value):
    return func(value)

def f():
    return "Hello"