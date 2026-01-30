# Programa para calcular el área y el perímetro de un circulo de radio R

# Librerias
import math

print("------------------------------------")
print("-----Area y perimetro del circulo----")
print("------------------------------------")

# input
r = input("Ingrese el valor del radio del círculo: ")
r = int(r)

# processing
a = math.pi*r**2
p = 2*math.pi*r

# output
print("------------------------------------")
print("-------------Resultados-------------")
print("------------------------------------")
print("El área del circulo es: " + str(a))
print("El perímetro del circulo es: " + str(p))
print("------------------------------------")






















