    
# Escribí un programa que tome un número y muestre: 

# a. su cuadrado
# b. cuánto da su división entera por n

# Ej: si ingreso 5,y la division entera por 4 la salida debe ser algo así: 
#El cuadrado de 5 es 25 y su división por 4 entera es…. 

# Escribí un programa que al ingresar un número me devuelva lo siguiente: 
# “Ingresaste el número 5: su cuadrado es 25, su división por dos es 2”
# “Ingresaste el número 50: su cuadrado es 2500, su división por dos es 25”
# “Ingresaste el número 7: su cuadrado es 49, su división por dos es 3”

# n2 = 5
# n3 = 50 
# n4 = 7

# print (f"Ingresaste el número {n2}: su cuadrado es {n2 **2}, su división por {n2} es {int(n2/2)}")
# print (f"Ingresaste el número {n3}: su cuadrado es {n3 **2}, su división por {n3} es {int(n3/2)}")
# print (f"Ingresaste el número {n4}: su cuadrado es {n4 **2}, su división por {n4} es {int(n4/2)}")

#Mas legible usando una funcion 
def calcularCuadradoYDivisionEnteraDe(numero):
 
  print (f"Ingresaste el número {numero}: su cuadrado es {numero **2}, su división por {numero} es {int(numero/2)}")

# Llamada a la función
calcularCuadradoYDivisionEnteraDe(5)
calcularCuadradoYDivisionEnteraDe(50)
calcularCuadradoYDivisionEnteraDe(7)