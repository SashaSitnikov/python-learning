contacts = {'Anna': '+79785930611'}
while True:
    print('1. Добавить контакт')
    print('2. Найти контакт по имени')
    print('3. Удалить контакт')
    print('4. Показать все контакты')
    print('0. Выход')
    choice = input('Выберите действие: ')
    print()
    
    if choice == '1':
        name = input('Введите имя контакта: ')
        phone = input('Введите его номер телефона: ')
        contacts[name] = phone
        print('Контакт добавлен! \n')
    elif choice == '2':
        name = input('Введите имя контакта: ')
        print(contacts.get(name, 'Контакт не найден! \n'))
    elif choice == '3':
        name = input('Введите имя контакта: ')
        contacts.pop(name)
        print('Контакт удален! \n')   #не стал обрабатывать ошибку, если контакта нет, т к плохо знаю try catch
    elif choice == '4':
        for key, value in contacts.items():
            print(key, value)
        print()
    elif choice == '0':
        break
    else:
        print('Неверный выбор! \n')
        



