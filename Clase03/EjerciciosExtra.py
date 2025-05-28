# Ejercicios bucles y métodos de cadena

# Viaje en el tiempo. Regresamos a Facebook en 2013. 
#Trabajá con una cadena de caracteres corta que ingrese el usuario y reemplazá las siguientes letras de esta manera: 

# A o a = 4
# t o T = 7
# o o O = 0
# s o S = 5

# usuario = input (f" Ingresar el usuario: ")
# usuario = usuario.replace("A","4")
# usuario = usuario.replace("a","4")
# usuario = usuario.replace("T","7")
# usuario = usuario.replace("t","7")
# usuario = usuario.replace("O","0")
# usuario = usuario.replace("o","0")
# usuario = usuario.replace("s","5")
# usuario = usuario.replace("S","5")
# print (usuario)

# Mostrar por la terminal.

#  Pedile al usuario que ingrese su contraseña que tiene que cumplir con lo siguiente: 
# Tiene que tener únicamente caracteres numéricos (Ver tabla en el cuadernillo de la clase 4).
# Tiene que tener mínimo 8 caracteres sin espacios en ningún lado

# string = input (f"Ingrese el usuario: ")
# if((len(string) == 8) and (string.isdigit) and (string.strip())):
    
#         print (f"El usuario {string} tiene una contrasenia valida")
# else:
#         print("contrasenia invalida")
    
  
# Imprimí en un bucle while, cada uno de los caracteres de "Talento-Tech"

# contador   = 0
# caracteres = "Talento-Tech"
# i = 0
# while (contador != len(caracteres)):
#         print (caracteres[i])
#         i = i +1
#         contador = contador +1 
   

# Generá un bucle que sume a la variable "resultado" el valor de 7 y que se repita hasta que el usuario ingrese algunas de estas palabra: 
#fin o Fin o FIn o fiN

resultado = 0 
palabra = input("El usuario ingresa la palabra:").strip().upper() #Para que filtra cualquier tipo de  diferencia en el string

while palabra != "fin":
    resultado = resultado +7 
    print(resultado)
    palabra =  input("El usuario ingresa la palabra: ").strip().lower()

print("finalizaste el bucle")


# Creá un programa que simule el ingreso de un usuario con nombre y contraseña.

# Las reglas son las siguientes:

# El programa debe permitir ingresar nombres tantas veces como sea necesario hasta que el usuario escriba 
#el nombre correcto "L10nel Me55i" o escriba la palabra "basta" (en minúscula).

# Si el usuario se equivoca, mostrá el mensaje: "Intentá de nuevo".

# Si escribe "basta", el programa termina sin mostrar ningún mensaje extra.

# Si escribe bien el nombre, el programa debe mostrar una ecuación sencilla (Ejemplo: Cuánto es 18 + 7?) 
#y esperar que el usuario ingrese el resultado como contraseña.

# Si responde correctamente, mostrá: "¡Bienvenido!".

# Si se equivoca en la contraseña, mostrá: "Intentá de nuevo" y volvé a pedir la contraseña hasta que acierte. 

# nombre          = input(f"Ingresar nombre: ")
# nombreCorrecto1 = "L10nel Me55i"
# nombreCorrecto2 = "basta"

# while True :
#   if (nombre == nombreCorrecto1 ): 
#     resultado    = input(f"Cuánto es 18 + 7?")
#     rtaResultado = "25"
    
#     if(resultado == rtaResultado):
#       print("¡Bienvenido!")
#       break
#     else:
#      print("ingresaste el resultado incorrecto")
     
#   elif(nombre == nombreCorrecto2): 
#     break
  
   





