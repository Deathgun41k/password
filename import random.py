import random 

list = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('Скок паролей те нужно ?' + 'n')
dlina = input('Какая длина пароля ?' + 'n')
number = int(number)
dlina = int(dlina)
for n in range(number):
    password = ''
    for i in range(dlina):
        password += random.choice(list)
    print(password)
