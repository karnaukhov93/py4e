while True:
    scr = input('Введите значение: ')

    try :
        scr = float(scr)
    except :
        print('Плохое значение')
        quit()

    def computegrade(x):
        x = float(x)
        if x >= 0 and x < 0.6 : print('F')
        elif x < 0.7 : print('D')
        elif x < 0.8 : print('C')
        elif x < 0.9 : print('B')
        elif x <= 1.0 : print('A')
        else : print('Плохое значение')

    computegrade(scr)
