x = [1]
print(iter(x) is x)
x = "ab"
print(iter(x) is x)
x = {1: 2}
print(iter(x) is x)
x = range(3)
print(iter(x) is x)
x = map(str, [1])
print(iter(x) is x)
x = zip([1], [2])
print(iter(x) is x)
x = enumerate([1])
print(iter(x) is x)
x = (i for i in [1])
print(iter(x) is x)
x = open("text.txt")
print(iter(x) is x)

task = range(3)
print(list(task))
print(list(task))

task = map(str, [1, 2])
print(list(task))
print(list(task))