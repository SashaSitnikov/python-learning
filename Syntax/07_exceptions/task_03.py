try:
    int("sdd")
except ValueError as e:
    print(f"{type(e).__name__}: {e}")
    
try:
    "20" + 3
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
    
try:
    d = {}
    d["x"]
except KeyError as e:
    print(f"{type(e).__name__}: {e}")
    
try:
    lst = [1, 2]
    lst[3]
except IndexError as e:
    print(f"{type(e).__name__}: {e}")
    
try:
    3 / 0
except ZeroDivisionError as e:
    print(f"{type(e).__name__}: {e}")
    
try:
    with open("sdfdsf.txt", "r", encoding="utf-8") as f:
        pass
except FileNotFoundError as e:
    print(f"{type(e).__name__}: {e}")
