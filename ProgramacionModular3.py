'''
Created on Nov 23, 2022

@author: estudiante
'''
#Ejercicio 1
# caracter="".upper()
# cadena="Hola Maria".upper()
# def characterInString(caracter):
#     contador=0
#     for i in cadena:
#         if caracter==i:
#             contador+=1
#     return contador
# print(characterInString("A"))

#Ejercicio 2
# cadena="Hola Maria"
# def lowCaseInString ():
#     contador=0
#     for i in cadena:
#         if i==i.lower() and i!=" ":
#             contador+=1
#     return contador
# print(lowCaseInString())

#Ejercicio 3

# cadena="Hola Maria"
# def upperCaseInString ():
#     contador=0
#     for i in cadena:
#         if i==i.upper() and i!=" ":
#             contador+=1
#     return contador
# print(upperCaseInString())

#Ejercicio 4
# cadena="Hola Maria 1970"
# def numberInString():
#     numeros=str([0,1,2,3,4,5,6,7,8,9])
#     contador=0
#     for i in cadena:
#         if i in numeros and i!=" ":
#             contador+=1
#     return contador
# print(numberInString())

#Ejercicio 5
# cadena="anilina"
# def palindrome():
#     cierto=False
#     if cadena==cadena[::-1]:
#         cierto=True
#     return cierto
# print(palindrome())

#Ejercicio 6
# cadena="shybaoxlna"
# palabra="hola"
# def buscarPalabraEscondida():
#     encontrado=False
#     for i in cadena:
#         for j in palabra:
#             if i==j:
#                 encontrado=True
#     return encontrado
# print(buscarPalabraEscondida())

#Ejercicio 7
def sustituir(cadena,palabra,sustituta):
    resultado,tmp="",""
    ipalabra=0
    for i in range(len(cadena)):
        
        
        if cadena[i]==palabra[ipalabra]:
            tmp+=palabra[ipalabra]
            ipalabra+=1
            
            if len(palabra)==ipalabra:
                ipalabra=0
                
                tmp=""
                resultado+=sustituta
                
                #sustituir
        
            
        else:
            resultado+=tmp+cadena[i]
            ipalabra=0
    
    return resultado

print(sustituir("la bicicleta esta nueva", "nueva", "vieja"))

#Ejercicio 8 
# vocales=['a','e','i','o','u']
# palabra=""
# listaSinRepetir=[]
# def obtenerVocales(palabra):
#     contador=0
#     for i in palabra:
#         if i.lower() in "aeiou":
#             listaSinRepetir.append(i)
#     for j in listaSinRepetir:
#         if j!=i:
#             contador+=1
#
#     return contador
# print(obtenerVocales("Abaco"))

#Ejercicio 9
#
# def ponerUltimasVocales(cadena):
#     separadorConsonante=""
#     separadorVocal=""
#     for i in cadena:
#         if i.lower() in "aeiou":
#             separadorVocal+=i
#         elif i==" ":
#             separadorVocal+="" 
#         else:
#             separadorConsonante+=i
#
#     return separadorConsonante+separadorVocal
# print(ponerUltimasVocales("curso de programacion"))

#Ejercicio 10
# def obtenerNumeroPalabras(cadena):
#     contador=0
#     if cadena[0]!=" ":
#         contador+=1
#     for i in range(len(cadena)-1):
#         if cadena[i]==" " and cadena[i+1] !=" ":
#             contador+=1
#     return contador
#
# print(obtenerNumeroPalabras(" He estudiado mucho "))
        







