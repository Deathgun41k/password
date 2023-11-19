#meneger password

import random
import time

# Список паролей 
passwords = {}


# Функции 
def password_manager():
    print("Добро пожаловать в менеджер паролей!")


def show_password():
    for i in passwords:
        print(i, '-', passwords[i])


def delete_password():
    key = input('Какой ключ удалить? ')
    if key in passwords:
        del passwords[key]
        print(passwords)
    else:
        print("Указанный ключ не найден в списке паролей.")


def add_password():
    name = input('Введите название пароля: ')
    password = input('Введите пароль: ')
    passwords[name] = password
    print('Пароль', name, 'добавлен.')


def ganarate_random_password(length):
    random_1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!+-#&amp;amp;amp;amp;*'
    n = ''
    for i in range(length):
        n += random.choice(random_1)
    print(n)


password_manager()
while True:
    print('Выберите действие: ')
    print('1. Показать список паролей')
    print('2. Удалить пароль')
    print('3. Добавить пароль')
    print('4. Сгенерировать случайный пароль')
    print('5. Выход')
    choice = input('Введите номер действия: ')
    if choice == '1':
        show_password()
    elif choice == '2':
        delete_password()
    elif choice == '3':
        add_password()
    elif choice == '4':
        length = int(input("Введите длину пароля: "))
        ganarate_random_password(length)
    elif choice == '5':
        print('До свидания! =) ')
        break
    else:
        print('Ошибка. Попробуй ещё раз! =)')
    time.sleep(1)
