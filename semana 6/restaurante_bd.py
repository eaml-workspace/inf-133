import sqlite3

conn =sqlite3.connect("restaurante.db")#crea coneccion a la base de datos

conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,
    categoria TEXT NOT NULL);
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria)
    VALUES('Milanesa',50,'ES una cadena?')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria)
    VALUES('Pollo',45,'AUN NO ES una cadena')
    """
)
print("PLATOS:")
cursor= conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
#####################CONTINUAR####################
