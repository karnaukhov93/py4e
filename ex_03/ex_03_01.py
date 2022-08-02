hrs = input('Введите отработанные часы: ')
rt = input('Введите ставку за час: ')
k = input('Введите повышающий коэфициент для переработки: ')

try :
    hrs, rt, k = float(hrs), float(rt), float(k)
    if hrs > 40 :
        pay = 40 * rt + (hrs - 40) * rt * k
        print('К оплате:', pay)
    else :
        pay = hrs * rt
        print('К оплате:', pay)
except :
    print('Ошибка! Вводите числовые значения.')
