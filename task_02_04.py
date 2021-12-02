string = input('Введите несколько слов')
words = string.split()
for index, word in enumerate(words, 1):
    print(index, word[:10])




    