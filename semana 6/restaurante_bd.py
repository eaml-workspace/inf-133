import sqlite3

conn =sqlite3.connect("restaurante.db")#crea coneccion a la base de datos
try:
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        categoria TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("El plato no existe")
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
try:
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La mesa no existe")

conn.execute(
    """
    INSERT INTO MESAS(numero)
    VALUES(20)
    """
)
conn.execute(
    """
    INSERT INTO MESAS(numero)
    VALUES(15)
    """
)
print("MESAS:")
cursor= conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)
################################
try:
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha TEXT NOT NULL
        FOREIGN KEY (plato_id) REFERENCES PLATOS(id)
        FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
        """
    )
except sqlite3.OperationalError:
    print("La mesa no existe")

conn.execute(
    """
    INSERT INTO PEDIDOS(plato_id,mesa_id,cantidad,fecha)
    VALUES(1,1,2,'2024-04-03')
    """
)
print("MESAS:")
cursor= conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)