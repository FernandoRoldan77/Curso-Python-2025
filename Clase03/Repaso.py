# Formulario de la clase 4
# nombre = "Ana"
# saludo = f"Hola, {nombre}!"
# print(saludo)

## MATCH
# sintaxis
# variable = "Lionel"
# match variable:
#     case "Tomas":
#         print("El nombre es tomas! ")
#     case "Jeremías":
#         print("El nombre es Jeremías")
#     case "lionel":
#         print("El nombre es lionel minuscula")
#     case "Lionel":
#         print("Ganaste!! ")
#     case _:
#         print("perdiste! ")

# edad = 30
# match edad:
#     ## Edad se evalua en cada caso del match
#     case edad if edad < 0:
#         ## Guardamos edad en una variable p y comparamos p.
#         print("edad incorrecta")
#     case edad if edad < 10:
#         ## Guardamos edad en una variable p y comparamos p.
#         print("edad menor a 10")
#     case _:
#         ## Guardamos edad en una variable p y comparamos p.
#         print("edad incorrecta 2")


# edad = 30
# match edad:
#     ## Edad se evalua en cada caso del match
#     case e if e < 0:
#         ## Guardamos edad en una variable p y comparamos p.
#         print("edad incorrecta")
#     case e if e < 10:
#         ## Guardamos edad en una variable p y comparamos p.
#         print("edad menor a 10")
#     case _:
#         ## Guardamos edad en una variable p y comparamos p.
#         print("edad incorrecta 2")

# if edad>20:
#     print("Ganaste")
# else:

# edad = int(input("Ingresá tu edad: "))

# if edad < 18:

#     print("Sos menor de edad.")

# else:

#     print("Sos mayor de edad.")



# texto = "Hola" # String => ordenados arrancan desde 0! texto[0]
#                # String => Inmutables! 
# print(texto[0])
# print(texto[1])

# # texto[0] = "J" # TypeError: 'str' object does not support item assignment
# print(texto.replace("H","J"))

# # string, int, bool, float  => inmutables
# numero = 987897
# numero[2] # TypeError: 'int' object is not subscriptable


## Operdaor ternario
# acceso = True if (p:=int(input("Ingresá tu edad"))) <= 30 else False
# print(acceso)


'''
Viaje en el tiempo. 
Regresamos a Facebook en 2013. Trabajá con una cadena de caracteres corta que ingrese el usuario y 
reemplazá las siguientes letras de esta manera: 
A o a = 4
t o T = 7
o o O = 0
s o S = 5

'''
# cadena = "EStO es un Texto cuAlquiera de 2013, saludos! "
# concatenar = "s"+5
# cadena.replace("s","5").replace("S","5")
# cadena.replace("t","5").replace("T","5")

# contrasenia = "09128a".isdigit() ## False
# contrasenia = "09128".isdigit() ## True
# if len(contrasenia)== 8:
#     print(contrasenia)

## Primera forma
# resultado = 0
# palabra =  input("El usuario ingresa la palabra: ").strip().lower()
# while palabra != "fin":
#     resultado = resultado +7 
#     print(resultado)
#     palabra =  input("El usuario ingresa la palabra: ").strip().lower()
    
# print("Fin del ciclo")

## Segunda forma
# resultado = 0
# while input("El usuario ingresa la palabra: ").strip().lower() != "fin":
#     resultado = resultado +7 
#     print(resultado)
    
# print("Fin del ciclo")

'''
Otro comentario de multilínea
'''







