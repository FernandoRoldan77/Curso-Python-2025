## Clase 12 => open (archivos de texto)
## txt, log, yml, toml, csv, dat
# open("adultos Python/Clase9/main.txt","modo")

## ¡modos distintos! 
# lectura (predeterminado) => r,  
# escritura, 
# lectura y escritura,
#  agregar.


# Clase9\main.txt
# C:\Users\USUARIO\Desktop\adultos python\Clase9\main.txt

# archivos = open("Clase9\main.txt")
# print(archivos) # <_io.TextIOWrapper name='Clase9\\main.txt' mode='r' encoding='cp1252'>

# archivos = open("Clase9/main.txt")
# print(type(archivos.read())) # <class 'str'>
# print(archivos.read())


## Problema : No me toma los acentos! 
# archivos = open("Clase9/main.txt")
# # <_io.TextIOWrapper name='Clase9\\main.txt' mode='r' encoding='cp1252'>
# print(archivos.read())


# # <_io.TextIOWrapper name='Clase9\\main.txt' mode='r' encoding='UTF-8'>
# archivos = open("Clase9/main.txt",encoding="UTF-8")
# print(archivos.read())

# archivos = open("Clase9/main.txt",mode="r",encoding="UTF-8")
# print(archivos.readlines()) # ['Papas\n', 'Verdulería\n', 'Mañana\n', '900']

# archivos = open("Clase9/main.txt",mode="r",encoding="UTF-8")

# lineas = archivos.readlines()# ['Papas\n', 'Verdulería\n', 'Mañana\n', '900']
# for linea in lineas:
#     print(linea)

# for linea in lineas:
#     print(linea.replace("\n",""))

## readline =>> Sin s!! 

# archivos = open("Clase9/main.txt",mode="r",encoding="UTF-8")
# print(archivos.readline())
# print(archivos.readline())
# print(archivos.readline())
# print(archivos.readline())

## modo => w write (escritura)
## modo => a append (agregar)
## modo => r+ (lectura y escritura)

# archivos = open("Clase9/mani.txt", mode="w",encoding="UTF-8") ## nos evitamos el error de abajo
# archivos = open("Clase9/mani.txt", mode="r",encoding="UTF-8") #FileNotFoundError: [Errno 2] No such file or directory: 'Clase9/mani.txt'
# archivos.write("Messi campeeon!")

# archivos = open("Clase9/main.txt", mode="a",encoding="UTF-8") #FileNotFoundError: [Errno 2] No such file or directory: 'Clase9/mani.txt'
# archivos.write("\nMessi campeeon!")

# archivos = open("Clase9/main.txt", mode="a",encoding="UTF-8")

# nombre = "Lautaro"
# categoria = "Messi"
# precio = 9999

# archivos.write(f"\n{nombre},{categoria},{precio}")


# archivos = open("Clase9/main.txt", mode="r",encoding="UTF-8")
# lineas = archivos.readlines()
# for linea in lineas:
#     print(linea.split(","))

# archivos = open("Clase9/main.txt", mode="r",encoding="UTF-8")
# # archivos.closed ## => True o False
# lineas = archivos.readlines()
# for linea in lineas:
#     print(linea.split(","))
# archivos.close()

# with open("Clase9/main.txt", mode="r",encoding="UTF-8") as archivos:
#     lineas = archivos.readlines()
#     for linea in lineas:
#         print(linea.split(","))
# with open("Clase9/main.txt", mode="a",encoding="UTF-8") as archivos:
#     archivos.write("\nRonaldo Campeeon")

### RECREO!! Volvemos 9 : 17 h


## Try-except  =>  Sintaxis
# try:
#     ## Lo que se puede romper!
# except ERROR:
#     ## mensaje del error

### Lo vamos a usar para salvar errores inesperados

### NameError

## print(tomate) # NameError: name 'tomate' is not defined

# try:
#     print(tomate)
# except NameError:
#     print("Variable no declarada")


# precio = int(input("ingresá un número: "))   # ValueError: invalid literal for int() with base 10: 'a'
# print(precio)
# try:
#     precio = int(input("ingresá un número: "))  # ValueError: invalid literal for int() with base 10: 'a'
#     print(precio) 
# except ValueError:
#     print("caracteres incorrectos, ingresá del 0 al 9")

# try:
#     precio = int(input("ingresá un número: "))  # ValueError: invalid literal for int() with base 10: 'a'
# except ValueError:
#     print("caracteres incorrectos, ingresá del 0 al 9")

# while True:
#     try:
#         precio = int(input("ingresá solo caracteres numéricos: "))  # ValueError: invalid literal for int() with base 10: 'a'
#         break
#     except ValueError:
#         print("caracteres incorrectos, ingresá del 0 al 9")

# print(precio)
# from datetime import datetime as dt
# while True:
#     try:
#         precio = int(input("ingresá solo caracteres numéricos: "))  # ValueError: invalid literal for int() with base 10: 'a'
#         break
#     except ValueError as e:
#         print("caracteres incorrectos, ingresá del 0 al 9")
#         with open("Clase9/main.log","a", encoding="utf-8") as archivo:
#             archivo.write(f"\n[ERROR]{dt.now()}:{e}")
# print(precio)


## FileNotFoundError
## IndexError
## TypeError

## FileNotFoundError => Cuando el archivo no existe
# from datetime import datetime as dt
# with open("Clase9/main2.log","r", encoding="utf-8") as archivo: # FileNotFoundError: [Errno 2] No such file or directory: 'Clase9/main2.log'
#     archivo.write(f"\n[ERROR]{dt.now()}:")

# from datetime import datetime as dt
# try:
#     with open("Clase9/main2.log","r", encoding="utf-8") as archivo: # FileNotFoundError: [Errno 2] No such file or directory: 'Clase9/main2.log'
#         archivo.write(f"\n[ERROR]{dt.now()}:")
# except FileNotFoundError:
#     with open("Clase9/main2.log","w+", encoding="utf-8") as archivo:
#         archivo.write(f"\n[ERROR]{dt.now()}:")


# nombre = input("Ingresá un precio: ").split()
# print(nombre[3]) # IndexError: list index out of range

# try:
#     precio =  int(input("Ingresá un precio: "))
#     nombre = input("Ingresá un precio: ").split()
#     print(nombre[3]) 
# except ValueError:
#     print("Te equivocaste")
# except IndexError:
#     print("Te equivocaste con la lista")

# try:
#     precio =  int(input("Ingresá un precio: ").isalpha()) ## isalpha si lo que ingresamos tiene caracteres alfabéticos
#     nombre = input("Ingresá un precio: ").split()
#     if len(nombre)<3:
#         print(nombre[3])
#     else:
#         print("rango indefinido")
# except ValueError:
#     print("Te equivocaste")

