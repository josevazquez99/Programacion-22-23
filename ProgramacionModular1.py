'''
Created on Nov 4, 2022

@author: estudiante
'''
# Ejercicio 1
# from random import randint
# lista=[]
# for i in range(10):
#     lista.append(randint(0,1000))
# print(lista)

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
# def obtenerSuma(lista):
#     contador=0
#     for i in range(len(lista)):
#         contador+=lista[i]
#     return contador
# print("La suma es ",obtenerSuma(lista))
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
#     print(lista)
#
#
#     a_borrar,a_escribir=0,0
#     for i in range(len(lista)):
#         a_borrar=lista[(i+1)%len(lista)]
#         lista[(i+1)%len(lista)]=a_escribir
#         a_escribir=a_borrar
#     return lista 
# print(imprimirLista())

#Ejercicio 3
# def es_bisiesto(year):
#     return (year%4==0 and (year%100!=0 or year%400==0))
#
# def es_fecha_valida(d, m, y):
#     dias_maximo_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     return (1<= d <= dias_maximo_por_mes[m-1]
#             or (es_bisiesto(y) and m==2 and 1<=d<=29)
#         )
#
# def transformar_fecha(day, month, year):
#     nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
#
#     if es_fecha_valida(day, month, year):
#
#         mes_largo = nombre_meses[month-1]
#         resultado = f"{day} de {mes_largo} de {year}"
#
#     else:
#         resultado = "La fecha introducida es incorrecta."
#
#     return resultado
#
#
# dia     = int(input("Introduzca un día: "))
# mes     = int(input("Introduzca un mes válido: "))
# anyo    = int(input("Introduzca un mes válido: "))
#
# while dia >= 0:
#     print(transformar_fecha(dia, mes, anyo))
#
#     dia     = int(input("Introduzca un día: "))
#     mes     = int(input("Introduzca un mes válido: "))
#     anyo    = int(input("Introduzca un mes válido: "))
    
    

    
    
#Ejercicio 4
# lista=[]
# numero=0
#
# def obtenerMayor(lista):
#     mayor=lista[0]
#     for i in range(len(lista)):
#         if lista[i]>mayor:
#             mayor=lista[i]
#     return mayor
#
# def obtenerPares(lista):
#     listaPar=[]
#     for i in range(len(lista)):
#         if lista[i]%2==0:
#             listaPar+=[lista[i]]
#     return listaPar
#
# while numero>=0:
#     numero=int(input("Introduce un numero"))
#     lista+=[numero]
# print(lista)  
# print(f"El mayor de la lista es {obtenerMayor(lista)}.")
# print(f"Los pares de la lista es {obtenerPares(lista)}.")

#Ejercicio 5
# lista=['di','buen','dia','a','papa']
# def obtenerReverse(lista):
#     invertida=[]
#     for i in range(1,len(lista)+1,1):
#         invertida.append(lista[-i])
#     return invertida
#
# print(obtenerReverse(lista))         
        
#Ejercicio 6
# lista=[1,2,4,3]
# def estaOrdenada(lista):
#     ordenada=True
#     for i in range(1,len(lista)):
#         if lista[i]<lista[i-1]:
#             ordenada=False
#     return ordenada
#
#
# print(estaOrdenada(lista))

#Ejercicio 7
# ficha_1="[1,3]"
# ficha_2="[0,3]"
#
# def es_ficha_valida(ficha):
#     resultado=False
#     if len(ficha)== 5 and ficha[1] in "0123456" and ficha[3] in "0123456":
#         resultado=True
#     return resultado
# def encajan(ficha_1,ficha_2):
#     resultado="No encajan"
#     if (es_ficha_valida(ficha_1) and es_ficha_valida(ficha_2))and ficha_1[1]==ficha_2[1] or ficha_1[1]==ficha_2==[3] or ficha_1[3]==ficha_2[1] or ficha_1[3]==ficha_2[3]:
#         resultado="Encajan"
#     return resultado
# print(encajan(ficha_1,ficha_2))

#Ejercicio 8
# lista=[]
# n=0
# def obtenerPrimos(lista):
#     listaPrimo=[]
#     for i in lista:
#         contador=0
#         for i in range(2,n):
#             if n%i==0:
#                 contador+=1
#         if contador ==0:
#             if n>0:
#                 listaPrimo.append(n)
#     return listaPrimo
#
# def obtenerSuma(lista):
#     suma=0
#     for i in lista:
#         suma+=i
#     return suma
#
# def obtenerPromedio(lista):
#     promedio=0
#     contador=0
#     suma=0
#     for i in lista:
#         suma+=i
#         contador+=1
#     promedio=suma/contador
#     return promedio
# def obtenerFactorial(lista):
#     factorial=[]
#     contador=1
#     for i in lista:
#         contador=contador+contador*i
#         factorial.append(contador)
#     return factorial
#
# while n>=0:
#     n=int(input("Introduce un numero"))
#     lista.append(n)
#
# print(f"La lista con todos los primos es {obtenerPrimos(lista)}")
# print(f"La lista con la suma es {obtenerSuma(lista)}")
# print(f"La lista con el promedio es {obtenerPromedio(lista)}")
# print(f"La lista con los factoriales es {obtenerFactorial(lista)}")

#Ejercicio 9
# lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# n=0
# n1=2
# def devolverMenor(lista):
#     listaMenor=[]
#     for i in range(len(lista)):
#         if i< n1:
#             listaMenor+=[lista[i]]
#     return listaMenor
# def devolverMayor(lista):
#     listaMayor=[]
#     for i in range(len(lista)):
#         if i> n1:
#             listaMayor+=[lista[i]]
#     return listaMayor
# def devolverMultiplo(lista):
#     listaMultiplo=[]
#     for i in range(len(lista)):
#         if i% n1==0:
#             listaMultiplo+=[lista[i]]
#     return listaMultiplo
# print(lista)
# print(f"Los menores son {devolverMenor(lista)}")
# print(f"Los mayores son {devolverMayor(lista)}")
# print(f"Los multiplos son {devolverMultiplo(lista)}")

#Ejercicio 10
# n=7
# n1=101
#
# def conversorBinarioDecimal(n1):
#     numeroDecimal=0
#     posicion=len(n1)-1
#
#     for i in n1:
#         numero=int(i)
#         numeroDecimal+=numero*2**posicion
#         posicion-=1
#     return numeroDecimal
# def conversorDecimalBinario(n):
#     numeroBinario=0
#     posicion=1
#     n=int(n)
#
#     while n!=0:
#         numeroBinario=numeroBinario+n%2*posicion
#         n//=2
#         posicion*=10
#     return numeroBinario
# print(conversorBinarioDecimal(n))
# print(conversorDecimalBinario(n))







#Ejercicio 11
# lista=[1,2,3,4,5,6,7,8,9,10]
# lista1=[2,4,6,8,10]
#
# def intersect(lista,lista1):
#     numerosComunes=[]
#     sinRepetir=[]
#     for i in lista:
#         for j in lista1:
#             if j == i:
#                 numerosComunes.append(i)
#     for j in numerosComunes:
#         if j not in sinRepetir:
#             sinRepetir.append(j)
#     return sinRepetir
# print(intersect(lista, lista1))

#Ejercicio 12
lista=[1,2,3,4,5,6,7,8,9,10,"Hola"]
lista1=[1,2,3,4,5]
def unionListas(lista,lista1):
    numeros=[]
    sinRepetir=[]
    for i in lista:
        numeros.append(i)
        for j in lista1:
            numeros.append(j)
    for j in numeros:
        if j not in sinRepetir:
            sinRepetir.append(j)
    return sinRepetir

print(unionListas(lista, lista1))


#Ejercicio 13
# lista=['Jose','Juanan','Yeray','Kike']
# letra='J'
# def obtenerNombreLetra(lista):
#     listaNombres=[]
#     for i in lista:
#         if i[0] ==letra:
#             listaNombres.append(i)
#     return listaNombres
# print(obtenerNombreLetra(lista))

#Ejercicio 14
# cad1=["Hooooooooollla","fasfsdhhasfsdf","aaa"]
# cad2=["Hooooolla","fasfsdhhasfsdf","bbbaaa"]
#
# palabra="Hoooooooooolll"
#
# def calcular_letras_distintas(palabra):
#     letras_distintas=""
#     for letra in palabra:
#         if letra not in letras_distintas:
#             letras_distintas+=letra
#     return len(letras_distintas)
#
#
# def obtener_cadena_mayor(cad1,cad2):
#     mayor=""
#     if len(cad1)>len(cad2):
#         mayor=cad1
#     elif len(cad1)<len(cad2):
#         mayor=cad2
#     else:
#         distintas_1=calcular_letras_distintas(cad1)
#         distintas_2=calcular_letras_distintas(cad2)
#         if distintas_1<distintas_2:
#             mayor=distintas_1
#         else:
#             mayor=distintas_2
#     return mayor
#
# print(obtener_cadena_mayor(cad1, cad2))




