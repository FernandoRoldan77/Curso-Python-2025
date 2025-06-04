
#Lista con productos y sus sublistas de productos
producto1      = ["Pera",   "Frutas",    10]
producto2      = ["Pan",    "Panaderia", 50]
producto3      = ["Cerveza","Bebidas",   100]
datosProductos = [producto1,producto2,producto3]

#Variables por si a futuro se quiere escalar las opciones en el inicio
opciones       = [("1. Agregar producto"),("2. Mostrar productos"),
                  ("3. Buscar producto"),("4. Eliminar producto"),("5. Salir \n")]    
                   
#Muestro las opciones a elegir                   
for o in opciones:
    print(o)           
    
#Ingreso numerico del usuario    
opcionesParaElUsuario    = int(input(f"Elegir mediante los numeros del 1 al 5 que quiere realizar: "))

#Para evitar que toque 0 el usuario y le vuelva a mostrar el menu por el case.
if(opcionesParaElUsuario == 0):
    print("Opcion invalida, por favor ingrese una opcion valida")
    opcionesParaElUsuario = int(input(f"Elegir mediante los numeros del 1 al 5 que quiere realizar: "))

#Mensajes en variables por si se quiere decir cambiar el mensaje para el usuario.
msjInicial       = (f"Seleccione con el numero de opcion que quiere hacer a continuacion: ")
msjVolverOSeguir = (f"Ingrese el numero 0 para volver al menu de opciones o el numero 5 para finalizar: ")

#Comienzo del programa
while(opcionesParaElUsuario <= 5):

  match opcionesParaElUsuario:
    case 0:                 #Una opcion para volver a mostrar el menu al usuario
        for o in opciones:
            print(o)
        opcionesParaElUsuario = int(input(msjInicial))
                      
    case 1: #Agrega un producto nuevo con sus correspondientes caracteristicas
        productoAgregado  = (input("¿Que producto queres agregar?: ").strip().capitalize())
        categoriaProducto = (input("¿Que categoria tiene?: ").strip().capitalize())
        precioProducto    = int((input("¿Cual es su precio?: ")))
        
        #Agrega una lista de producto, con categoria y precio a la lista de productos
        nuevoProducto = [productoAgregado,categoriaProducto,precioProducto]
        datosProductos.append(nuevoProducto)
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
        #Para evitar que el usuario elija otro caso del case
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
            print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido\n")
            opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
    case 2: #Muestra los productos
        for producto in enumerate(datosProductos): 
            print (producto) 
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
        #Para evitar que el usuario elija otro caso del case
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
            print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido \n")
            opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
    case 3: #Muestra el producto solicitado por el usuario
        pBuscado = input("¿Que producto desea buscar?: ").strip().capitalize()
        for producto in datosProductos:
            if(pBuscado in producto):       #palabra reservada para buscar si un elemento pertenece a una lista.
                print(f"Producto solicitado: {producto} \n")
                break  
            else:
                print(f"El producto {pBuscado} no esta en el sistema\n")    
                break #Para que el print no repita la longitud de la lista 
                
        opcionesParaElUsuario = int(input(msjVolverOSeguir)) 
            
        #Para evitar que el usuario elija otro caso del case
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
                print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido\n")
                opcionesParaElUsuario = int(input(msjVolverOSeguir))                       
                          
    case 4: #Para que el usuario borre algun producto en particular
    
        #Para que el usuario vea que quiere eliminar
        print("¿Que producto quiere borrar?\n")
        for producto in enumerate(datosProductos): 
            print (producto)     
            
        #Elegir mediante el indice que se quiere eliminar            
        posABorrar   = int(input("Seleccione el numero de posicion para borrar: "))         
        for indiceP, producto in enumerate(datosProductos):
                if(posABorrar >= len(datosProductos) ):
                    print("El numero de posicion es invalido, vuelva a elegir una opcion valida por favor\n")
                    break
                if( (indiceP == posABorrar)  ):
                        datosProductos.pop(posABorrar)
                        print("Producto borrado exitosamente\n")                                    
                      
        #Muestra que se borro exitosamente el producto                                                                       
        for producto in enumerate(datosProductos): 
            print (producto)                 
        
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
        #Para evitar que el usuario elija otro caso del case
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
           print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido\n")
           opcionesParaElUsuario = int(input(msjVolverOSeguir))
            
    case 5:
        print("Usted salio exitosamente del sistema")
        break 
        
    case _: #Para evitar que el usuario ingrese algo incorrecto
        print("Opcion invalida, por favor ingrese una opcion valida\n")
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
        '''Ideas de mejoras a futuro:
        
        * Me hubiese gustado poder hacer validaciones mas exigentes con respeto
          al ingreso de input, que solamente admita determinados valores y mediante try, catch y excepciones
          poder personalizar mas los mensajes de errores para el usuario como por ejemplo si ingresa un valor no numerico
          
        * Utilizar funciones para darle mas legibilidad al codigo y ahorrar lineas.
        
        * Ver alguna manera( no se si map(diccionario) con una key id y un valor que sea la lista del productos)  de acceder al producto y
          sus atributos para no depender de la longitud de la lista que requiere mas control de elementos para 
          evitar errores.
          
        * Hacer un login para ingresar usuarios y que queden registrados , esos usuarios podrian tener una lista como ejemplo de llenar un carro y comprar  
          productos o si es empleado tener el stock de los productos.
          
        '''
        
   
    
