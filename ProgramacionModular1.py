'''
Created on Nov 4, 2022

@author: estudiante
'''
# Ejercicio 1
from random import randint
lista=[]
for i in range(10):
    lista.append(randint(0,1000))
print(lista)

# def obtenerMayor(lista):
#     mayor=lista[0]
#     for i in range(len(lista)):
#         if lista[i]>mayor:
#             mayor=lista[i]
#     return mayor
#
# print("El mayor es " ,obtenerMayor(lista))     
#
# def obtenerMenor(lista):
#     menor=lista[0]
#     for i in range(len(lista)):
#         if lista[i]<menor:
#             menor=lista[i]
#     return menor
# print("El menor es ",obtenerMenor(lista))   
#
def obtenerSuma(lista):
    contador=0
    for i in range(len(lista)):
        contador+=lista[i]
    return contador
print("La suma es ",obtenerSuma(lista))
#
# def obtenerMedia(lista):
#     contador=0
#     media=0
#     for i in range(len(lista)):
#         contador+=lista[i]
#         media=contador/10
#     return media
# print("La media es ",obtenerMedia(lista))

# def sustituirImprimirListaCambiada(lista):
#     numeroSustituido=int(input("Indica la posicion empezando desde 0"))
#     numero=int(input("Introduce el numero nuevo"))
#     lista[numeroSustituido]=numero
#     return lista
# print(sustituirImprimirListaCambiada(lista))

#Ejercicio 2
# def imprimirLista():
#     lista=[]
#     contador=0
#     while contador<10:
#         numero=int(input("Introduce un numero"))
#         contador+=1
#         lista.append(numero)
#     for i in range(len(lista)):
#
#
#     return lista 
# print(imprimirLista())


    

        