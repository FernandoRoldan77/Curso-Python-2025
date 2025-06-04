## CRUD => create, read, update, y delete
'''
métodos de listas
listas = list()
'''

# nombres_personajes = ["Lionel","Rodrigo"]
'''append()'''
# nombres_personajes.append("Angelito") # ['Lionel', 'Rodrigo', 'Angelito']
# nombres_personajes.append(90) # ['Lionel', 'Rodrigo', 'Angelito', 90]
# print(nombres_personajes)

'''sort() ## Ordenar una cadena... '''
# nombres_personajes.sort()
# print(nombres_personajes) # ['Angelito', 'Lionel', 'Rodrigo']
# print(nombres_personajes.sort()) # None

'''
El sort() ordena los elementos modificando la lista original. 
    1 - No crea una representación como otros métodos vistos. 
    2 - No retorna nada (None)
    3- Solo se puede usar en las listas
'''
# nombres_personajes.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
# print(nombres_personajes) # ['Angelito', 'Lionel', 'Rodrigo',90]
# print(nombres_personajes.sort()) # None

# numeros = [9,4,6,7,101,2,4,2,7,7]
# numeros.sort()
# numeros.sort(reverse=True)
# print(numeros)

'''
El append solamente puede agregar de a un elemento a otra lista.
Si quiero agregar mas elementos, tengo que ir agregando de a uno. 
Si quiero agregar una lista, conviene usar el extend...
'''
# nombres_personajes.append("Tomas","Javier") # TypeError: list.append() takes exactly one argument (2 given)
# print(nombres_personajes)

# extras = ["Tomas","Javier"]
# nombres_personajes.extend(extras)
# print(nombres_personajes) # ['Angelito', 'Lionel', 'Rodrigo', 'Tomas', 'Javier']


'''
remove(x)
Si el x no está tira error... prestar atención! 
'''
# jugadores = ['Angelito', 'Lionel', 'Rodrigo', 'Tomas', 'Javier']
# print(jugadores)
# # jugadores.remove("Dibu") # ValueError: list.remove(x): x not in list
# jugadores.remove("Tomas")
# print(jugadores)

'''
pop(indice) => elimino por el indice...ver el error.
'''
# jugadores = ['Angelito', 'Lionel', 'Rodrigo', 'Tomas', 'Javier']
# jugadorEliminado = jugadores.pop(12) ## IndexError: pop index out of range

# print(jugadorEliminado)
# print(jugadores)

'''
count(caracter) # La cantidad de apariciones que tengo del caracter.
'''
# jugadores = ['Angelito', 'Lionel', 'Rodrigo', 'Tomas', 'Javier','Lionel']
# numero = jugadores.count("Lionel")
# print(numero)

### Uso del count pra validaciones...

# mail = "lautaro.antriolo@bue.edu.ar"
# cantidad = mail.count("@")
# if cantidad == 1:
#     print("bien")
# else:
#     print("Mal")

'''

inser()
Insertar en un lugar específico: 

'''
# jugadores = ['Angelito', 'Rodrigo', 'Tomas', 'Javier']
# jugadores.insert(1,"Lionel")
# print(jugadores)

# jugadores = ['Angelito', 'Rodrigo', 'Tomas', 'Javier']
# # jugadores.insert(15,"Lionel")
# jugadores.append("Lionel")
# print(jugadores)

'''tuplas'''
# list() => Listas => ordenadas y mutables. []
# tuple() => tuplas => Ordenadas e inmutables. ()
# int()
# str()
# float()
# bool()

# metodos que no van a estar: append, remove(), pop()...etc

# coordenadas = ("nombre", 9099,9.00, False,["lista"],("tuplass"))
# coordenadas = 9,8,7,6,5,4,3
# print(coordenadas)

## count() y index()
# cantidad = coordenadas.count("nombre ")
# cantidad = coordenadas.index("lista") #ValueError: tuple.index(x): x not in tuple
# cantidad = coordenadas.index(["lista"]) 
# print(cantidad)

'''conversión'''
# coordenadas = (0.545453,0.72342,0.765753)
# print(coordenadas)
# lista_coordenadas = [list(coordenadas).pop(), list(coordenadas).pop()] # [0.765753, 0.765753]
# print(coordenadas)
# print(lista_coordenadas)

# coordenadas = (0.545453,0.82342,0.965753)
# print(coordenadas) # (0.545453,0.72342,0.765753)
# lista_coordenadas = list(coordenadas) # [0.545453,0.72342,0.765753]
# elementoEliminado = [lista_coordenadas.pop(), lista_coordenadas.pop()]

# print(elementoEliminado)

'''Slices
Así como en el tipo de dato range generabamos una secuencia de números enteros:

range(inicio, fin, step) => range(0,10,2)

Los slices me permiten tomar una rebanada de una lista, mas grande:

Listas o tuplas => [lista de n elementos..][inicio:fin:step]
'''
## elementos ordenados = list, tuplas, str
# jugadores = ['Angelito', 'Lionel', 'Rodrigo', 'Tomas', 'Javier','Lionel']
# # ultimos_jugadores = jugadores[2::2] ## del jugador 2 al final, de dos en dos...
# ultimos_jugadores = jugadores[:3:] ## del principio al tercer jugador de uno en uno...

# print(ultimos_jugadores)

# ganancias = list(range(1,28))
# semana1 = ganancias[0:7:]
# semana2 = ganancias[7:14:]
# semana1 = sum(ganancias[0:7:])
# semana2 = sum(ganancias[7:14:])
# print(semana1)
# print(semana2)


listaDeListas = [["nombre1","categoria",int(9.00)],["nombre2","categoria",int(9.2434)]]
contador = 0
for elemento in listaDeListas:
    print(f'producto #{contador}: {elemento[0]}')
    contador += 1



##################### preguntas del código

'''Idea de una lista de listas'''
lista_principal = [["Lista secundaria"],["Otra lista secundaria"]]
print(lista_principal)

## Le appendeo elementos a la lista.
lista_principal.append(["nombre1","categoria1",int(9.87)])
lista_principal.append(["nombre2","categoria2",int(10.87)])
print(lista_principal)

'''
pregunta: Como ordenamos de z a A?
'''
## REcordemos que sort modifica la lista original! 
ganancias = list(range(1,28))
ganancias.sort(reverse=True)
print(ganancias)
'''
pregunta:  Si una lista es tipo alfabetico pero yo al llámarlo lo transformo a entero (.int) el dato cambia?

Si tengo la siguiente lista: 
posiciones = ["abc","90","45","9"]

En este caso si quiero convertir posiciones[0] ("abc") en int, me va a tirar un error. Con las demás posiciones 
está bien.'''

'''
pregunta: yo ahí ¿Podría agregar una función que me los enumere de la manera en la cual voy ingresando los datos?

Está la función enumerate que podemos usar en el bucle for, que nos permite obtener además de su elemento, la posición 
dentro del elemento ordenado. 

pregunta: si yo quiero que cuando me lo imprima diga por ejemplo "jugador1:Angelito" como debería hacer?
'''
listaCompleja = [["Lionel","Jug",999],["Enzo","jug",9],["Pedro","jug",8]]
for i, elemento in enumerate(listaCompleja):
    # print(f'El jugador en la posición {i} es: \n{elemento}')
    ## Si no me gusta, podría hacer lo siguiente, sin meterme en muchos bucles..
    print(f'El jugador en la posición {i} es: \nnombre:{elemento[0]}\ncategoria:{elemento[1]}\nprecio:{elemento[2]}\n')


## obvio que podemos usar las dos formas! 
contador =0
for elemento in listaCompleja:
    print(f'El jugador{contador}:{elemento[0]}')
    contador += 1
