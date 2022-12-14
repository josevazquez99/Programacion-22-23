'''
Created on Dec 2, 2022

@author: vazquez
'''
#Ejercicio 1 USUARIOS
# menu=('''
# 1.Guardar usuario
# 2.Logarse
# 3.Mostrar Nombres de usuarios
# 4.Salir
#
# ''')
# opcion=int(input("Introduce la opcion "))
# listaUsuario=[]
# listaContraseña=[]
# listaIntentosFallidos=[]
# contador=0
# MAXIMO=5
# while opcion!=4:
#     if opcion==1:
#             nombre=input("Introduce el nombre de usuario")
#             contraseña=input("Introduce la contraseña")
#             if contador<10:
#                 listaUsuario.append(nombre)
#                 listaContraseña.append(contraseña)
#             else:
#                 listaUsuario[contador%MAXIMO]=nombre
#                 listaContraseña[contador%MAXIMO]=contraseña
#                 contador+=1
#     elif opcion==2:
#         print("Bienvenido introduce tu usuario y contraseña para iniciar sesión. ")
#
#         usuario_existente=input("Introduce tu nombre de usuario: ")
#         contraseña_existente=input("Introduce la contraseña de tu usuario:")
#
#         if usuario_existente in listaUsuario and contraseña_existente in listaContraseña:
#             print("Inicio de sesión correcto.")
#
#         elif usuario_existente in listaUsuario and not contraseña_existente in listaContraseña:
#             for i in range(len(listaUsuario)):
#                 if listaUsuario[i] == usuario_existente:
#                     posicionUsuario = i
#
#             while listaIntentosFallidos[posicionUsuario] < 3 and (usuario_existente in listaUsuario) and not (contraseña_existente in listaContraseña):
#                 listaIntentosFallidos[posicionUsuario] += 1
#                 print("El usuario existe, pero la contraseña es incorrecta.")
#                 contraseña_existente=input("Introduce la contraseña de tu usuario:")
#
#             if contraseña_existente in listaContraseña:
#                 print("Inicio de sesión correcto.")
#
#             if listaIntentosFallidos[posicionUsuario] >= 3:
#                 print("Cuenta bloqueada, inténtalo de nuevo más tarde...")
#         else:
#             print("El usuarioo introducido no existe.")
#
#
#
#
#     else:
#         print(listaUsuario)
#
#     opcion=int(input("Introduce la opcion "))
#

    
#Ejercicio 2 CALCULO
#1. Write a Python program to calculate the sum of digits of a number.
def sumarDigitos(numero):
    numero=str(numero)
    total=0
    for n in numero:
        total=total+int(n)

    return total

assert(sumarDigitos(5)==5)
assert(sumarDigitos(12)==3)

# Write a Python program to compute the greatest common divisor (GCD) of two
#positive integers
def maximo_comun_divisor(numero1,numero2):
    divisores1=[]
    divisores2=[]
    comunes=[]
    for div1 in range(1,numero1+1):
        if numero1%div1==0:
            divisores1.append(div1)
    for div2 in range(1,numero2+1):
        if numero2%div2==0:
            divisores2.append(div2)

    for i in divisores1:
        if i in divisores2:
            comunes.append(i)

    return comunes[-1]

assert(maximo_comun_divisor(18,24)==6)

#Write a Python program to get the least common multiple (LCM) of two positive
#integers
def minimo_comun_multiplo(numero1,numero2):
    mcm=(numero1*numero2)/maximo_comun_divisor(numero1,numero2)
    return mcm

assert(minimo_comun_multiplo(18,24)==72)
        
#Write a Python program that accepts two integers (n and i) and computes the value
#of n+nn+nnn+....

def sumar_patron(numero1, numero2):
    suma=""
    for i in range(1,numero2+1):
        suma+=str(i*numero1)
    return int(suma)
   
assert(sumar_patron(2,3)==246)

#Ejercicio 5
def leer_fraccion(numerador,denominador):
    n=0
    if numerador>denominador:
        while n < numerador:
            n+=1
            if numerador%n==0 and denominador%n==0:
                numerador=numerador//n
                denominador=denominador//n
    return numerador,denominador


assert(leer_fraccion(16,6)==(8,3))

def escribir_fraccion(numerador,denominador):
    fraccion=0
    if denominador==1:
        print(numerador)
    else:
        print(f"{numerador}/{denominador}")

escribir_fraccion(16,6)


def simplificar_fraccion(numerador,denominador):
    numeradorsimp=numerador//maximo_comun_divisor(numerador,denominador)
    denominadorsimp=denominador//maximo_comun_divisor(numerador,denominador)
    return numeradorsimp, denominadorsimp

assert(simplificar_fraccion(16,6)==(8,3))

def sumar_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=(numerador1*denominador2)+(denominador1*numerador2)
    denominador=denominador1*denominador2
    return simplificar_fraccion(numerador,denominador)

def restar_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=(numerador1*denominador2)-(denominador1*numerador2)
    denominador=denominador1*denominador2
    return simplificar_fraccion(numerador,denominador)   

def multiplicar_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=numerador1*denominador1
    denominador=denominador1*denominador2
    return simplificar_fraccion(numerador,denominador)

def dividir_fraccion(numerador1,denominador1,numerador2,denominador2):
    numerador=numerador1*denominador2
    denominador=numerador2*denominador1
    return simplificar_fraccion(numerador,denominador)

#Ejercicio 6
opcion=""
pantalla="""
a. Sumar dos fracciones.
b. Restar dos pracciones.
c. Multiplicar dos fracciones.
d. Dividir dos fracciones.
e. Salir"""
while opcion != "e":
    print(pantalla)

    opcion=input("Introduzca una opcion: ").lower()

    if opcion=="a":
        print(sumar_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    elif opcion=="b":
        print(restar_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    elif opcion=="c":
        print(multiplicar_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    elif opcion=="d":
        print(dividir_fraccion(int(input("Introduzca numerador1: ")),int(input("Introduzca denominador1: ")),int(input("Introduzca numerador2: ")),int(input("Introduzca denominador2: "))))
    else:
        print("\nIntroduzca una opcion del menu")

#Ejercicio Figuras
def calcular_area_circulo(radio):
    PI=3.1416
    return f"{PI*(radio**2):.2f}"

def longitud_circulo(radio):
    PI=3.1416
    return f"{PI*(radio*2):.2f}"

def distancia_euclidea(x1,y1,x2,y2):
    return f"{(((x2-x1)**2)+((y2-y1)**2))**0.5:.2f}"

def perimetro_triangulo(x1,y1,x2,y2,x3,y3):
    return f"{((((x2-x1)**2)+((y2-y1)**2))**0.5)+((((x3-x2)**2)+((y3-y2)**2))**0.5)+((((x3-x1)**2)+((y3-y1)**2))**0.5):.2f}"


def area_triangulo(x1,y1,x2,y2,x3,y3):
    return f"{(((((x2-x1)**2)+((y2-y1)**2))**0.5)+((((x3-x2)**2)+((y3-y2)**2))**0.5)+((((x3-x1)**2)+((y3-y1)**2))**0.5))*0.5:.2f}"
