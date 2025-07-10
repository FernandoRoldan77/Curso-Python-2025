import sqlite3

#CREO BASE DE DATOS INVENTARIO CON SU TABLA
pathConexion = "ProyectoFinal/inventario.db"
conexion = sqlite3.connect(pathConexion)## Para parametrizar la direccion donde crear la bdd
cursor   = conexion.cursor()
                 
     
'''Proposito: Crea la base de datos y la tabla productos si no existe'''
def crearBaseDatosYTabla():
    try:
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre      TEXT UNIQUE NOT NULL,       
                descripcion TEXT NOT NULL,
                cantidad    INTEGER NOT NULL,
                precio      REAL NOT NULL,
                categoria   TEXT NOT NULL
            );
        ''')
        conexion.commit()
        print("Base de datos creada correctamente")
        
    except Exception as e:
        print("Error al crear base de datos y sus tablas:", e)
          
        
'''Proposito: Inserta un nuevo producto a la base de datos, los parametros reciben los siguientes tipos:
    nombre: String, 
    descripcion: String, 
    cantidad Integer, 
    precio: Float, 
    categoria: String'''
def insertarProducto(nombre, descripcion, cantidad, precio, categoria):
    try:
       with conexion as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR IGNORE INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                (nombre, descripcion, cantidad, precio, categoria)
            )
                
    except Exception as e:
        print("Error al insertar el producto:", e)

'''Proposito: Muestra todos los productos de la base de datos'''
def mostrarProductos():
    try:
        with conexion as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos ORDER BY id")
            productos = cursor.fetchall()

            if productos:
                print("Lista de productos:")
                for producto in productos:
                    print(producto)
            else:
                print("No hay productos en la base de datos.")

    except Exception as e:
        print("Error al mostrar productos:", e)


'''Proposito: Muestra un producto específico por su ID, 
   el parametro recibe el tipo:
   idProductoBuscado: Int'''
def buscarProductoPorID(idProductoBuscado):
    try:
        with conexion as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE id = ?", (idProductoBuscado,))
            producto = cursor.fetchone()

            if producto:
                print("Producto encontrado:")
                print(producto)
            else:
                print(f"No se encontró un producto con ID {idProductoBuscado}.")

    except Exception as e:
        print("Error al buscar el producto:", e)
    
'''Proposito: Actualizar un dato del producto, donde los parametros reciben el tipo:
    idParaActualizar: Int,
    dato: Integer, Float, String segun lo que se quiere actualizar
    nuevoDato: Integer, Float, String segun lo que se quiere actualizar'''
def actualizarDatoDelProducto(idParaActualizar, dato, nuevoDato):
    try:
        datosValidos = {"nombre", "descripcion", "cantidad", "precio", "categoria"}
        if dato not in datosValidos:
            raise ValueError(f"dato incorrecto: {dato}")

        with conexion as conn:
            cursor = conn.cursor()
            consulta = f"UPDATE productos SET {dato} = ? WHERE id = ?"
            cursor.execute(consulta, (nuevoDato, idParaActualizar,))
            print(f"dato '{dato}' actualizado correctamente.")
            
    except Exception as e:
        print("Error al actualizar el dato:", e)
        
        

'''Proposito: Borra un producto por ID de la base de datos, donde el parametro
idConProductoABorrar recibe un tipo Int'''
def borrarProducto(idConProductoABorrar) :
    try:
        with conexion as conn:
            cursor = conn.cursor() 
            cursor.execute("DELETE FROM productos WHERE id = ?", (idConProductoABorrar,))
            print(f"Producto con ID {idConProductoABorrar} borrado correctamente.")
    except Exception as e:
        print("Error al borrar el producto:", e)

'''Proposito: Muestra productos con cantidad menor o igual al límite dado
donde el parametro limiteEspecifico recibe un tipo Int'''
def reporteDeProductos(limiteEspecifico,):
    try:
        with conexion as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limiteEspecifico,))
            productos = cursor.fetchall()

            if productos:
                print(f" Cantidad igual o inferior a {limiteEspecifico}:")
                for producto in productos:
                    print(producto)
            else:
                print(f"No hay productos con cantidad menor o igual a {limiteEspecifico}.")
    except Exception as e:
        print(" Error al generar el reporte:", e)    
    
    



