from funciones import *

while True:
    opcion= int(input("Ingrese un número del 1 al 15 para realizar el punto que corresponde y escriba x para salir   "))
    if opcion==1:
        punto1()
    elif opcion==2:
        punto2()
    elif opcion==3:
        punto3()
    elif opcion==4:
        punto4()
    elif opcion==5:
        punto5()
    elif opcion==6:
        punto6()
    elif opcion==7:
        punto7()
    elif opcion==8:
        punto8()
    elif opcion==9:
        punto9()
    elif opcion==10:
        punto10()
    elif opcion==11:
        punto11()
    elif opcion==12:
        punto12()
    elif opcion==13:
        punto13()
    elif opcion==14:
        punto14()
    elif opcion==15:
        punto15()
    elif opcion=="x":
        break
    else:
        print("Ese número no es válido")