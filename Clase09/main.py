## while true con opciones
# import modulo1

# while True:
#     opcion = input("ingresá una opción").strip()
#     if opcion == "1":
#         nombre = "Lautari"
#         categoria = "precio"
#         precio = 90
#         modulo1.agregarProducto(nombre,categoria,precio)
#     break


## colorama! función: sirve para darle color a la terminal

# from colorama import Fore, Back, init
# # from colorama import *
# init(autoreset=True)
# print(Fore.RED + "Bienvenido")
# print(Fore.GREEN + "Bienvenido")
# print(Back.GREEN + "Bienvenido de fondo 🫶 ")
# print("Sin formatoo")

# from datetime import datetime as dt
# import modulo1

# while True:
#     # opcion = int(input("ingresá una opción").strip())
#     print("Bienvenidoo")
#     while True:
#         opcion = input("ingresá una opción").strip()
#         if opcion.isdigit():
#             break
#         else:
#             print("la opción tiene que ser numérica! ")

#     if opcion == "1":
#         nombre = "Lautari"
#         categoria = "precio"
#         precio = 90
#         try:
#             precio/0
#         except ZeroDivisionError as e:
#             ruta = "Ruta al archivo"
#             with open("0_Repasos/01_07/main.log", mode="a") as archivo:
#                 archivo.write(f"[ERROR] - {dt.now()} - {e}\n")
#     if opcion == "2":
#         print("gracias")
#     break

