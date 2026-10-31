from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b    
        
print(list(islice(fibonacci(), 10)))

for num in fibonacci():
    if num > 1000:
        print(f"Найдено число: {num}")
        break
