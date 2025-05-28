'''
REPASO
WHILE , BREAK Y CONTINUE
bucle while: repito un bloque de código infinitas veces o hasta que se cumpla una condición.
 '''
# while condicion:
#     print("esto está dentro del bucle")
#     #
#     #
#     #
# print("Fuera del bucle! ")

# contador = 0 # inicio mi variable en 0
# # condicion = contador<10 # True o False
# while (contador<10 and contador<5):
#     print(f"Entraste al bucle! {contador}") # f-string

#     contador += 1

# print("Esto si es False")

'''
Repaso de F-string: formateador de cadena. 
Sintaxis => f'cadena de texto {variable}'
'''
# cadena de texto!
# nombre = "Lionel"
# mensaje = "bienvenido " + nombre + ",como estas?" # bienvenidoLionel
# mensaje = f"bienvenido {nombre}, como estas? " 

# contador = 0 # inicio mi variable en 0
# # condicion = contador<10 # True o False
# while (contador<10):
#     print(f"Entraste al bucle! {contador}") # f-string
#     contador +=1
#     if contador == 4:
#         break

# print("Fuera del bucle! ")

# contador = 0 # inicio mi variable en 0
# # condicion = contador<10 # True o False
# while (contador<10):
#     contador +=1
#     if contador == 4:
#         continue
#     else:
#         print(f"Entraste al bucle! {contador}")

# print("Fuera del bucle! ")

# mail>12 caracteres; 1 solo @ ; gmail.com o yahoo.com . hotmail.com
# while True:
#     mail = True
#     if mail:
#         print("Envio correo")
#     else:
#         continue


'''
################################## LISTAS! ##################################
Otro tipo de dato ordenado. 

sintaxis = [valor1, valor2, valor3] Valores de cualquier tipo, separados por coma y 
entre corchetez

Tipos de datos que vimos, ordenados (⭐): 
int   => (0-9)
float => (0-9-.) valores numéricos con un punto . para dividirlo de la parte decimal, aunque sea 0
bool  => True o False
str   => caracteres alfanuméricos entre "" o '' ⭐
list  => [valor1, valor2, valor3] Valores de cualquier tipo ⭐
'''
# 0.0000000000983 # float
# 987231239.0 # Float => tiene que tener parte decimal.
# 8.0 => ocho de tipo float.
# 8 => ocho de tipo int.

# lista_jugadores = [] # => tipo de dato list (lista vacía)
# print(lista_jugadores)
# print(type(lista_jugadores))

# Puede tomar múltiples valores y de diferente tipo de dato separados por coma
# lista_jugadores = [9,9.0,False,"Lionel", [True, True]] # => list

# lista_jugadores = [9 ,9.0,False,"Lionel", [True, True]]
# # lista_jugadores=[0 ,1  ,2    ,3       , 4]
# mensaje = "Esto es un mensaje! "
# print(mensaje[0])
# print(lista_jugadores[1]) # 9.0

# print(int(lista_jugadores[1])) # 9

# print(lista_jugadores)

# contador = 0
# lista_jugadores = ["EL dibu ", "motiel", "Lionel", "  RODRIGRO", "Lisandro"]
# # lista_jugadores = [0       ,   1   ,    2   ,        3  ]
# print(len(lista_jugadores)) # 4

# while contador < len(lista_jugadores):
#     print(lista_jugadores[contador])
#     # lista_jugadores[contador]  == cadena de caracteres con un valor.

#     contador+=1


# mensaje = "HOLA"
# print(mensaje[9]) # IndexError: string index out of range


# lista_jugadores = ["EL dibu ", "motiel", "Lionel", "  RODRIGRO", "Lisandro"]
# print(lista_jugadores[0])
# print(type(lista_jugadores[0]))
# print(lista_jugadores[0]) # Como accedo a un elemento de tipo string de la lista, puedo aplicarle 
# los distintos métodos de cadena que vimos. 


# ¿como hago para acceder al último elemento?
# lista_jugadores = ["EL dibu ", "motiel", "Lionel", "  RODRIGRO", "Lisandro"]
# print(lista_jugadores[-1])
# print(lista_jugadores[len(lista_jugadores)-1])

################################# Range()!
# range(fin)
# range(inicio, fin)
# range(inicio, fin ,step) ## step o salto

# listaNumeros = [0,1,2,3,4,5,6,7,8,9]
# print(range(10)) # range(0, 10) => secuencia de números de 1 en 1 hasta 10 -1
# print(list(range(10)))
# print(range(4,10))
# print(list(range(4,10+1)))
# print(range(4,19,3))
# print(list(range(4,19,3)))

## ERRROR
# listaNumeros = range([0,1,2,3,4,5,6,7,8,9]) # TypeError: 'list' object cannot be interpreted as an integer
# print(listaNumeros)


## BUCLE FOR 
## bucle for => sabemos exactamente cuantas veces vamos a recorrer! 

## SINTAXIS 
# ObjetoOrdenado = "Hola"
# ObjetoOrdenado = ["Hola", "FIN","VOLVI"]

# for variableIntera in ObjetoOrdenado:
#     '''
#     Por cada variable del objeto ordenado...
#     '''
#     print(variableIntera)

# ObjetoOrdenado = ["Hola", "FIN","VOLVI"]
# print(ObjetoOrdenado[0])
# print(ObjetoOrdenado[1])
# print(ObjetoOrdenado[2])



# ObjetoOrdenado = ["Hola", "FIN","VOLVI"]

# for variableIntera in ObjetoOrdenado:
#     '''
#     Por cada variable del objeto ordenado...
#     '''
#     print(variableIntera.lower().strip())

# split() => me devuelve una lista
# mensaje = "Hola como estas?"
# mensaje = mensaje.split()
# print(mensaje)

# mensaje = "Hola como estas mi nombre es Lionel Messi, te invito a jugar"
# mensaje = "Hola como estas mi nombre es Lionel Messi, te invito a jugar".replace(",","")

# for variable in mensaje.split():
#     if variable.lower() == "messi":
#         print("Grande!!! ")

# listaDepalabras = ["Hola", "FIN","VOLVI"]
# for palabra in listaDepalabras:
#     print(palabra)

# for numero in range(8+1):
#     print(numero)

## Esta lista podría ser información de una columna de algún excel o base de datos llamada nombres
# listaNombres = ["Lionel ","rodrio","Lionel","Pablo"]

# nombreABuscar = "lionel"
# contador = 0
# for nombre in listaNombres:
#     if nombre.lower().strip() == nombreABuscar:
#         contador += 1

# print(contador)

## Estos tipos de dato list, vienen de diferentes fuentes. En este caso, podría ser
# la fila de una archivo excel, donde las columnas tengan estos nombres: nombre,edad,altura,¿comio dulce de leche?
# listaInfo = ["Lautaro", 20,1.7,False]


