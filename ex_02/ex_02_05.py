celsius_temp = input('Введите температуру в градусах Цельсия: ')
try:
    kelvin_temp = float(celsius_temp) + 273.15
    print('Температура в градусах Кельвина:',kelvin_temp)
except:
    print('Ошибка! Введите значение.')
