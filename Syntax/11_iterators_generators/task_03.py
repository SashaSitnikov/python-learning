def countdown(n):
    while n > 0:
        print(f"[До yield] Сейчас отдадим число: {n}")
        yield n
        print(f"[После yield] Функция проснулась, уменьшаем {n}")
        n -= 1

c_test = countdown(3)

print(next(c_test))
print(next(c_test))

c_for = countdown(4)
for num in c_for:
    print(num)