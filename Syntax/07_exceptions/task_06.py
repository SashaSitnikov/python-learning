try:
    int("abc")
except ValueError:
    print(1)
except Exception:
    print(2)

try:
    1 / 0
except ZeroDivisionError:
    print(1)
except ArithmeticError:
    print(2)