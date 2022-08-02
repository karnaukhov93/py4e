def check(x):
    try :
        x = float(x)
    except :
        print('Ошибка! Вводите числовое значение.')
        quit()

hrs = input('Введите отработанные часы: ')
check(hrs)
rt = input('Введите ставку за час: ')
check(rt)
k = input('Введите повышающий коэфициент для переработки: ')
check(k)

hrs, rt, k = float(hrs), float(rt), float(k)
if hrs > 40 :
    pay = 40 * rt + (hrs - 40) * rt * k
    print('К оплате:', pay)
else :
    pay = hrs * rt
    print('К оплате:', pay)
