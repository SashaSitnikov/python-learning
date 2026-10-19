def read_int(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Вы не ввели целое число, попробуйте еще раз!")
        else:
            print("Вы ввели целое число, спасибо!")
            return number
            
            
number = read_int("Пожалуйста, введите целое число: ")


