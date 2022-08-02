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

# Вывод суммы, количества, среднего значения с помощью встроенных функций
print('Sum:', sum(l), end = '\n')
print('Count:', len(l), end = '\n')
print('Average:', sum(l)/len(l), end = '\n')
