#31 Создайте пустой словарь. Запустите цикл который...
a = {}
i = 0
for i in range(0,3):
    b = input("Введите имя: ")
    c = input("Введите пароль: ")
    a[b] = c
print('Ваши попытки: ', a)
