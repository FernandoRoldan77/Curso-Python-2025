# Esta lista está muy bien, pero debería estar vacío y poder rellenarla. Si tiene elementos deberíamos poder editarlos! 
p1          = ["Pera",   "Frutas",    10]
p2          = ["Pan",    "Panaderia", 50]
p3          = ["Cerveza","Bebidas",   100]
productos   = [p1,p2,p3]

## Excelente! El número no es necesario, te lo da la propia lista. La tupla tampoco es necesario! Si queremos darle algún estilo en particular a la salida, se lo damos con f-string.
opciones       = [("1. Agregar producto"),("2. Mostrar productos"),
                  ("3. Buscar producto"),("4. Eliminar producto"),("5. Salir \n")]    
                   
for o in opciones:
    print(o)           
    
## Acá si ingreso un valor de tipo float ya lo rompo. O si ingreso una letra pasa lo mismo. ValueError: 
opcionesParaElUsuario    = int(input(f"Elegir mediante los numeros del 1 al 5 que quiere realizar: "))

## bien pensado! 
if(opcionesParaElUsuario == 0):
    print("Opcion invalida, por favor ingrese una opcion valida")
    ## Acá pasa lo mismo que te mencionaba mas arriba.
    opcionesParaElUsuario = int(input(f"Elegir mediante los numeros del 1 al 5 que quiere realizar: "))


msjInicial       = (f"Seleccione con el numero de opcion que quiere hacer a continuacion: ")
msjVolverOSeguir = (f"Ingrese el numero 0 para volver al menu de opciones o el numero 5 para finalizar: ")

## Esto está muy bien! 
while(opcionesParaElUsuario <= 5):

  match opcionesParaElUsuario:
    case 0:               
        for o in opciones:
            print(o)
        ## En este pasa lo mismoo
        opcionesParaElUsuario = int(input(msjInicial))
                      
    case 1: 
        ## Acá nos sobran paréntesis. Si no es parámetro de una función, o tupla, no le ponemos paréntesis. Esa línea es lo mismo que esto:
        # productoAgregado  = input("¿Que producto queres agregar?: ").strip().capitalize()

        productoAgregado  = (input("¿Que producto queres agregar?: ").strip().capitalize())
        # Por lo general esperamos que los productos agregados el usuario los agregue
        # como quiera, por ahí hay dos marcas de igual nombre que varía su letra mayúscula... Nosotros le aplicamos los métodos de cadena 
        # para validar y comparar productos! 
        categoriaProducto = (input("¿Que categoria tiene?: ").strip().capitalize())
        precioProducto    = int((input("¿Cual es su precio?: "))) ## Acá nos corta de nuevoo
        
        #Agrega una lista de producto, con categoria y precio a la lista de productos
        nuevoProducto = [productoAgregado,categoriaProducto,precioProducto]
        productos.append(nuevoProducto)
        # Acá lo mismo
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
        ## Muy bien esta idea! Pero le puedo ingresar los valores dos veces y si agrego dos veces la opción 4, voy directo a eliminar... 
        ## Estas validaciones están bien, pero podríamos hacerlas con un bucle while capaz y algún contador. Si el usuario ingresa 10 veces la opción incorrecta es problema suyo.
        # nosotros le dcimos que ingrese correctamente. 
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
            print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido\n")
            opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
    case 2:
        # Este enumerate está bien usado, no usamos el index pero queda bíen. Por lo general cuando no usamos el index, no ponemos enumerate... usamos algún contador o algo.
        ## la forma correcta sería: for index, producto in enumerate(productos): 
        for producto in enumerate(productos): 
            print (producto) 
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
        ## Acá te comento lo mismo que lo de arriba!
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
            print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido \n")
            opcionesParaElUsuario = int(input(msjVolverOSeguir)) ## Este se rompee :(
        
    case 3: 
        pBuscado = input("¿Que producto desea buscar?: ").strip().capitalize() ## Muy bien acá formateado todo 
        for producto in productos:
            if(pBuscado in producto): 
                print(f"Producto solicitado: {producto} \n")
                break
                
        else:
                print(f"El producto {pBuscado} no esta en el sistema\n")    
                break 
                
        opcionesParaElUsuario = int(input(msjVolverOSeguir))         
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
                print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido\n")
                opcionesParaElUsuario = int(input(msjVolverOSeguir))                       
                          
    case 4:
        ## Muy bien esta parteee
        print("¿Que producto quiere borrar?\n")
        for producto in enumerate(productos): 
            print (producto)     
        
        ## Acá lo mismo, aunque el le digamos que ingrese el número entero y positivo de 0 a 5, tenemos que validar el resto.
        posABorrar   = int(input("Seleccione el numero de posicion para borrar: "))         
        for indiceP, producto in enumerate(productos):
                if(posABorrar >= len(productos) ):
                    print("El numero de posicion es invalido, vuelva a elegir una opcion valida por favor\n")
                    break
                if( (indiceP == posABorrar)  ):
                        productos.pop(posABorrar)
                        print("Producto borrado exitosamente\n")                                    
                      
        #Muestra que se borro exitosamente el producto Perfectooo                                                                     
        for producto in enumerate(productos): 
            print (producto)                 
        
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
    
        if( (opcionesParaElUsuario != 0) and (opcionesParaElUsuario != 5) ):
           print(f"El numero: {opcionesParaElUsuario} es invalido, seleccione un numero valido\n")
           opcionesParaElUsuario = int(input(msjVolverOSeguir))
            
    case 5:
        print("Usted salio exitosamente del sistema")
        break 
        
    case _:
        print("Opcion invalida, por favor ingrese una opcion valida\n")
        opcionesParaElUsuario = int(input(msjVolverOSeguir))
        
        '''
        
        Ideas de mejoras a futuro:
        
        * Me hubiese gustado poder hacer validaciones mas exigentes con respeto
          al ingreso de input, que solamente admita determinados valores y mediante try, catch y excepciones
          poder personalizar mas los mensajes de errores para el usuario como por ejemplo si ingresa un valor no numerico
          ## FER CON RESPECTO A ESTO, ES POSIBLE! SI USAMOS LOS MÉTODOS DE CADENA POR EJEMPLO ISDIGIT, PODEMOS VALIDAR VARIAS COSAS... 
        
        *tambien formas mas eficientes para que el usuario pueda regresar a opciones anteriores mas personalizadas y no genericas a todo el menu
          
        * Utilizar funciones para darle mas legibilidad al codigo y ahorrar lineas.
        ## ESTO LO VAMOS A VER EN LAS PRÓXIMA CLASES :D
        
        * Ver alguna manera( no se si map(diccionario) con una key id y un valor que sea la lista del productos)  de acceder al producto y
          sus atributos para no depender de la longitud de la lista que requiere mas control de elementos para 
          evitar errores.
          ## CON LOS DICCIONARIOS TODO ESTO ES UN POCO MAS SIMPLE, U ORDENADO AL MENOS 
          
        * Hacer un login para ingresar usuarios y que queden registrados , esos usuarios podrian tener una lista como ejemplo de llenar un carro y comprar  
          productos o si es empleado tener el stock de los productos.
          ### EEEEEH YA NOS METIMOS CON TODO! LOS LOGIN NO SON COSA TAAN SIMPLE, POR LA CONTRASEÑA MAS QUE NADA... LO DEMÁS PODEMOS HACERLO INCLUSO CON LISTAS O DICCIONARIOS.
          
        '''

        '''
        Fer estuvo muy bien tu pre-entrega! Te dejo algunos comentarios para que puedas tenerlos en cuenta para futuros códigos. 
        Te conteste algunas de las preguntas que me hiciste al final del código. 
        Lee los comentarios que te dejé línea a línea así vamos trabajando sobre ello.
        Para esta entrega podríamos haber solucionado varios problemas con algunos bucles while y es método isdigit() aplicado al input... pensalo y probá. 
        Siempre probá tu código como si fueras el peor usuario de todos, así ves que posibles errores podemos tener! 

        Muy buen trabajo! te dejo el enlace al código con los comentarios. ¡Saludos!! 
        
        
        '''
        
   