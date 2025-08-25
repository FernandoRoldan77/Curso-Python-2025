import sqlite3

def crearDatabase(ruta):
    '''
    Documentación
    '''
    with sqlite3.connect(ruta) as conn:
        cursor = conn.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS productos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       categoria TEXT NOT NULL,
                       precio REAL DEFAULT 0,
                       stock INTEGER NOT NULL)''')

def cargarALaDB(ruta:str,productos:tuple[str,str,float,int]) -> None:
    with sqlite3.connect(ruta) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, categoria, precio, stock)
            VALUES (?, ?, ?, ?)
        ''', productos)

def tomarTodosLosProductos(ruta:str) -> list[tuple]:
    with sqlite3.connect(ruta) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM productos''')
        productos = cursor.fetchall()
        # [(32, 'Decoración de castillo', 'Peces', 1100.0, 40), (33, 'Pan', 'panadería', 1200.0, 200)]
    return productos

def consultaStock(ruta:str,stock:int) -> list[tuple] | None:
    '''
    Descripción

    return 
    - list[tuple] Si encuentra valores
    - None si no encuentra nada
    '''
    ## mayor, menor o igual => a completar.
    with sqlite3.connect(ruta) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM productos WHERE stock < ?''', (stock,))
        productos = cursor.fetchall()
    return productos

def buscarPorNombre(ruta:str, nombre:str) -> tuple | None:
    with sqlite3.connect(ruta) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM productos WHERE nombre LIKE ?''', (f"%{nombre}%",))
        productos = cursor.fetchall()
    return productos






