### REPASO

'''Operadores matemáticos => +, -, *, /, //, %, **
Operadores lógicos     =>, > , >= , < , <= , == , !=
edad = int(input("ingresá tu edad: "))
edadCorrecta = edad > 17'''

'''Operadores lógicos => And or not'''

'''Condicional!'''

# if edadCorrecta and True:
#     print("Hola!")
# elif edad < 15:
#     print("Tenés menos de 15")
# else:
#     print("las condiciones son falsas.")

# nombre = input("ingrese tu nombre: ")
# if nombre == "":
#     print("Nombre correcto")
##
'''
FUNCION LEN => Nos devuelve la cantidad de elementos que tiene un tipo de dato ordenado.
'''

# print(len("Lio"))
# print(len(" "))

# print(len("las "))
# print(len("sal"))

# contrasenia = input("Ingrese su contraseña: min 8 caracteres: ")

# if len(contrasenia)<8:
#     print("Mínimo 8 caracteres. ")

# mensaje = "las arañas comen mosquitos"
# print(mensaje)
# # print(mensaje[5]) ## Accedo al caracter en la posicion 5
# # print(mensaje[8]) ## Accedo al caracter en la posicion 8
# print(mensaje[1]) ## Accedo al caracter en la posicion 8

# ### Los elementos ordenados en python SIEMPRE arrancan en cero.
# print(mensaje[0]) ## Accedo al caracter en la posicion 0 => l
# print(mensaje[1]) ## Accedo al caracter en la posicion 0 => a
# print(mensaje[2]) ## Accedo al caracter en la posicion 0 => s
# print(mensaje[3]) ## Accedo al caracter en la posicion 0 => "el espacio"

# print(len("las")) # 3 espacios ocupados por caracteres.

'''MÉTODOS DE CADENA =>  String ordenados!'''

'''title'''
# mensaje = "las arañas comen mosquitos"
# print(mensaje)
# método title()
# print(mensaje.title())

# mensaje = "las arañas comen mosquitos".title() # Las Arañas Comen Mosquitos
# mensaje = input("Ingresá tu nombre completo: ").title() # Las Arañas Comen Mosquitos
# print(mensaje)

'''lower() => pasa todo a minuscula!'''
# mensaje = "LAS Arañas Comen MosquiTOS".lower() #
# print(mensaje)
# mensaje = input("Ingresá tu nombre completo: ").lower()
# print(mensaje)

'''upper() => Pasa todo a mayúscula'''
# mensaje = "LAS Arañas Comen MosquiTOS".upper() #
# print(mensaje)
# mensaje = input("Ingresá tu nombre completo: ").upper()
# print(mensaje)

# nombre = input("Ingresá tu nombre completo: ").lower()
# nombreMayus = nombre.upper()
# mensaje = nombreMayus.title()

'''Formateo del nombre. ej : de lionel Messi a Lionel Messi'''
# nombre = input("Ingresá tu nombre completo: ").lower().upper().title()

'''replace(a,b) => reemplaza a por b'''

# mail = input("ingrese su mail: ").replace("gmail.com","yahoo.com")
# print(mail)
# mensaje = "Hay una araña en mi escritorio"
# print(mensaje)
# print(mensaje.replace("araña","ARAÑA"))

'''¿POr que hacer esto suelto no funciona?
    
    mensaje.replace("araña","ARAÑA")

    Cuando almacenamos una cedena en una variable,
    necesitamos modificar el valor de la variable para que se apliquen
    los métodos que elegimos. Por eso al llamar a la variable y aplicarle un método cualquier,a en este caso el replace
    no estamos modificando la variable, solamente la estamoss trabajando con la particularidad del método que elijamos.

    Para almacenar los cambios es necesario almacenar el cambio en una varaible. Puede incluso ser la misma variable. 
    
    mensaje = mensaje.replace("araña","ARAÑA")

    Ahora esta variable mensaje tiene el mismo nombre, pero su valor es distinto y podemos usarlo! 

'''


# mail = input("Ingresa tu mail: ")
# cantCaracteres = len(mail)
# remplazo = len(mail.replace("@",""))
# if (cantCaracteres-remplazo) == 1:
#     print("el usuario tiene un solo @")
# else:
#     print("te faltan o sobran! ")

'''strip() => elimina los espacios al principio y al final'''

'''
¿Donde se aplica strip?
Siempre que queramos eliminar espacios de una cadena. Hay un ejemplo mas abajo sobre el input del nombre de un usuario.
También es común en las contraseñas y textos largos que se formatean con algun programa en particular para transformarlo en HTML por ejemplo.
'''
# nombre = input("ingresá tu nombre: ")
# print(nombre)
# print(len(nombre))
# print(len(nombre.strip()))

#### Split () => NO LO VIMOS PERO LO PUEDEN INVESTIGAR! 

'''
BUCLE WHILE => mientras.

...mientras la condición sea True, entonces ejecuto las líneas de código que estén
debajo y a mas de 4 espacios, como mínimo, de la linea de fondo.

'''
# condicion = True

# while condicion:
#     ## Strip elimina los espacios al principio y al final.
#     ## Lower => convierte todo a minusculas.
#     nombre = input("Ingrese su nombre: ").strip().lower()
#     if nombre == "angel":
#         condicion = False


## ERRRO 1
'''
El error viene de que estoy comparando "angel " con un espacio, pero con el strip, le estoy elimnando justamente los espacios antes y después! 
'''
# condicion = True

# while condicion:
#     ## Strip elimina los espacios al principio y al final.
#     nombre = input("Ingrese su nombre: ").strip()
#     if nombre == "angel ":
#         condicion = False

# ERROR 2
'''
Este error genera un bucle infinito, porque el condicional me queda por fuera del bucle, haciendo 
que el bucle se ejecute infinitamente, y no llegue nunca al condicional de abajo, que está
por fuera del bucle => se ejecutará una vez terminado el bucle.
'''
# condicion = True
# while condicion:
#     ## Strip elimina los espacios al principio y al final.
#     nombre = input("Ingrese su nombre: ").strip()

# if nombre == "angel":
#     condicion = False

'''Contador y acumuladores'''

# contador = 0
# while contador < 3:
#     nombre = input("Ingresá tu nombre: ").strip().lower()
#     if nombre == "angel":
#         print("entraste!")
#     print(contador)
#     contador = contador + 1
#     # contador += 1 # Es lo mismo que arriba!

# contador = 0
# while contador < 3:
#     nombre = input("Ingresá tu nombre: ").strip().lower()
#     if nombre == "angel":
#         print("entraste!")
#         break
#     print(contador)
#     contador = contador + 1

# print("cortaste el bucle")


# acumulador = 0
# while acumulador <= 3:
#     nombre = input("Ingresá tu nombre: ").strip().lower()
#     if nombre == "angel":
#         print("entraste!")
#         acumulador += 1
#     print(acumulador)

# print("cortaste el bucle")

# condicion = True
# if condicion:
#     print(" Hola esto esto NO será infinito")

'''# Bucle infinitoo
# while condicion:
#     print(" Hola esto esto será infinito")
'''

# condicion1 = False
# condicion2 = False

# while condicion1 and condicion2:
#     print("paso esto:! ")


contador = 0
while True:
    nombre = input("Ingresá tu nombre: ").strip().lower()
    if nombre == "angel":
        print("entraste!")
        break
    print(contador)
    if contador == 3:
        break
    contador = contador + 1

print("cortaste el bucle")


### Próxima clase! 
# LISTAS
# BUCLE FOR
# FUNC RANGE
