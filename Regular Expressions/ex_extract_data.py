filename = input('Введите имя файла: ')
f = open(filename)
count = 0
l = list()

import re

for string in f:
    if re.search('[0-9]+', string) :
        x = re.findall('[0-9]+', string)
        for num in x:
            l.append(int(num))
print(len(l))
print(sum(l))
