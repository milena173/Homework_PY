seasons = {'Выбранный месяц зимний': (1, 2, 12),
           'Выбранный месяц весенний': (3, 4, 5),
           'Выбранный месяц летний': (6, 7, 8),
           'Выбранный месяц осенний': (9, 10, 11)}

month = int(input("Введите порядковый номер месяца (напр. 2)"))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)


# вариант 2
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = int(input("Введите порядковый номер месяца (напр. 2)"))
if month in winter:
    print(f'Выбранный месяц зимний')
elif month in spring:
    print(f'Выбранный месяц весенний')
elif month in summer:
    print(f'Выбранный месяц летний')
elif month in autumn:
    print(f'Выбранный месяц осенний')



