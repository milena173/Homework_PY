my_list = (input("Введите данные для списка через пробел")).split()
for index in range(0, len(my_list)-1, 2):
    my_list[index], my_list[index+1] = my_list[index+1], my_list[index]

print(my_list)
