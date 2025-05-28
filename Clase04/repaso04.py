# nombres = ["  Lionel", "andres ", "MARIA", " camila ", "JUAN",  "rodrigo", "a riel  ", "   lucas", "MARTIN", " RomarIO", "Ezequiel", " mateo", "LAURA", " soledad", "CAR LOS ",
#            " pedro ", "FERNANDA", " elena", "AGUSTINA", "jorge", "  victoria", "dIEGO", "Sofia  ", "alberto ", "ANA", " juLIETA", "MARIANO", "  delfina ", "NOELIA", " emmanuel"]

# tipo de dato  = ["lionel","tomas",False,90,9.0,[True,True]]
# orden del dato= [0       ,  1    ,  2  , 3, 4 ,[True,True]]
# orden del dato= [0       ,  -5   ,  -4 ,-3, -2,       -1  ]

# Accedo a cada elemento por su posición
# nombres[0]
# nombres[1]
# nombres[-1]

# Mutable => podemos cambiar los valores dentro de la lista.

'''
1 A
'''
# El trabajador Lionel, realizó 12 h hoy.
# nombres = ["  Lionel", "andres ", "MARIA", " camila ", "JUAN",  "rodrigo", "a riel  ", "   lucas", "MARTIN", " RomarIO", "Ezequiel", " mateo", "LAURA", " soledad", "CAR LOS ",
#            " pedro ", "FERNANDA", " elena", "AGUSTINA", "jorge", "  victoria", "dIEGO", "Sofia  ", "alberto ", "ANA", " juLIETA", "MARIANO", "  delfina ", "NOELIA", " emmanuel"]

# for nombre in nombres:
#     # nombre = nombre.strip().capitalize().replace(" ","") ## Cualquiera de las dos son correctas!
#     # nombre = nombre.replace(" ","").capitalize() ## mejor maneraaa
#     print(f'El trabajador {nombre}, realizó 12 h hoy')

# contador = 0
# while contador < len(nombres):
#     nombre = nombres[contador].replace(" ","").capitalize() ## mejor maneraaa
#     print(f'El trabajador {nombre}, realizó 12 h hoy')
#     contador += 1

# nombres = ["  Lionel", "andres ", "MARIA", " camila ", "JUAN",  "rodrigo", "a riel  ", "   lucas", "MARTIN", " RomarIO", "Ezequiel", " mateo", "LAURA", " soledad", "CAR LOS ",
#            " pedro ", "FERNANDA", " elena", "AGUSTINA", "jorge", "  victoria", "dIEGO", "Sofia  ", "alberto ", "ANA", " juLIETA", "MARIANO", "  delfina ", "NOELIA", " emmanuel"]
# horas_trabajadas = [7, 9, 13, 7, 6, 10, 11, 13, 10, 8, 9, 10,
#                     13, 14, 6, 14, 10, 9, 7, 7, 13, 14, 6, 14, 10, 7, 6, 10, 6, 12]

'''
1 B
'''
# contador = 0
# for nombre in nombres:
#     nombre = nombre.replace(" ", "").capitalize()
#     print(
#         f'El trabajador {nombre}, realizó {horas_trabajadas[contador]} h hoy')
#     contador += 1

'''
2 B
'''

# Ahora esta nueva lista acentúa a algunas  marías y otras no…

# nombres_marias = ["  Lionel", "andres ", "MARíA", " camila ", "JUAN",  "rodrigo", "a riel  ", "maría ", "   maria", "MARTIN", " RomarIO", "Ezequiel", " mateo", "LAURA", " soledad", "CAR LOS ",
#                   " pedro ", "FERNANDA", " elena", "AGUSTINA", "jorge", "  victoria", "dIEGO", "Sofia  ", "alberto ", " MaRI a", "ANA", " juLIETA", "MARIANO", "  delfina ", "NOELIA", " emmanuel", "Maria", "maría"]

# contador = 0
# for nombre in nombres_marias:
#     nombre = nombre.replace(" ", "").capitalize()
#     if nombre == "María" or nombre == "Maria":
#         nombre = nombre.replace("i", "í")
#     print(f'El trabajador {nombre}, realizó h hoy')
#     contador += 1

# horas_trabajadas = ['13 h', '11 hs', '13 horas', '11 h', '6 h', '12 horas', '7 h', '12 hs', '8 h', '14 h', '6 h', '6 h', '9 h', '6 h', '7 h', '6 h', '6 h', '13 h', '6 h', '8 h', '8 h', '11 h', '14 h', '10 h', '11 h', '11 h', '12 h', '7 h', '8 h', '6 h']
# contador = 0
# for horas in horas_trabajadas:
#     contador += float(horas.split()[0])
#     # print(horas.replace(" horas","").replace(" hs","").replace(" h",""))
# print(contador)



'''###################################### EJERCICIO 1 B HECHO CON DOS BUCLES ######################################'''
# nombres = ["  Lionel", "andres ", "MARIA", " camila ", "JUAN",  "rodrigo", "a riel  ", "   lucas", "MARTIN", " RomarIO", "Ezequiel", " mateo",
#            "LAURA", " soledad", "CAR LOS ", " pedro ", "FERNANDA", " elena", "AGUSTINA", "jorge", "  victoria", "dIEGO", "Sofia  ", "alberto ",
#            "ANA", " juLIETA", "MARIANO", "  delfina ", "NOELIA", " emmanuel"]

# horas_trabajadas = [7, 9, 13, 7, 6, 10, 11, 13, 10, 8, 9, 10,
#                     13, 14, 6, 14, 10, 9, 7, 7, 13, 14, 6, 14, 10, 7, 6, 10, 6, 12]

# for pos_nombre in range(len(nombres)):
#     for pos_horas in range(len(horas_trabajadas)):
#         if pos_nombre == pos_horas:
#             nombre_limpio = nombres[pos_nombre].replace(" ", "").capitalize()
#             print(f"El trabajador {nombre_limpio}, realizó {horas_trabajadas[pos_horas]} h hoy")