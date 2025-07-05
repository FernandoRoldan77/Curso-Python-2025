## En los módulos podemos encontrar funciones. 
def numeroPar(numero:int) -> bool:
    '''
    descripción: Reconoce si un número es par o impar

    argumentos / parametros / args : recibe una lista de números enteros y flotantes

    return bool => True si es Par. False si no

    raise: (opcionaal) => posibles errores,
    '''
    if numero % 2 == 0:
        return True
    else:
        return False

def menu(opciones:list, mensaje: str) -> None:

    '''
    Descripción : imprimos cada una de las opciones de la lista

    args : lista de opciones => str

    return : None

    Raise: Si le paso un entero, se rompe.
    '''
    print(mensaje)
    for opcion in opciones:
        print(f'{opcion}\n')

## También podemos encontrar variables! 
variable1 = True
variable2 = [True,"Toamte"]

'''
Es importante en los módulos que todas las funciones estén bien documentadas
con lo que vimos al principio de la clase: Docstring y buenas prácticas.
'''