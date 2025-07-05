## Docstring y buenas prácticas
'''
La traducción de los parámetros escritos de esta manera: 

(numeros:list, señal:bool) -> None

Podría ser: esta función recibe PRFERENTEMENTE un primer parámetro de tipo list
y un segundo parámetro de tipo bool. No son obligatorios! por eso en
los docstring, agregamos el valor de "raise": para deolver un error en caso de que no 
funcione correctamente. 
Con " -> None " estamos diciendo que esta función no devuelve nada. Solo se ejecuta o imprime algo.

Si quiero especificar mas de un parámetro, tengo que usar el simobolo |

# def numeroPar(numeros:list | tuple , señal:bool) -> None:

Ahora mencionamos que el parámtro numeros puede ser de tipo list o tuple.
'''
# def numeroPar(numeros:list, señal:bool) -> None:
#     '''
#     descripción: Reconoce si un número es par o impar

#     argumentos / parametros / args : recibe una lista de números enteros y flotantes

#     return bool => True si es Par. False si no

#     raise: (opcionaal) => posibles errores,
#     '''
#     print(numeros)
#     return 

# numeroPar("a","s")

'''
módulo propio
'''
# import modulo ## para importar nuestro módulo propio, puedo hacerlo de forma similar que las demás librerías
# vistas mas adelante! 

# print(modulo.numeroPar(10))
# # modulo.menu(["Ingresar producto, Eliminar producto, Mostrar productos"],"Bienvenido a mi sistema! ")

# opciones = ["Ingresar producto", "Eliminar producto", "Mostrar productos"]
# modulo.menu(opciones ,"Bienvenido a mi sistema! ")


# modulo.variable1
# modulo.variable2


## módulos ( ya instalados - de terceros)

# math  / random  / datetime

## random =
'''
3 formas de importar los módulos. 

1 - El módulo completo
2 - Cada una de las funciones
3 - Una función en particular

'''

# import random 

# random.seed(90) ## en python no existe algo aleatorio. En este caso random usa un algoritmo.
# Este algoritmo sale de un número de entrada. Con seed de random especificamos ese número


# print(random.random())
# print(random.random())

# print(random.randint(0,100)) ## me devuelve un entero entre

# lista = [1,2,3,4,5,6,9,12]
# print(random.choice(lista))

# print(random.sample(lista,5)) # Valores únicos! 

## print(random.choices(lista,5))  ## error
# ypeError: The number of choices must be a keyword argument: k=5. Porque los 
# parámetros están desordenados! 

# print(random.choices(lista,k=5)) # no nos asegura valores únicos!

# import random
# lista = [1,2,3,4,5,6,9,12]
# random.shuffle(lista) ## Desordeno los elemtnso de una lista ordenados
# print(lista)



## Math! 
# import math as mt
# # import random as rm
# print(mt.sqrt(25)) ## Raiz cuadrada
# print(mt.sqrt(36)) ## Raiz cuadrada

# print(mt.pi) ## Variables como constante dentro del módulo
# print(mt.e)  ## Variables como constante dentro del módulo

# print(mt.pow(12.5,3)) ## 12.5^3 Exponencial
'''
La funcione de redondeo es una función que podríamos hacer nosotros en nuestro módulo
pero como ya está creada, nos permite ahorra tiempo y errores en desarrollo.
'''
# print(mt.floor(12.5)) ## redondeo hacia abajo
# print(mt.ceil(12.5)) ## Redondeo hacia arriba

# from random import randint as rt ## Apodamos a la función
# from random import randint, sample as rt ## Apodo solamente la última función! 

# from random import randint
# from math import pi
# from math import *
# print(randint(1,9))

# import datetime

# import math 
# math.nombreFuncion
# from math import *
# nombreFuncion

# from datetime import datetime as dt
# import datetime

# print(datetime.date.today())
# print(type(datetime.datetime.now())) # <class 'datetime.datetime'>

'''
No quiero comentarles una forma única de importar las librerías, pero esta 
es la mas común para datetime. En documentación pueden averiguar si una función en particular
está en el módulo datetime (solo datetime)
'''
from datetime import datetime as dt
print(dt.now().date())

fecha = "19/06/2025"
print(type(fecha)) # <class str>
fechaConvertida = dt.strptime("19/06/2025","%d/%m/%Y")
print(type(fechaConvertida)) # <class 'datetime.datetime'>


print(dt.now().date())
print(dt.now().date().day)
print(dt.now().date().month)
print(dt.now().date().year)

'''
Otras librerías importantes de python! 

## pandas! flask, fastAPI, TKinter, Flet
recomiendo leer la documentación de cada una antes de instalarlas! 
para instalar librerías de terceros, será necesario ejecutar por la terminal
lo siguiente: 

python -m pip install <nombreLibreria> 
## Donde <nombreLibreria> puede ser Pandas, flask, etc.
'''



