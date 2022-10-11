# 1.- Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
#from math import pi
from cmath import pi
from os import truncate

variable    =   2
print(variable)
# 2.- Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
# 3.- Imprimir el tipo de dato de la variable creada en el punto 1
print(type(variable))
# 4.- Crear una variable que contenga tu nombre
nombre  =   'Carlos'
# 5.- Crear una variable que contenga un número complejo
complejo    =   16   +   12j 
# 6.- Mostrar el tipo de dato de la variable crada en el punto 5
print(type(complejo))
# 7.- Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
variable_pi1 = "{:.4f}".format(pi)
variable_pi2 = round(pi,5)
print(variable_pi1)
print(variable_pi2)
# 8.- Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
Var1 = 'True'
Var2 = True
print(type(Var1))
print(type(Var2))





