# Escribí un programa que al ingresar dos textos muestre: si son iguales, un mensaje de bienvenida; si no son iguales, un mensaje de advertencia.



# def mensaje(texto1,texto2):
    
#     if (texto1 == texto2):
#         print ("Ingresaste dos textos iguales, sos bienvenido")
#     else:
#         print("Tus textos no son iguales")
        
# mensaje("Hola","Hola")

# # ¡Para practicar! Los operadores lógicos no solo son para condicionales, se pueden usar también en variables. 
# #Esto nos permite generar variables de tipo bool que usamos luego en algún condicional. 


# # variableBool = 45>50 or 50>39
# # usuario = edad>18 and tiempoRegistro>5000
# # actividad = login and permanencia>3600


# # Condicionales
# # 5. Pedile al usuario que ingrese su nombre. Si es "Lionel Messi", mostrale "usuario válido", sino, mostrá "Nombre incorrecto".
# def imprimirSiEsMessi(texto1):
    
#     if (texto1 == "Lionel Messi"):
#         print ("Usuario valido")
#     else:
#         print("Nombre incorrecto")
        
# imprimirSiEsMessi("Lionel Messi")        
# imprimirSiEsMessi("Delgado")   

# # 6. Creá un programa que al ingresar un número te informe si es positivo, negativo o igual a cero.

# def elNumeroEs(numero):
#     if(numero > 0):
#         print (f"{numero} es positivo")
#     elif (numero < 0):
#         print(f"{numero} es negativo")
#     else: 
#         print(f"{numero} es igual a cero")
        
# elNumeroEs(10)
# elNumeroEs(-40)
# elNumeroEs(0)

# # 7.  Pedí al usuario un número y verificá si es múltiplo de 2, 3 o de ambos.
# #retorna si es multiplo si el resto es 0
# def esMultiplo(n,x):  
#      n % x == 0
    
# usuarioN = int (input(f"verificar numero: "))

# if( (esMultiplo (usuarioN,2)) or (esMultiplo (usuarioN,3)) ):
#     print (f"El numero {usuarioN} es multiplo ")
# else:
#     print(f"El numero {usuarioN} NO es multiplo")
    


# 8. Escribí un programa que te pida una edad y puedas avisarle de los siguientes beneficios:

def beneficiosSegunEdad(edad):

    edad = int(input (f"Ingrese su edad para conocer sus beneficios:"))
    if(edad < 12):
        print("Entran gratis")
    elif(edad >= 12 and edad <= 17):
        print("25% de descuento")    
        
    elif(edad >= 18 and edad <= 69):
        print("15% de descuento")
    elif(edad >= 70):
        print("Entran gratis")        
    elif(edad != int): 
        print("Debe ingresar un numero")
    
beneficiosSegunEdad(70)    
       
# Menores de 12: entran gratis
# Entre 12 y 17: 25% de descuento
# Entre 18 y 69: 15% de descuento
# 70 o más: entran gratis
# Otro: error

