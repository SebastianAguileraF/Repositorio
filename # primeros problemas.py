# primeros problemas 

# Problema 1. 
print("Hola, Mundo")

# Problema 2. 
numero1 = int(input("Indique el primer numero "))
numero2 = int(input("Indique el segundo numero "))

Elegir = 0

print("Especifique su operacion, 1) suma. 2) resta. 3) multiplicacion. 4) division")
Elegir = int(input())

if Elegir == 1:
    print(numero1+numero2)
elif Elegir == 2:
    print(numero1-numero2)
elif Elegir == 3:
    print(numero1*numero2)
elif Elegir == 4:
    print(numero1/numero2)

# Problema 3. 
numero = int(input("Introduzca el numero "))

factorial = 1

i = 1
while (i <= numero):
    factorial = factorial * i
    i = i + 1

print (factorial)

# Problema 4. 
# No tengo idea 

# Problema 5.
numero = input("Especifique su numero ")


# Problema 6. 
capital = int(input("Introduzca el capital inicial "))
interes = int(input("Introduzca la tasa de interes "))
tiempo = int(input("Introduzca el periodo de ahorro "))

interesCompuesto = capital* (1+interes)**tiempo
print(interesCompuesto)