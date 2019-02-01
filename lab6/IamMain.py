import square
import rectangle
import circle

# ---------methods-------------------
def change(WhatTheVariable):
    """check variable on correct type"""
    return   float(input(WhatTheVariable))



# ---------main----------------------
flag = True
while flag:
    print("1. круг")
    print("2. квадрат")
    print("3. прямоугольник")
    print("0. выход")
    WhatTheFigure = change("")
    if (WhatTheFigure == 1):
        R=0
        while R <= 0 :
            try :
                R = change("Введите радиус круга: ")
                func1 = lambda  R : print("площадь круга равна " + str(circle.circle(R).reckon())) if R > 0 else print("Радиус круга должен быть больше 0")
                func1(R)
            except ValueError:
                print('неверный формат строки')
                R = 0

    if(WhatTheFigure == 2):
        L = 0
        while L <=0 :
            try:
                L = change("Введите длину стороны: ")
                func2 = lambda L :  print("площадь квадрата равна: " + square.square(R).reckon()) if L>0 else print("Длина стороны должна быть больше 0")
                func2(L)
            except ValueError:
                print('неверный формат строки')
                L=0


    if(WhatTheFigure == 3):
        L0 = 0
        L1 = 0
        while L0 <=0 :
            try:
                L0 = change("Введите длину 1 стороны прямоугльника: ")
                func3 = lambda L0: print("Длина стороны должна быть больше 0") if L0 <= 0 else print("")
                func3(L0)
            except ValueError:
                print('неверный формат строки')
                L0 = 0

        while L1 <= 0 :
            try :
                L1 = change("Введите дину второй стороны прямоугольника: ")
                func4 = lambda L1 : print("Площадь прямоугльника равна " + str(rectangle.rectangle(L0,L1).reckon())) if L1 >0 else print("Длина стороны должна быть больше 0")
                func4(L1)
            except ValueError:
                print('неверный формат строки')
                L1 = 0

    if(WhatTheFigure == 0):
        flag = False