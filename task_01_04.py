n = int(input('Введите любое число'))
mn=0
while n > 0:
    c=n%10
    if c >= mn : mn = c
    n//=10
print(mn)