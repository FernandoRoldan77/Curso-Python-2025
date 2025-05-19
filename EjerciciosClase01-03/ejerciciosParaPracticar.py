# Ejercicios de práctica
# Creá un programa que le pida al usuario dos números y muestre el resultado de realizar: 
# suma, resta, multiplicación y división entre el primero y el segundo.
# ej: si ingreso 5 y 10 el resultado sería: La suma es 1, su multiplicación es 50. 

#Convierto el tipo String a int para que imprima los resultados matematicos
n1 = int( input (f"Ingresar primer numero: "  ))
n2 = int (input (f"Ingresar segundo numero: " ))


suma            = f"La suma de {n1} + {n2} es de: {n1 + n2}"
resta           = f"La resta de {n1} - {n2} es de: {n1 - n2}"
multiplicacion  = f"La multiplicacion de {n1} * {n2} es de: {n1 * n2}"

print (suma)
print (resta)
print(multiplicacion)
try:    
 division        = f"La division de {n1} / {n2} es de: {n1 / n2}"   
 print (division)
except ZeroDivisionError:
 print ("Error: No se puede dividir por cero")

#print(division)

# 1. 2.  Creá un programa que genere cálculos combinados: el doble de la suma del número uno + número dos.

nCombinados = (n1+n2) * 2
print (f"el doble de la suma entre {n1} y {n2} es de :", nCombinados) 

# 1.3. ¿Qué pasa en la división por cero? ¿Qué podríamos hacer?

#Use un try para levantar un except con ZeroDivisionError de Python para mostrar error



# 9. Ingresá la edad, si tiene CUD (como booleano), y si está jubilado (como booleano). Comentale de los siguientes beneficios: (¡Importante! las condiciones no están organizadas o pueden organizarse mejor).


# CUD mas Jubilacion : Ingreso gratis
# CUD sin jubilacion : Ingreso de $10000
# Mas de 15 años : Ingreso 15000
# Menos de 3 años: Ingreso gratis
# Mas de 3 años: $5000
# con jubilación y sin CUD: Ingreso gratis



# Para investigar: 
# Tenemos también la opción de usar estos operadores lógicos: 
# & y  | que representan a and y or respectivamente. ¿Sabés cuál es la diferencia? 


