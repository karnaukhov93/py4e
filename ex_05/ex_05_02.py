l = list()

while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        x = float(x)
        l.append(x)
    except:
        print('Invalid input')

# Вывод суммы, количества, среднего значения, максимума и минимума с помощью цикла
summa = 0
count = 0
try:
    max = l[0]
    min = l[0]
except:
    print('No data')
    quit()

for number in l:
    count = count + 1
    summa = summa + number
    if number > max:
        max = number
    if number < min:
        min = number

average = summa / count
print('Sum:', summa)
print('Count:', count)
print ('Average:', average)
print('Max:', max)
print('Min:', min)

# Вывод суммы, количества, среднего значения, максимума и минимума с помощью встроенных функций
#print('Sum:', sum(l), end = '\n')
#print('Count:', len(l), end = '\n')
#print('Average:', sum(l)/len(l), end = '\n')
# print('Max:', max(l), end = '\n')
# print('Min:', min(l), end = '\n')
