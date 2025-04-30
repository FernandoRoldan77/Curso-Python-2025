# print("Hola mundo") # El numeral es un comentario!! Pueden tener la longitud que queramos.

## Toda linea que empiece con un #, será considerada por Python como un comentario. 
## Si ven comentarios con dos numerales o mas (##) es para asegurarse que si descomentamos el código, se descomente esa línea
## También existe el comentario multilínea, que python lo reconoce con 3 comillas simples 
            # para inicio, y 3 para fin => (''' ''')


## ¡TIPOS DE DATOS!
# numericos => 
# int (integer: enteros), 
# float (flotantes, valores numéricos decimales, ¡separados por PUNTO!.)

# print(5) # entero => int 
# print(5.0) ## flotante => float, Si bien nosotros no leemos el decimal en 0, python lo reconoce.

# print(p) ## => esta p, no es un tipo de dato válido, por no estár guardada con un valor en líneas anteriores.

# string => cadena de caracteres. "Hola mundo" => str
# print('hola mundo')
# print("hola mundo")
# print("5") # string! 

# bool => booleanos. (False, True)
# print(False)
# print(True)

# función type => <class int> <class bool> <class float> <class str>
# type()


# print(type(False)) # <class 'bool'>a
print(type(5.00000000000000000000)) # <class 'float'>
print(type(0.0)) # <class 'float'>
print(type(99999999999999999999)) # <class 'int'>

## ¡Variable! 
## = (simbolo de asignación)
variable1 = 3
print(variable1)
print(type(variable1))

## buenas practicas de las variables: 
# 1. Tienen que ser representativas
## Si mi variable guarda un nombre... 
# 2. Tienen que empezar con una letra. 
# 3. No pueden empezar con un número
# 4. Si tiene mas de una palabra, snake_case (un guion bajo entre cada palabra); camelCase
# 5. Python es sensible a mayusculas y minúsculas, por lo que estas variables NO SON IGUALES: 
#                           Alumno y alumno; usuario y Usuario; usuario y usuariO

nombreALumno = "Leo"
apellidoAlumno = " Messi"

print(nombreALumno + apellidoAlumno)

####################### RECORDATORIO IMPORTANTE #######################
### comentar código rápido! ctrl + }
# Python va de arriba hacia abajo. Es secuencial, línea a línea va leyendo, guardando y ejecutando.
# CASO DE EJEMPLO
# Si tengo una variable llamada nombre declarada en la linea 5,
# y vuelvo a declarar una variable con el mismo nombre en la linea 7
# Al imprimir en una linea posterior, python guardará el ÚLTIMO valor que haya guardado.

# nombre_jugador = "Tomas"

# nombre_jugador = "Angel"

# print(nombre_jugador) # la salida será Angel.

## Si las variables a declarar están debajo del print(), entonces python no las reconoce.

# print(nombre_jugador) # la salida seguirá siendo Angel.
# nombre_jugador = "Tomas"

#######################################################################