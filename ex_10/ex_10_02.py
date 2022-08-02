filename = input('Введите имя файла: ')
file = open(filename)
counts = dict()
hours = list()

for string in file :
    if string.startswith('From ') :
        day = string.split()[4]
        time = string.split()[5]
        hour = time.split(':')[0]
        hours.append(hour)

for hour in hours :
    counts[hour] = counts.get(hour, 0) + 1

search = sorted(counts.items())

n = 0
for value in search:
    print(search[n][0], search[n][1])
    n = n + 1
