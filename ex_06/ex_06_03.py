
def counter(string, letter):
    count = 0
    for letter_in_string in string:
        if letter_in_string == letter:
            count = count + 1
    return count

s = input('Введите строку: ')
l = input('Введите букву: ')

print(counter(s, l))
