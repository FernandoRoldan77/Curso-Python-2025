# Ejercicios de bucles while, for y condicionales
# Genera un print según las listas disponibles: 

nombres = [ "  Lionel", "andres ", "MARIA", " camila ", "JUAN",  "rodrigo", "a riel  ", "   lucas", 
            "MARTIN", " RomarIO", "Ezequiel", " mateo", "LAURA", " soledad", "CAR LOS ", " pedro ", "FERNANDA", 
            " elena", "AGUSTINA", "jorge", "  victoria", "dIEGO", "Sofia  ", "alberto ", "ANA", " juLIETA", 
            "MARIANO", "  delfina ", "NOELIA", " emmanuel"]



def trabajadorPorHoras(trabajador):
    trabajador = trabajador.strip().capitalize() #Para sacar los espacios en blanco y que los nombres inicien en mayuscula
    
    for e in nombres:
     e = e.strip().capitalize() #Para sacar los espacios en blanco y que los nombres inicien en mayuscula
     
     if( e == trabajador):
      return trabajador
    
   
# # El trabajador Lionel, realizó 12 h hoy..
# trabajadorPorHoras("Lionel") 

# # El trabajador Andres, realizó 12h hoy..
# trabajadorPorHoras("Andres") 

# # El trabajador Maria, realizó 12 h hoy..
# trabajadorPorHoras("Maria")

# Lo importante es que cambie el nombre del trabajador por el momento. 

# Si además a la lista de nombres, le agregamos la lista de horas trabajadas?
horas_trabajadas = [7, 9, 13, 7, 6, 10, 11, 13, 10, 8, 9, 10, 13, 14, 6, 14, 10, 9, 7, 7, 13, 14, 6, 14, 10, 7, 6, 10, 6, 12]


def buscarCuantasHorasTrabajo(trabajador,horasqueTrabajo):
    horasSinRepetidos = set(horas_trabajadas)
    for h in horasSinRepetidos:     
    
     if( h == horasqueTrabajo):
      t = trabajadorPorHoras(trabajador)
      
      return print(f"El trabajador {t} realizó {horasqueTrabajo} h hoy")
    

# Debe dar como resultado: 

# El trabajador Lionel, realizó 7 h hoy..

buscarCuantasHorasTrabajo("Lionel" ,7)
# El trabajador Andres, realizó 9 h hoy..
buscarCuantasHorasTrabajo("Andres" ,9)

# El trabajador Maria, realizó 13 h hoy..
buscarCuantasHorasTrabajo("Maria" ,13)



# ¡importante! 
# Las dos cadenas tienen la misma longitud, al nombre de la posición 0 le corresponde el horario de la posición 0… Intentá resolverlo de esta manera. Prestá atención a los métodos de cadena y su orden. 
# Si sabes como hacerlo de otra forma, adelante! 


# Con la lista de nombres anterior:
# Contá la cantidad de personas que se llaman Maria
# Ahora esta nueva lista acentúa a algunas  marías y otras no…

nombres_marias= [ "  Lionel", "andres ", "MARíA", " camila ", "JUAN",  "rodrigo", "a riel  ","maría ", "   maria", 
                  "MARTIN", " RomarIO", "Ezequiel", " mateo", "LAURA", " soledad", "CAR LOS ", " pedro ", "FERNANDA", 
                  " elena", "AGUSTINA", "jorge", "  victoria", "dIEGO", "Sofia  ", "alberto "," MaRI a" ,"ANA", " juLIETA", 
                  "MARIANO", "  delfina ", "NOELIA", " emmanuel","Maria","maría"]


# Contá la cantidad de marías que hay en esta lista. 
def contarPorNombre(trabajador):
    trabajador = trabajador.strip().capitalize() #Para sacar los espacios en blanco y que los nombres inicien en mayuscula
    contador   = 0
    for e in nombres:
     e = e.strip().capitalize() #Para sacar los espacios en blanco y que los nombres inicien en mayuscula
     if( e == trabajador):
      contador = contador +1
    return contador

contarPorNombre("Maria")
# Spoiler: No es el mismo número 😀


# Con la lista de horas_trabajadas: 
def contarLosQueTrabajaronMasDe(hora):
    contarHoras = 0
    for h in horas_trabajadas:     
     if( h > hora):
      contarHoras = contarHoras +1
      
    return contarHoras
    
def contarLosQueTrabajaronMenosDe(hora):
    contarHoras = 0
    for h in horas_trabajadas:     
     if( h < hora):
      contarHoras = contarHoras +1
      
    return contarHoras    
    
def contarLosQueTrabajaronMismaCantidad(hora):
    contarHoras = 0
    for h in horas_trabajadas:     
     if( h == hora):
      contarHoras = contarHoras +1
      
    return contarHoras    
# Contá la cantidad de personas que trabajaron más de 8 horas. 

# ¿Podrías hacer un informe de las personas que trabajaron más de 8 hs, las que trabajaron menos y las que trabajaron justo 8 horas?

print (f"La cantidad de personas que trabajaron mas de 8 horas es de: {contarLosQueTrabajaronMasDe(8)}")
print (f"La cantidad de personas que trabajaron menos de 8 horas es de: {contarLosQueTrabajaronMenosDe(8)}")
print (f"La cantidad de personas que trabajaron justo  8 horas es de: {contarLosQueTrabajaronMismaCantidad(8)}")
# Hubo cambios en la empresa, y el empleado nuevo en la base de datos completó el campo de horas_trabajadas con la h de esta manera: 

# horas_trabajadas = ['13 h', '11 h', '13 h', '11 h', '6 h', '12 h', '7 h', '12 h', '8 h', '14 h', '6 h', '6 h', '9 h', '6 h', '7 h', '6 h', '6 h', '13 h', '6 h', '8 h', '8 h', '11 h', '14 h', '10 h', '11 h', '11 h', '12 h', '7 h', '8 h', '6 h']

# Generá un bucle que sume los elementos de esta nueva lista.

# ¡Ayuda! Es mucho más fácil si utilizamos el método split() o replace…
