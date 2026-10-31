from itertools import islice

def take(n, iterable):
    if n <= 0:
        return 
    for el in iterable:
        yield el
        n -= 1
        if n == 0:
            break
        
def paginate(items, size):
    page = []
    for el in items:
        page.append(el)
        if len(page) == size:
            yield page
            page = []
    if page:
        yield page
        
def numbers(start=1):
    while True:
        yield start
        start += 1
        
def only_even(iterable):
    for el in iterable:
        if el % 2 == 0:
            yield el
            
def squares(iterable):
    for el in iterable:
        yield el ** 2

result = take(5, squares(only_even(numbers())))
print(list(result))

print(list(paginate(range(10), 3)))
print(list(islice(paginate(numbers(), 4), 4)))