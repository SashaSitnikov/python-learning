def add_contact(name, phone):
    contacts[name] = phone
    print('Контакт добавлен! \n')

def find_contact(name):
    print(contacts.get(name, 'Контакт не найден! \n'))

def delete_contact(name):
    contacts.pop(name)
    print('Контакт удален! \n')

def show_all_contacts():
    for key, value in contacts.items():
        print(key, value)
    print()

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
        add_contact(name, phone)
        
    elif choice == '2':
        name = input('Введите имя контакта: ')
        find_contact(name)
        
    elif choice == '3':
        name = input('Введите имя контакта: ')
        delete_contact(name)
        
    elif choice == '4':
        show_all_contacts
    elif choice == '0':
        break
    else:
        print('Неверный выбор! \n')