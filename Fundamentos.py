def nuevoTema(tema):
    print("\n=====", tema, "=====\n")

#para que el interprete sepa que es una funcion usamos def
#para que el interprete sepa cuanto dura la funcion TABULAMOS

nuevoTema("Enteros")
w = 105
x = 210829403
y = -256
z = 0b00110011
h = 0xffa

print(w, type (w))
print(x, type (x))
print(y, type (y))
print(z, type (z))
print(h, type (h))


nuevoTema("Conjuntos")
t ={50, 20, 30, 40, 10, 50}
print ("Conjunto t=", t, type(t))


nuevoTema("Diccionario")
d = {1:"Valor1", "Valor2":2j}
print(d, type(d))
print("d[Valor2]:", d["Valor2"])


nuevoTema("Cadenas")
cadena1 = "Cadeba con comillas dobles"
cadena2 = "Cadena con comillas simples"
print(cadena1, type(cadena1))
print(cadena2, type(cadena2))
cadenaMultilinea = '''esta es una
cadena de varias lineas
con tabulares y saltos
de
linea'''
print(cadenaMultilinea)
print("Segmentacion de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1 = "Hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena5 = cadena4.capitalize()
print(cadena5)

nuevoTema("Flotantes")
x = 1297.50
print(x, type(x))

print("Hola")


#para indicar que es complejo debe ser primero el numero y luego la j
nuevoTema("Complejos")
x = -46j
y = 12 + 45j
z = 2j
print(x, type (x))
print(y, type (y))
print(z, type (z))


nuevoTema("Variables")
variable1 = 10
_variable2 = 6.2456
Variable3 = "Juancho"
dosPalabras = "Hola"
dos_palabras = "Hello" #estilo convencional de python
print(variable1, Variable3, _variable2, dos_palabras, dosPalabras)


nuevoTema("Booleans")
lis = [8]
print(lis, "es" , bool(lis))
t = ()
print(t,"es"  , bool(t))


nuevoTema("Listas")
a = [10, 20.5, "Python list"]
print(a)
print(a[1])
a[0] = "hola"
print (a)


nuevoTema("Tuplas")
t = (25, "Tupla", 1 + 10j, 3.1416)
print(t)
print(t[2])
print("t[0:2]: ", t[0:2])
#t[1] =34  OPERACION NO VALIDA EN TUPLAS, NO SE PUEDE SOBREESCRIBIR

print("==== Operadores aritmeticos ====")
print("Operador division entera (10//3): ",  10//3)
print("Operador potencia (5 ** 3): ", 5**3)

print("==== Operadores logicos ====")
print ("Operador and (True and False): ", True and False) 

#este es un comentario de una linea

"""este es un 
comentario 
de varias
lineas :)
"""

#Actividad: Imprimir la tabla de verdad de los operadores logicos
print("==== Actividad 1 ====")
print("==== and ====")
print ("Operador and (True and False): ", True and False) 
print ("Operador and (True and True): ", True and True) 
print ("Operador and (False and False): ", False and False) 
print ("Operador and (False and True): ", False and True) 

print("==== or====")
print ("Operador or (True or False): ", True or False) 
print ("Operador or (True or True): ", True or True) 
print ("Operador or (False or False): ", False or False) 
print ("Operador or (False or True): ", False or True) 

print("==== not ====")
print ("Operador not (Not True): ", not True)
print ("Operador not (Not False): ", not False)

print("==== Operadores de comparacion ====")
print(" 2 == 3" , 2==3)
print(" 2 != 3" , 2!=3)
print(" 2 < 3", 2<3 )
print(" 2 > 3", 2>3 )
print(" 2 <= 3", 2<=3 )
print(" 2 >= 3", 2>=3 )


