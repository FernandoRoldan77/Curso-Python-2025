from crud import menu, productosUsuario, mostrarProductos, generarStock
from midatabase import crearDatabase, cargarALaDB, tomarTodosLosProductos, consultaStock,buscarPorNombre


listaDeOpciones = ["Agregar producto","Mostrar productos",
                   "Buscar producto","Eliminar productos",
                   "Actualizar producto","Generar stock","Salir"]

rutaAlaDB = "Clase11/inventario.db"
# rutaReporte = "Clase11/reportes/reporte.txt" # Esot me va a tirar error
rutaReporte = "Clase11/reporte.txt"

while True:
    print("Bienvenido a mi crud")
    menu(listaDeOpciones)
    opcion = input("Ingresá una opcion (1-6): ").strip()
    crearDatabase(rutaAlaDB)
    # print(list(range(1,len(listaDeOpciones)+1))) ## valido
    if opcion.isdigit() and int(opcion) in list(range(1,len(listaDeOpciones)+1)):
        if opcion == "1":
            ## Agregar productos
            productos = productosUsuario()
            cargarALaDB(rutaAlaDB,productos)
        elif opcion == "2":
            ## Mostrar productos
            productosTotales = tomarTodosLosProductos(rutaAlaDB)
            mostrarProductos(productosTotales)
        elif opcion == "3":
            ## Buscar producto
            opciones = ["nombre", "categoria","precio"]
            menu(opciones)
            opcion = input(f"Ingresá una opcion (1-{len(opciones)}): ").strip()
            match opcion:
                case "1":
                    nombre = input("Ingrese el nombre del producto: ").strip()
                    productos = buscarPorNombre(rutaAlaDB,nombre)
                    mostrarProductos(productos)
        elif opcion == "4":
            ## eliminar producto
            print("eliminar producto")
        elif opcion == "5":
            ## actualizar producto
            print("actualizar producto")
        elif opcion == "6":
            ## Generar stock
            stock = input("Ingresá tu consulta del stock (entero): ").strip()
            if opcion.isdigit():
                productos = consultaStock(rutaAlaDB,stock)
                if productos:
                    # mostrarProductos(productos) # Muestra por terminal
                    generarStock(rutaReporte,productos) # genera un reporte en la ruta
            else:
                print("número de stock inválido! ")
            break
        elif opcion == "7":
            break
    else:
        print("opcion incorrecta")
        continue

