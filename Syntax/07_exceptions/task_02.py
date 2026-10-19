def divide(a, b):
    try:
        result = a / b 
    except ZeroDivisionError:
        return None
    except TypeError as e:
        print(f"Некорректные данные: {e}")
    else:
        return result
        
print(divide("10", 2))
print(divide(10, 0))
print(divide(10, 2))