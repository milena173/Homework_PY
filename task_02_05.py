my_list = [7, 5, 3, 3, 2]
my_list_copy = my_list.copy()

x = int(input("Введите число"))
if x > my_list[0]:
    my_list_copy.insert(0, x)
elif x < my_list[-1]:
    my_list_copy.append(x)
else:
    for y in my_list:
        if x == y:
                x_index = my_list.index(y)
                my_list_copy.insert(x_index, x)
                break
        elif x > y:
                my_list_copy.insert(my_list.index(y), x)
                break
print(my_list_copy)