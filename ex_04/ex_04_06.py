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

def computepay(x, y, z):
    if x > 40 :
        pay = 40 * y + (x - 40) * y * z
        print('К оплате:', pay)
    else :
        pay = x * y
        print('К оплате:', pay)

computepay(hrs, rt, k)
