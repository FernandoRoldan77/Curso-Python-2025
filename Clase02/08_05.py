### Clase 2 => Contenidos: Clase 3/4

## Repasoo
nombre_usuario = True

## Operadores aritméticos =>> Operaciones matemáticas
# + - * (multiplicación) ** (potencia) 
# / (división) // (división entera) % (resto) numeroCualquier%2 => 0 (part) 1(impar)

primer_numero = 90
segundo_numero = 5

## suma
resultado = primer_numero + segundo_numero + segundo_numero + segundo_numero
## resta 
resultado = primer_numero - segundo_numero - segundo_numero - segundo_numero
# resultadoSumaPersonal = primer_numero - segundo_numero - segundo_numero - segundo_numero # formato camelCase

# resultado = "hola "+ "chau" ## si piso la variable puedo cambiar el tipo de dato también! 

resultado = primer_numero * segundo_numero 
resultado = primer_numero * segundo_numero * (segundo_numero * segundo_numero)

nombre_usuario = "Lionel "
resultado = nombre_usuario * segundo_numero

# / => Division
resultado = primer_numero / segundo_numero # Siempre me va a dar un valor de tipo float

# // => Division entera
resultado = primer_numero // segundo_numero # Siempre me va a dar un valor de tipo int
resultado = primer_numero / 7 # 12.857142857142858
resultado = primer_numero // 7 # trunco el número.

resultado = 7 // 3 # trunco el número.

## % resto 

resultado = 13%2 ## => si es par: el resto es 0 ; si es impar: el resto es 1.

resultado = 13%5 

## potencia => **

resultado = segundo_numero ** 2  #(5 al cuadrado)
resultado = 5.5 ** 2  #(5 al cuadrado) => Devuelve un float

##### Operadores relacionales => siempre nos devuelve un booleano 🚨🚨🚨🚨
## False o True
## > => (mayor estricto que)
numero_1 = 30.0
numero_2 = 100.987

## no se suele usar, pero está bueno saberlo.
numero_1 = "holaasdasd" # => el valor ASCI de cada caracter.
numero_2 = "chau"

## < => (menor estricto que)
numero_1 = 30
numero_2 = 10
# print(numero_1<(numero_2*5))

## >= => (mayor o igual que)
numero_1 = 30
numero_2 = 30
# print(numero_1>=numero_2)


## <= => (menor o igual que)
numero_1 = 270
numero_2 = 30
# print(numero_1<=numero_2)

## Ejemplo de error: mayor o menor de edad?

edad = 18
# edad = 19
# print("El usuario puede ingresar? ", edad>18)
# print("El usuario puede ingresar? ", edad>=18)


## == => (igual que)

numero_1 = 30
numero_2 = 30.06
# print(numero_1==numero_2)

numero_1 = "hola "
numero_2 = "Hola "
# print(numero_1==numero_2)

## != => (distinto que)  => Es true cuando los valores son distintos
numero_1 = 50
numero_2 = 50.000000001 
# print(numero_1!=numero_2)

## Operadores lógicos
## and => True and True : True
## or => False or True : True
## not => Negar el booleano. : Ej: True lo pasa a False

# if not registro == True: 👀👀👀👀👀👀👀



## condicionales
## Sintaxis => 
# if condicion: => condicion tiene que ser True
#     codigo a ejecutar

numero1 = 50
numero2 = 30

# if numero1>(numero2*2): # la condición me devuelve False. 
#     print("el número2 es mayor")

if numero1>numero2: # la condición me devuelve False. 
    print("el número1 es mayor")

# El código siguee e imprimo esto! 
print("hola che como andas?")

# if (numero1*2)>numero2: # la condición me devuelve True. 
#     print("el número1 es mayor")

# nombre = input("ingresá tu nombre")
# if nombre == "Lau": # la condición me devuelve True. 
#     print("usuario válido")

######### IF ELSE
# if (condicion):
#     codigo a ejecutar
# else:
#     Ejecuto este otro código

# nombre = input("ingresá tu nombre: ")
# if nombre == "Lau": # la condición me devuelve True. 
#     print("usuario válido")
# else:
#     print("Ingresá un nombre de usuario válido")


# edad = int(input("ingresá tu edad: "))
# if edad >= 18: 
#     print("El usuario puede ingresar")
# else:
#     print("El usuario no puede ingresar")


######### IF ELIF ELSE 
# if condicion:
#     codigo a ejecutar
# elif condicion2:  ### Los elif pueden ser 1 o mas de 1
#     codigo a ejecutar
# elif condicion3:
#     codigo a ejecutar
# elif condicion4:
#     codigo a ejecutar
# else:
#     Codigo a ejecutar

### Evaluando rango de edad
# edad = int(input("ingresá tu edad: "))

if edad < 12:
    print("entra gratis: ")
elif edad >= 12 and edad < 18: 
    print("Descuento 25% ")
elif edad >= 18 and edad < 70:
    print("Descuento 15% ")
elif edad >= 70:
    print("Entra gratis")
else:
    print("Error del beneficio.")


##################### 


# edad = int(input("ingresá tu edad: "))
jubilada = False # check que devuelve true si marco y false si no marcó que está jubilado/a
cud = True # certificado único de discapacidad

### EJEMPLO CON edad = 13
if edad < 12: # false
    print("entra gratis: ")
elif edad >= 12 and edad < 18 or cud: ## (True or True) => true
    print("Descuento 25% ") ## Ejecutamos este código
elif edad >= 18 and edad < 70 and jubilada: ## (False and False) => true
    print("Descuento 15% ")
elif edad >= 70:
    print("Entra gratis")
else:
    print("Error del beneficio.")


numero = int(input("ingresa un número par: "))
if numero%2==0:
    print("Número es par")
else:
    print("Número es impar")


### MATCH


## métodos de cadena

