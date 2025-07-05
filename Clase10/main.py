# por que una base de datos (BD) ? Por persistencia
# productos = [["nombre", "categoria", "precio"],
#              ["nombre", "categoria", "precio"],
#              ["nombre","categoria","precio"]]

# SQL => Conjunto de Tablas :D Filas y columnas = registros y campos.
'''
Podemos pensarlo como un excel, donde el cuaderno de excel sería la base de datos
y las hojas serían las tablas.
'''
# sqlite3 => Librería externa! python -m pip install salite3
# Colab => !pip install sqlite3 (ya está instaladao en colab)


# import sqlite3

# # connection
# conn = sqlite3.connect("Clase10/productos.db")
# conn.close()


import sqlite3

'''
PUNTEO PARA HACER UN BUEN USO DE LA BD

# 1. generar la conexión
# 2. genero el cursor
# 3. genero la consulta SQL
# 4. Confirmo los cambios
# 5. Cierro conexión.

'''
# conn = sqlite3.connect("Clase10/productos.db") # DadoBueno
# cursor = conn.cursor() ## intermediario!
# cursor.execute("Consulta SQL")
# conn.commit()
# conn.close()

# SENTENCIA - QUERY - SENTENCIA = CREATE (vamos a crear una tabla)
'''
CREATE TABLE productos
    (nombreColumna caracteristicas))
caracteristicas = tipo de dato, restricciones

tipos de datos = INTEGER, TEXT, REAL
restricciones = UNIQUE (si queremos que el valor en esa columna sea único)
                NOT NULL
                PRIMARY KEY
                DEAFULT
                CHECK(condicion)
                AUTOINCREMENT
'''

# REPRESENTO LA TABLA PRUDUCOTS => productos = [["nombre", "categoria", "precio"]]
# conn = sqlite3.connect("Clase10/productos.db")  # DadoBueno
# cursor = conn.cursor()  # intermediario!
# cursor.execute('''CREATE TABLE productos
#                (nombre TEXT NOT NULL,
#                categoria TEXT NOT NULL,
#                precio INTEGER DEFAULT 0) ''')
# conn.commit()
# conn.close()
'''
Una buena práctica sería crear la tabla unicamente si no existe para
evitarnos errores. Eso lo hacemos escribiendo la query de la siguiente manera: 
CREATE TABLE IF NOT EXISTS clientes ... Solo para tablas!

En SQLite no existe una instrucción como CREATE DATABASE IF NOT EXISTS (como mencioné 😢😇 perdonenme :D )
porque SQLite no maneja múltiples bases de datos como otros sistemas (como por ejemplo, MySQL o PostgreSQL)
En SQLite, la base de datos es simplemente un archivo (.db o .sqlite)
'''
# conn = sqlite3.connect("Clase10/productos.db")  # DadoBueno
# cursor = conn.cursor()  # intermediario!
# cursor.execute('''CREATE TABLE clientes
#                (nombre TEXT NOT NULL,
#                categoria TEXT NOT NULL,
#                id INTEGER PRIMARY KEY) ''')
# conn.commit()
# conn.close()

'''
Reemplazo los 5 pasos por la apertura del documento con with.
Nos evitamos errores y nos aseguramos el cierre.
'''
# db = "Clase10/productos.db" ## Esto es bueno tenerlo como variable al principio del código o en otro lado! 
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     cursor.execute(''' CREATE TABLE tomate
#                 (nombre TEXT NOT NULL,
#                 categoria TEXT NOT NULL,
#                 id INTEGER PRIMARY KEY AUTOINCREMENT) ''')

'''

query INSERT, SELECT, UPDATE, DELETE 

'''

# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     cursor.execute(''' CREATE TABLE clientes
#                 (nombre TEXT NOT NULL,
#                 categoria TEXT NOT NULL,
#                 id INTEGER PRIMARY KEY AUTOINCREMENT) ''')
'''
INSERT INTO nombreTable (column1,column2) VALUES (?,?)

Siempre esperamos que si queremos agregar n columnas, el 
values tenga n parámetros. Ni mas ni menos :D 
'''
# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     cursor.execute('''INSERT INTO clientes (nombre,categoria) 
#                    VALUES (?,?)''',
#                    ("Pablo","periodista",))

# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     cursor.execute('''INSERT INTO clientes (nombre,categoria) 
#                    VALUES (?,?)''',
#                    ("Lebron","jugador",))

# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes
#                 (nombre TEXT NOT NULL,
#                 categoria TEXT NOT NULL,
#                 id INTEGER PRIMARY KEY AUTOINCREMENT) ''')


'''
SELECT => Vamos a seleccionar registros de la base de datos! 
Tenemos dos formas: Fetchall() y fetchone()
Fetchall => Devuelve todos como una lista de tuplas, donde cada tupla es un registro (línea)
fetchone => Devuelve de a uno como un tupla! 

parecido a la clase pasada, en este caso:
el readlines sería fetchall;
el readline sería fetchone
'''
# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     cursor.execute(''' SELECT nombre FROM clientes
#                    ''')
#     # print(cursor.fetchall()) # [('lionel',), ('Lebron',), ('Pablo',), ('Pablo',), ('Marcos',)]
#     lineas = cursor.fetchall()
#     for linea in lineas:
#         print(linea[0])


### SELECT
# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     cursor.execute(''' SELECT nombre FROM clientes
#                    ''')
#     for i in range(3):
#         print(cursor.fetchone()) ## Igual que readline => GENERADOR


### SELECT
# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor()  # intermediario!
#     # cursor.execute(''' SELECT nombre,id FROM clientes''')
#     cursor.execute('''SELECT * FROM clientes''')
#     lineas = cursor.fetchall()
#     print(lineas)  [('lionel', 'jugador', 1), ('Lebron', 'jugador', 2), ('Pablo', 'jugador', 3), ('Pablo', 'Maestro', 4), ('Marcos', 'Maestro', 5)]
#     for linea in lineas:
#         print(linea[0]) ## Solo imprimo el nombre

'''
Con el delete tenemos que prestar atención a lo siguiente: 

import sqlite3
db = "Clase10/productos.db"
with sqlite3.connect(db) as conn:
    cursor = conn.cursor()
    ###Esta query borra TODOS los registros de la tabla clientes###
    cursor.execute("DELETE FROM clientes")
    print("Todos los registros de la tabla 'clientes' fueron eliminados.")

#Para evitar ese error (muy malo) usamos la sentencia WHERE
'''
# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor() 
'''En este caso eliminamos al cliente que tiene id 2'''
#     cursor.execute('''DELETE FROM clientes WHERE id=?''',("2"))


'''
UPDATE! 
EL update nos permite actualizarl .
La traducción de esta sentencia sería así: 
"Actualizá la tabla clientes cambiando el valor de la columna categoria a "jugador" 
solo para el/los registro donde el nombre sea "Marcos"."
'''
# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor() 
#     cursor.execute('''UPDATE clientes SET categoria=? WHERE nombre=?''',
#                    ("jugador","Marcos",))

'''
"Actualizá la tabla clientes cambiando el valor de la columna nombre a "Gustavo" 
solo para el/los registro donde la categoría sea "jugador" " -> actualizamos 2 registros en mi caso
'''
# db = "Clase10/productos.db"
# with sqlite3.connect(db) as conn:
#     cursor = conn.cursor() 
#     cursor.execute('''UPDATE clientes SET nombre=? WHERE categoria=?''',
#                    ("Gustavo","jugador",))

## Eliminar una tabla de la base de datos
db = "Clase10/productos.db"
with sqlite3.connect(db) as conn:
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS productos''')
