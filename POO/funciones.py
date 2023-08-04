import random

def punto1():
    nombre = input("Ingrese su nomnbre: ")
    edad = int(input("Ingrese su edad: "))
    print("Hola",nombre,"," "tienes", edad, "años")

def punto2():
    radio = int(input("Ingrese el radio del círculo: "))
    area = (radio**2) * 3.1416
    print("El área es: ", area)

def punto3():
    aleatorios=[]
    for i in range (5):
        aleatorios.append(random.randint(1,99))
    print(aleatorios)

def punto4():
    num = int(input("Ingrese un número: "))
    if num%2 == 0:
        print("El número es par")
    else:
        print("Es impar")

def punto5():
    f = float(input("Ingrese los grados en Fahrenheit: "))
    c = (f-32)/1.8
    print(c)

def punto6():
    lista=[]
    suma=0
    for i in range(5,0,-1):
        num = int(input("Ingrese números para una lista: "))
        lista.append(num)
        suma += num
    print(lista)
    print("La suma de los números es:", suma)

def punto7():
    lista=[]
    for i in range(5):
        num = int(input("Ingrese números para una lista: "))
        lista.append(num)
    lista.sort()
    print("El número más pequeño es: ",lista[0])
    print("El número más grande es: ",lista[-1])

def punto8():
    lista=[]
    listainversa=[]
    for i in range(5):
        num = int(input("Ingrese números para una lista: "))
        lista.append(num)
    for j in range(1,len(lista)+1,1):
        listainversa.append(lista[-j])
    print(lista)
    print(listainversa)
        
def punto9():
    matriz=[]
    for i in range(5):
        filas=[]
        for j in range(5):
            filas.append(random.randint(1,99))
        matriz.append(filas)
    print(matriz)

def punto10():
    num=int(input("Ingrese un número: "))
    for i in range(num-1,1,-1):
        num=num*i
    print("El factorial es: ",num)

def punto11():
    lista_pares=[]
    for i in range(10):
        num=random.randint(0,100)
        if num % 2 == 0:
            lista_pares.append(num)
    print(lista_pares)

def punto12():
    for i in range(1,11):
        print(i)

def punto13():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    suma= num1+num2
    resta=num1-num2
    mult=num1*num2
    divi=num1/num2
    print("La suma de los números es", suma)
    print("La resta de los números es", resta)
    print("La multiplicación de los números es", mult)
    print("La división de los números es", divi)

def punto14():
    suma=0
    lista=[]
    for i in range(5):
        num = int(input("Ingrese números para una lista: "))
        lista.append(num)
        suma += num
    media=suma/len(lista)
    print("La media aritmética es: ", media)

def punto15():
    world= input("Ingrese una palabra: ")
    palindromo=world[::-1]
    if palindromo == world:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
