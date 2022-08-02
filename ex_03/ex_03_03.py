scr = input('Введите значение: ')

try :
    scr = float(scr)
except :
    print('Плохое значение')
    quit()

scr = float(scr)
if scr >= 0 and scr < 0.6 : print('F')
elif scr < 0.7 : print('D')
elif scr < 0.8 : print('C')
elif scr < 0.9 : print('B')
elif scr <= 1.0 : print('A')
else : print('Плохое значение')
