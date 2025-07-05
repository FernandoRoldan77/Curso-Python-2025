'''
Generador de alias
Escribí una función que reciba un nombre y un apellido, y devuelva 
un aliascompuesto por 
las primeras 3 letras del nombre + las últimas 2 del apellido,
todo en mayúsculas. Pensemos en los slices de las listas que vimos…
'''

def generar_alias(nombre:str,apellido:str) -> str:
    '''
    ## descripción:
        genero un alias con 
        las primeras 3 letras del nombre + las últimas 2 del apellido

    Args: 
        nombre: El nombre de la persona
        apellido: El apellido de la persona

    Returns:
        alias de tipo str 
    '''
    pepito = nombre[:3] 
    apellido_str = apellido[-2:]

    return (pepito+apellido_str).upper()

# print(generar_alias("Lautaro","Messi"))


'''
Contador de vocales por palabra
Hacé una función que reciba una lista de palabras y devuelva un 
diccionario donde cada palabra sea una clave y el valor sea la cantidad de vocales
que tiene (a-e-i-o-u).
'''

palabras = [
    "sol", "montaña", "río", "elefante", "luz", "bicicleta", 
    "pan", "cielo", "aurora", "mar", "navegar", "flor", 
    "laguna", "árbol", "caminata", "tren", "universo", "pez"
]
diccionario = {"sol":1,"montaña":1}
def contadorVocales(palabras:list[str]) ->dict:
    diccionario = {}
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    ## la clave = palabrita in
    for palabra in palabras:
        contador = 0
        for letra in palabra:
            if letra in vocales:
                # diccionario[palabra] = 1 ## todas las claves con el mismo valor de 1
                # diccionario[palabra] += 1 ## KeyError. La clave no existe!
                contador += 1
        diccionario[palabra] = contador
    return diccionario

print(contadorVocales(palabras))

'''
Filtro de palabras largas
Hacé una función que reciba una lista de palabras y un número (x). 
Retorna una lista con las palabras que tienen más de x cantidad de letras.


Si quiero que esta función, también me permita obtener una lista de palabras
con menos de x cantidad de letras, ¿Cómo harían? Pensemos en los parámetos... optativos y estrictos
'''

def menu():
    opcion = "1"
    return opcion


def agregarProducto(nombre,categoria,precio) -> list[str,str,int]:
    '''
    ## recibe una lsita de 3 elementos

    ## Args: 
    -nombre : str 
    -categoria : str 
    -precio : str 

    ## returns: 
        lsita con los elementos agregados.
    '''
    print("producto agregado")
    listaProducto = []
    return listaProducto

def listaCompleta(lista:list[str,str,int]):
    '''
    Conectamos a la bd
    '''
    return True

while True:
    opcion = menu()
    if opcion == "1":
        nombre = input("ingresa tu nombre")
        categoria = input("ingresa tu nombre")
        while True:
            precio = input("ingresa tu nombre")
            if precio.isdigit():
                break
        listaCompleta(agregarProducto(nombre,categoria,precio))