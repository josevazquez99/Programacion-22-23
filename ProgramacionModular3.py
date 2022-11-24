'''
Created on Nov 23, 2022

@author: estudiante
'''
#Ejercicio 1
caracter="".upper()
cadena="Hola Maria".upper()
def characterInString(caracter):
    contador=0
    for i in cadena:
        if caracter==i:
            contador+=1
    return contador
print(characterInString("A"))

#Ejercicio 2
cadena="Hola Maria"
def lowCaseInString ():
    contador=0
    for i in cadena:
        if i==i.lower() and i!=" ":
            contador+=1
    return contador
print(lowCaseInString())

#Ejercicio 3

cadena="Hola Maria"
def upperCaseInString ():
    contador=0
    for i in cadena:
        if i==i.upper() and i!=" ":
            contador+=1
    return contador
print(upperCaseInString())

#Ejercicio 4
cadena="Hola Maria 1970"
def numberInString():
    numeros=str([0,1,2,3,4,5,6,7,8,9])
    contador=0
    for i in cadena:
        if i in numeros and i!=" ":
            contador+=1
    return contador
print(numberInString())

#Ejercicio 5
cadena="anilina"
def palindrome():
    cierto=False
    if cadena==cadena[::-1]:
        cierto=True
    return cierto
print(palindrome())

#Ejercicio 6
cadena="shybaoxlna"
palabra="hola"
def buscarPalabraEscondida():
    encontrado=False
    for i in cadena:
        for j in palabra:
            if i==j:
                encontrado=True
    return encontrado
print(buscarPalabraEscondida())

#Ejercicio 7
cadena="Mo moto ol pono doroponto"
letraBuscar="o"
letraCambiar="e"

cadena.replace(letraBuscar, letraCambiar)        







