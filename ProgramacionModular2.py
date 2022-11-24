'''
Created on Nov 22, 2022

@author: estudiante
'''
#Ejercicio 1
num=5
def saberFactorial(num):
    factorial=1
    if num==0:
        factorial=1
    elif num<0:
        factorial=None
    while num>1:
        factorial*=num
        num-=1
    return factorial

print(saberFactorial(num))

#Ejercicio 2
num=2024
def saberAñoBisiesto(num):
    bisiesto=None
    if (num%4==0) and (num%100!=0 or num%400==0):
        bisiesto=True
    else:
        bisiesto=False
    return bisiesto
print(saberAñoBisiesto(num))

#Ejercicio 3

def saberDiasMes(mes,año):
    mesesDia=[31,28,31,30,31,30,31,31,30,31,30,31]
    dia=0
    try:
        if mes<1 or año<1:
            dia=-1
        else:
            if saberAñoBisiesto(año)and mes==2:
                dia=29
            else:
                dia=mesesDia[mes-1]
    except:
        dia=-1
    return dia
   
print(saberDiasMes(2, 2020))    

#Ejercicio 4
def saberdiaSemana(dia,mes,año):
    diaMes=[31,28,31,30,31,30,31,31,30,31,30,31]
    diaSemana={7:"Domingo",1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado"}
    try:
        if mes<1 or año<1:
            print("Introduzca valores validos")
        else:
            a = (14 - mes)/12
            y = año - a
            m = mes + 12 * a - 2
            d= int(((dia + y + y//4 - y//100 + y//400 + (31*m)//12)%7))
            d=diaSemana[d]
    except:
        print("Valores invalidos")
    return d
print(saberdiaSemana(21,11,2022))   

#Ejercicio 5

def multiplicacion(n,m):
    prod=0
    for i in range(m):
        prod=prod+n
    return prod
def elevadoconsuma(base,exp=0):
    total=1
    for i in range(exp):
        total=multiplicacion(base,total)
    return total

def powerIt(base,exponent=0):
    total=1
    for i in range(exponent):
        total=base*total
    
    return total

print(powerIt(2, 2))

#Ejercicio 6
def conseguirNumeroDigito(number):
    digitos=None
    txt=str(number).upper()
    contador=0
    try:
        if "." in txt:
            digitos=len(txt)-1
        elif "." in txt and "-" in txt:
            digitos=(len(txt))-2
        else:
            digitos=len(txt)
        for char in txt:
            if char in "GHIJKLMNOPQRSTUVWXYZ":
                digitos=None
            elif char ==".":
                contador+=1
                if contador>1:
                    digitos=None
        if digitos==0:
            digitos=None
    except ValueError:
        digitos=None


    return digitos


print(conseguirNumeroDigito("a"))


#Ejercicio 7

def esPrimo(number):
    if number>0:
        try:
            prime=True
            for i in range(2,number):
                if number%i==0:
                    prime=False
        except:
            prime=None
    else:
        prime="Introduce un numero mayor a 0"
    return prime
    
print(esPrimo(2))

#Ejercicio 8

def solveSecondOrderEquation(a,b,c):
    try:
        x1=(-b+(((b**2)-4*a*c)**0.5))/2*a
        x2=(-b-(((b**2)-4*a*c)**0.5))/2*a
        solucion=x1,x2
    except:
        solucion=None

    return solucion


print(solveSecondOrderEquation(True,"2",6))


#Ejercicio 9

def conseguirPrimoDivisores(a):
    primes=[]
    for i in range(1,a):
        if a%i==0 and esPrimo(i):
            primes.append(i)

    return primes

print(conseguirPrimoDivisores(77777))

#Ejercicio 10

def isFriendNumber(a,b):
    divisors=[]

    for i in range(1,a-1):
        if a%i==0:
            divisors.append(i)
    if sum(divisors)==b:
        isFriend=True
    else:
        isFriend=False
    return isFriend
    
print(isFriendNumber(425,200))



    
