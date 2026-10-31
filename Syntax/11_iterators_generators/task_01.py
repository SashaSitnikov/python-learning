lst = [10, 20, 30]
it = iter(lst)

print(next(it), next(it), next(it))
try:
    print(next(it)) 
except StopIteration:
    print(f"Ошибка")

obj = [1, 2, 3]
it_two = iter(obj)
while True:
    try:    
        x = next(it_two)
        print(x)
    except StopIteration:
        break