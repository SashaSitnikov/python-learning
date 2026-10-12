funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
# выведет [2, 2, 2] из за того, что функция не запоминает переменную в момент создания(надеюсь, нормально объяснил)

# исправление
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])