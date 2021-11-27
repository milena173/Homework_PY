a = int(input("Введите сумму выручки: "))
b = int(input("Введите сумму издержек : "))
if a > b:
     profit = a - b
     rent = profit/a
     print(f" Ваша прибыль равна {profit}")
     print (f" Ваша рентабельность составляет {rent}")
     employees = int(input("Введите количетсво сотрудников: "))
     print(f"Один сотрудник вам приносит {profit/employees} прибыли")
elif a == b:
     print("Ваша прибыль равна нулю")
else:
     print("Ваша фирма работает в убыток")
     print(f" Ваш убыток {b-a}")