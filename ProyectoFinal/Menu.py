from ConsultasTabla import*

'''Proposito: Muestra la lista de opciones al usuario'''
def mostrarOpciones():
    opciones= ["\nSeleccione una opcion para el inventario de productos: \n",
                "1. Visualizar productos",
                "2. Actualizar productos",
                "3. Borrar productos",
                "4. Buscar productos",
                "5. Reporte de productos por cantidad",
                "6. Ingresar un nuevo producto",
                "7. Salir \n"
              ]
    for o in opciones:
        print(o)      
    
'''Proposito: Muestra el menu al usuario'''
def mostrarMenu():
    mostrarOpciones()
    
    while True:
        try:
            seleccionDeOpciones = input("Elegi una opcion del 1 al 6: ").strip()
           
            if not seleccionDeOpciones.isdigit():
                print("Seleccion invalida, ingresa un eleccion valida.")
                continue

            numeroDeOpcionSeleccionado = int(seleccionDeOpciones) #actualizo si paso el filtro de valor valido

            match numeroDeOpcionSeleccionado:
                    
                case 1:
                    print("\nEstos son los productos registrados \n")
                    mostrarProductos()
                    mostrarOpciones()
                    
    
                case 2:
                    print("Seleccione que quiere actualizar")
                    mostrarProductos()
                    idParaActualizar = input("Seleccione el id para actualizar: ").strip()
                    if not idParaActualizar.isdigit():
                        print("ID invalido.")
                        continue
                    id = int(idParaActualizar)
                    dato = input("¿Que dato quiere actualizar? ")
                    datoNuevo = input("¿Con que quiere reemplazarlo? ")
                    actualizarDatoDelProducto(id, dato, datoNuevo)

                case 3:
                    print("Seleccione que producto quiere borrar")
                    mostrarProductos()
                    idB = input("Seleccione el id a borrar: ").strip()
                    if not idB.isdigit():
                        print("ID invalido.")
                        continue
                    idABorrar = int(idB)
                    borrarProducto(idABorrar)
                    

                case 4:
                    idBuscado = input("Seleccione el id a buscar: ").strip()
                    if not idBuscado.isdigit():
                        print("ID invalido.")
                        continue
                    idABuscar = int(idBuscado)
                    buscarProductoPorID(idABuscar)

                case 5:
                    limiteDeCantidad = input("Mostrar productos con cantidad menor o igual a: ").strip()
                    if not limiteDeCantidad.isdigit():
                        print("El valor del limite es invalido.")
                        continue
                    limite = int(limiteDeCantidad)
                    reporteDeProductos(limite)
                    
                case 6:
                    print("\nIngresa los datos del nuevo producto:")
                    nombre = input("Nombre: ").strip()
                    if not nombre:
                        print("El nombre no puede estar vacio.")
                        continue
                        
                    descripcion = input("Descripcion: ").strip()
                    if not descripcion:
                        print("La descripcion no puede estar vacia.")
                        continue
                        
                    cant = input("Cantidad: ").strip()
                  
                    if not cant.isdigit():
                        print("La cantidad debe ser un numero entero positivo.")
                        continue
                        
                    cantidad = int(cant)
                    if not cant.isdigit():
                        print("Cantidad invalida.")
                        continue
                        
                    cantidad = int(cant)
                    precio = input("Precio: ").strip()
                    try:
                        precio = float(precio)
                        if precio < 0:
                            print("El precio no puede ser negativo.")
                            continue
                            
                    except ValueError:
                        print("Precio invalido.")
                        continue

                    categoria = input("Categoria: ").strip()
                    if not categoria:
                        print("La categoria no puede estar vacia.")
                        continue
                    
                    insertarProducto(nombre, descripcion, cantidad, precio, categoria)
                    mostrarProductos()
                case 7:
                    print("Saliendo del programa.")
                    break

                case _:
                    print("Opcion invalida, selecciona una opcion correcta")

        except Exception as e:
            print("Error inesperado:", e)       
            

 