# def suma():
#     print("funcion suma llamada! ")
#     return 34, 35, True, "Tomate"


# ## Return y print
# suma() # funcion suma llamada! 
# print(suma) # <function suma at 0x0000021988381440> => (34, 35, True, "Tomate")


# devuelve si el número es entero, positivo => bool
# def validacionNumerica():
#     valor = input("ingresá un número: ")
#     resultado = valor.isdigit()
#     while not resultado:
#         valor = input("ingresá un número: ")
#         resultado = valor.isdigit()
#     return resultado, valor

# print(validacionNumerica()) # (False, '-90')
# print(validacionNumerica()[0]) # False
# print(validacionNumerica()[1]) # -90

# boleano, valor = validacionNumerica()
# print(boleano)
# print(valor)

# def validacionNumerica():
#     resultado = False
#     while not resultado:
#         valor = input("ingresá un número: ")
#         resultado = valor.isdigit()
#     return resultado, valor



def validacionMail(mail):
    correcto = False
    if mail.count("@") == 1:
        division = mail.replace("@"," ").split(" ")
        if str(division[1])=="gmail.com":    
            if str(division[0]).isdigit():
                return correcto
            if len(mail)>8 and len(mail)<30:
                correcto = True
    return correcto

# print(validacionMail("1234@gmail.com")) # False
# print(validacionMail("lautaro@gmail.com")) # True
# print(validacionMail("lautaro@hotmail.com")) # False
# print(validacionMail("        @        ")) # False
# print(validacionMail("        @gmail.com")) # False
# print(validacionMail("Lautaro dos@gmail.com")) # ¿? False
# print(validacionMail("Lautaro gmail.com@gmail.com")) # True  # Salvamos ete error:


def validacionMail(mail):
    correcto = False
    if mail.count("@") == 1:
        division = mail.replace("@"," ").split(" ")
        if len(division)==2 and str(division[1])=="gmail.com":    
            if str(division[0]).isdigit():
                return correcto
            if len(mail)>8 and len(mail)<30:
                correcto = True
    return correcto

print(validacionMail("Lautaro gmail.com@gmail.com"))

opciones = ["Ingresar elementos","Ver los productos",
            "Eliminar productos","Buscar productos","Ver partido","Comprar entradas","Salir"]
def menu(listaDeOpciones,TituloMenu): ## POO
    print(f'{TituloMenu}')
    print("#"*20)
    for opcion in listaDeOpciones:
        print(opcion)
    print("#"*20)

# menu(opciones,"Ingresa una de las opciones! ")