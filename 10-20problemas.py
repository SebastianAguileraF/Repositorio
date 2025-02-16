#10


#11
palabra=input("Ingrese la palabra ").lower().replace(" ", "")
if palabra==palabra[::-1]:
    print("La palabra es un palindromo")
else: 
    print("La palabra no es un palindromo")


#12
def numero_menor(a, b, c):
    return min(a, b, c)

n1=float(input("Ingresa el primer número: "))
n2=float(input("Ingresa el segundo número: "))
n3=float(input("Ingresa el tercer número: "))

print("El numero menor es:", numero_menor(n1, n2, n3))


#13 
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_a_kelvin(c):
    return c + 273.0

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_a_kelvin(f):
    return (f - 32) * 5/9 + 273.0

def kelvin_a_celsius(k):
    return k - 273.0

def kelvin_a_fahrenheit(k):
    return (k - 273.0) * 9/5 + 32

print("1. Celsius a Fahrenheit y Kelvin")
print("2. Fahrenheit a Celsius y Kelvin")
print("3. Kelvin a Celsius y Fahrenheit")

opcion=int(input("Selecciona una opcion: "))

if opcion==1:
    c = float(input("Ingresa la temperatura en Celsius: "))
    print(f"{c} °C = {celsius_a_fahrenheit(c)} °F")
    print(f"{c} °C = {celsius_a_kelvin(c)} K")

elif opcion==2:
    f = float(input("Ingresa la temperatura en Fahrenheit: "))
    print(f"{f} °F = {fahrenheit_a_celsius(f)} °C")
    print(f"{f} °F = {fahrenheit_a_kelvin(f)} K")

elif opcion==3:
    k = float(input("Ingresa la temperatura en Kelvin: "))
    print(f"{k} K = {kelvin_a_celsius(k)} °C")
    print(f"{k} K = {kelvin_a_fahrenheit(k)} °F")

else:
    print("Opción no válida.")


#14


#15
año=int(input("Ingrese la duracion del año en dias (365 o 366): "))

comparacion=(año-1)%364
if comparacion==0: 
    print("El año no es bisiesto")
else:
    print("El año es bisiesto")


#16
def contar_vocales_consonantes(cadena):
    cadena = cadena.lower()
    vocales = "aeiouáéíóú"
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    
    num_vocales = 0
    num_consonantes = 0

    for i in cadena:
        if i in vocales:
            num_vocales = num_vocales+1
        elif i in consonantes:
            num_consonantes = num_consonantes+1
    return num_vocales, num_consonantes

cadena_usuario = str(input("Ingrese una cadena: "))

vocales, consonantes = contar_vocales_consonantes(cadena_usuario)
print("Numero de vocales:", vocales)
print("Numero de consonantes:", consonantes)


#17


#18
import cmath

def soluciones_cuadraticas(a, b, c):
    discriminante = b**2-4*a*c
    x1 = (-b+cmath.sqrt(discriminante))/(2 * a)
    x2 = (-b-cmath.sqrt(discriminante))/(2 * a)
    return x1, x2

print("La estructura de una funcion cuadraticas es la siguiente: ax^2 + bx +c")
a=float(input("Ingrese la constante a: "))
b=float(input("Ingrese la constante c: "))
c=float(input("Ingrese la constante c: "))

x1, x2=soluciones_cuadraticas(a, b, c)

print("Las soluciones son: ", x1, x2)

