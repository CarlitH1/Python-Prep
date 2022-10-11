# 1.- Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
#from math import pi
from cmath import pi
from os import truncate
from stringprep import c22_specials

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
# 9.- Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(Var1))
print(type(Var2))
# 10.- Asignar a una variable, la suma de un número entero y otro decimal
Suma    =   10  +   10.5
# 11.- Realizar una operación de suma de números complejos
COM1  = 3   +   6j
COM2  = 7   +   8J
sComplejo   =   COM1    +   COM2
print(sComplejo)
# 12.- Realizar una operación de suma de un número real y otro complejo
REAL1  = 3.2
COM3  = 7   +   8J
sComplejo1   =   REAL1    +   COM3
print(sComplejo1)
# 13.- Realizar una operación de multiplicación
factor1 = 2.0  
factor2 = 3.3
multiplicacion  = factor1*factor2
print(multiplicacion)
# 14.- Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
# 15.- Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
resultado1=27/4
print(resultado1)
# 16.- De la división anterior solamente mostrar la parte entera
resultado2=27//4
print(resultado2)
# 17.- De la división de 27 entre 4 mostrar solamente el resto
resultado3=27%4
print(resultado3)
# 18.- Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
resultado4=4*resultado2+resultado3
print(resultado4)
# 19.- Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
suma_string = "a" + 'b' + '''c'''
print(suma_string)
# 20.- Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
dos_a= '2'
dos_b= 2
print(type(dos_a))
print(type(dos_b))
print(dos_a==dos_b)
# 21.- Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int(dos_a)==dos_b)
print(dos_a==str(dos_b))
# 22.- ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a=float('3.8')
print(a)
# 23.- Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
b=30
b-=100
print(b)
# 24.- Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<12)
# 25.- Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
print(str(2)+'2')
print(2+int('2'))
print(type(str(2)+'2'))
print(type(2+int('2')))
# 26.- Realizar una operación válida entre valores de tipo entero y string
print('carro '+str(12))