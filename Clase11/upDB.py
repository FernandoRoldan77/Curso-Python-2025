productos = [
    ("Pluto", "Perro", 900, 1000),
    ("Pelota mordedora", "Perro", 750, 500),
    ("Comedero grande", "Perro", 1200, 300),
    ("Correa reforzada", "Perro", 1500, 200),
    ("Cucha acolchada", "Perro", 3500, 80),
    ("Hueso de goma", "Perro", 500, 600),
    ("Shampoo canino", "Perro", 1100, 250),
    ("Arnés ajustable", "Perro", 2000, 150),
    ("Galletas dentales", "Perro", 850, 900),
    ("Collar luminoso", "Perro", 1700, 120),

    ("Rascador", "Gato", 2500, 70),
    ("Comedero doble", "Gato", 1100, 180),
    ("Pelota con plumas", "Gato", 600, 400),
    ("Cama cueva", "Gato", 3200, 60),
    ("Piedras sanitarias", "Gato", 800, 300),
    ("Cepillo de autolimpieza", "Gato", 1400, 90),
    ("Juguete láser", "Gato", 950, 150),
    ("Collar con cascabel", "Gato", 300, 500),
    ("Puerta para gato", "Gato", 1800, 40),
    ("Snacks de salmón", "Gato", 700, 220),

    ("Jaula mediana", "Ave", 2700, 35),
    ("Bañera de aves", "Ave", 900, 100),
    ("Alpiste premium", "Ave", 400, 250),
    ("Perchas naturales", "Ave", 600, 150),
    ("Nido artificial", "Ave", 1300, 80),

    ("Rueda metálica", "Roedor", 800, 90),
    ("Cama de algodón", "Roedor", 700, 110),
    ("Pellets nutricionales", "Roedor", 500, 200),

    ("Pecera de 20L", "Peces", 3500, 20),
    ("Filtro externo", "Peces", 2900, 30),
    ("Comida en escamas", "Peces", 450, 250),
    ("Decoración de castillo", "Peces", 1100, 40)
]
import sqlite3

with sqlite3.connect("Clase11/inventario.db") as conn:
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO productos (nombre, categoria, precio, stock)
        VALUES (?, ?, ?, ?)
    ''', productos)