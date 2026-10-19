def f():
    try:
        return "try"
    finally:
        print("finally")

print(f())

def g(x):
    try:
        print("A")
        result = 10 / x
        print("B")
    except ZeroDivisionError:
        print("C")
    else:
        print("D")
    finally:
        print("E")
    print("F")

g(2)
g(0)
