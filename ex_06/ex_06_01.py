# Запись строки наоборот

string = input('Введите строку: ')

# Вариант 1
#index = len(string)

#while index <= len(string) and index >= 1:
#    print(string[index-1])
#    index = index-1

# Вариант 2
for char in string:
    string = char + string

string = string[:int(len(string)/2)]

print(string)
