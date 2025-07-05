# Diccionarios dict
'''Como crear un diccionario
sintaxis => nombreVariable = {}

Incluye llave de apertura y llave de cierre.

'''

# persona = {} # diccionario vacío
# print(type(persona)) # <class 'dict'>
# numero = 0
# print(type(numero))
# numero2 = 0.0
# print(type(numero2))
'''
1. Las claves tienen que ser únicas.
2. la clave peude ser cualquier tipo de dato inmutable => int, tuplas, string.
3. Los valores pueden ser cualquier tipo de dato!! str, int, list, dict, función, etc
'''


# persona = {
#     "clave":"valor",
#     "clave":"Messi"
#     }

# persona = {
#     "nombre":"Arturo",
#     "Apellido": "Vidal",
#     "edad":37,
#     "Altura":1.7,
#     "Hijos" : ["hijo1","hijo2","hijo3"], # Esta coma es buena práctica
#     }

# print(persona)
# ## Lista de diccionarios.
# personas = [persona, persona]

'''¿por que buena práctica la coma al final?

Las comas al final del último elemento de una tupla, lista o diccionario, son redundantes en la práctica
pero también son importantes para los controladores de versiones como git, lo que nos evita errores. Git es una tecnología
que nos permite trabajar de forma colaborativa con códigos. En todo rubro IT se usa git con alguna herramienta (Github, Gitlab, Gitea entre otros) 
En menor medida, nos evita errores al momento de agregar elementos al diccionario. Si no tenemos la coma la tenemos que agregar nosotros 🤷🤷
'''


# persona = {
#     "nombre":"Arturo",
#     "Apellido": "Vidal",
#     37:"Edad",
#     (9,8):"Coordenada",
#     "Hijos" : ["hijo1","hijo2","hijo3"], # Esta coma es buena práctica
#     }
# print(persona)

'''Como accedemos a sus claves y valores'''

# persona = {
#     "nombre":"Arturo",
#     "Apellido": "Vidal",
#     "Edad":37,
#     "Altura":1.7,
#     "Hijos" : ["hijo1","hijo2","hijo3"], # Esta coma es buena práctica
#     }
'''
Accedo a cada uno de los valores, por su clave! '''
# print(persona["nombre"]) # Arturo
# print(persona["Altura"]) # 1.7
# print(persona["Hijos"][0]) # ['hijo1', 'hijo2', 'hijo3']


'''
Esto sería un diccionario de diccionario => persona = {clave:{}}.
Este diccionario tiene el par clave-valor de la siguiente manera =>  clave-diccionario
Esto es muy común, y no me dificulta el acceso a los elementos. Solo tengo que saber en que 
diccionario estoy parado :D 

'''
# persona = {"Jugador1": {
#     "nombre": "Arturo",
#     "Apellido": "Vidal",
#     "Edad": 37,
#     "Altura": 1.7,
#     "Hijos": ["hijo1", "hijo2", "hijo3"],  # Esta coma es buena práctica
# }}

'''keys() y values()'''
# print(persona.keys()) ## Todas las claves que tiene persona como diccionario
# ## Diccionario de diccionarios, nos queda mucho mas ordenado.
# print(persona["Jugador1"]["nombre"])

# redes = {
#     "nombre":"Arturo",
#     "Apellido": "Vidal",
#     "Edad":37,
#     "Altura":1.7,
#     "Hijos" : ["hijo1","hijo2","hijo3"],
#     }

'''values() keys()'''

# print(redes.values()) # dict_values(['Arturo', 'Vidal', 37, 1.7, ['hijo1', 'hijo2', 'hijo3']])
# print(redes.values()[0]) # TypeError: 'dict_values' object is not subscriptable


'''dict_values => Es un tipo de dato iterable! 
Como es iterable puedo recorrerlo.
'''

# for valor in redes.values():
#     print(valor)

## otra forma de acceder a un elemento. Esta forma es la menos usada, porque pasamos a 
## un tipo de dato iterable, a una representación de una lista.

# print(list(redes.values())[1])



# print(redes.values()) # <built-in method values of dict object at 0x000001CA34F31DC0>
# print(redes.keys())


# persona = {
#     "nombre":"Arturo",
#     "Nombre": "Lionel",
#     "Edad":37,
#     "Altura":1.7,
#     "Hijos" : ["hijo1","hijo2","hijo3"],
#     }
# print(persona)

'''Como agrego elementos a un diccionario. 
1. Agrego por la clave
2. setdefault()
'''

# cliente = {}
# print(cliente)
# cliente["nombre"] = "Gary"
# cliente["apellido"] = "Medel"
# cliente["nombre"] = "Pablo"
# print(cliente)
# print("Subo cliente a mi bd")

# cliente = {}
# print(cliente)
# cliente.setdefault("nombre","Gary")
# cliente.setdefault("nombre","Lionel") # setdefault nos agrega un elemento si la clave no existe! 
# print(cliente)

'''
Como elimino elementos
1. pop() => elimina y guarda el elemento (Como en las listas)
2. popitem() => elimina el último elemento del diccionario
3. clear() => Limpia todo el diccionario. No deja nada! 
'''

# persona = {
#     "nombre":"Arturo",
#     "apellido": "Vidal",
#     "Edad":37,
#     "Altura":1.7,
#     "Hijos" : ["hijo1","hijo2","hijo3"],
#     }
# print(persona)
# persona.pop("Edad") # el pop elimina un elemento en particular del diccionario
# persona.popitem()   # El popitem elimina el último elemento del diccionario
# print(persona)

# persona = {
#     "nombre":"Arturo",
#     "apellido": "Vidal",
#     "Edad":37,
#     "Altura":1.7,
#     "Hijos" : ["hijo1","hijo2","hijo3"],
#     }
# print(persona)
# eliminado = persona.pop("Edad") 
# print(eliminado)
# print(persona)

# persona.clear()
# print(persona)

# persona = {
#     "nombre":"Arturo",
#     "apellido": "Vidal",
#     "Edad":37,
#     "Altura":1.7,
#     "Hijos" : ["hijo1","hijo2","hijo3"],
#     }

# print(persona["nombre"])
# print(persona.get("Copas_Americas"))
# if persona.get("Copas_Americas") == None:
#     print("No hay copas americas")

# print(persona["Copas_Americas"])


### Si quiero agregar mas de un elemeneto al diccionario:
# persona = {}

# persona.setdefault("nombre","Andres")
# persona["apellido"] = "Messi"

# print(persona)


'''Funcioness'''
'''
- Bloque de código que se va a repetir.
- Tengo que resolver un problema concreto.. 
. Puede recibir o no informaciónc . Entrada - Proceso - Salida
'''

## nombre funciones = no puede ser una palabra reservada de python
## nombre funcion => Tiene que ser representativo

'''
'''
# def nombre_funcion_que_realiza_la_suma():
#     ## código a ejecutar en la función

# Creamos la función
# def saludo():
#     '''
#     Proceso
#     '''
#     print("Bienvenido Gary Medel")

# print(saludo) # <function saludo at 0x0000026DD3391440>

# ## llamado/ejecutamos a la función
# saludo() # Bienvenido Gary Medel

## funciones con parámetros
# def suma(a,b):
#     '''
#     Proceso
#     '''
#     print(a + b)

# suma() # TypeError: suma() missing 2 required positional arguments: 'a' and 'b'
# suma(90,10)
# suma("hola",0) # TypeError: can only concatenate str (not "int") to str


## El print lo guarda en memoria? NO.
# def suma(a,b): #  # <function suma at 0x0000026DD3391440>
#     '''
#     Proceso
#     '''
#     print(a + b)

# def saludo(nombre):
#     print(f'Bienvenido {nombre}')
#     suma(10,90)

# saludo("Lihuel")}

# def nombreFuncion(param1, param2):
#     ## proceso de código de la función
#     print("Chau")

# nombreFuncion("param1"," param2")


# def agregar():
#     lista = []
#     contador = 0
#     while contador < 4:
#         nombre = input("ingresá un nombre: ")
#         lista.append(nombre)
#         contador += 1
#     print(lista)

# agregar()
