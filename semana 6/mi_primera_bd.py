import sqlite3

conn =sqlite3.connect("instituto.db")#crea coneccion a la base de datos
#CREACION DE LA TABLA CARRERA
conn.execute(#USAR LAS PALABRAS CLAVES en mayusculas create table, integer, text, integer <= definimos el tipo de datos
    """
    CREATE TABLE CARRERAS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL);
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS(nombre, duracion)
    VALUES('Ingenieria en Informatica',5)
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS(nombre, duracion)
    VALUES ('Licenciatura en Administracion', 4)
    """
)

#Consulta de datos
print("CARRERAS:")
cursor= conn.execute("SELECT * FROM CARRERAS")#SELECCIONA todo de CARRERAS
for row in cursor:
    print(row)

#CREACION DE LA TABLA ESTUDIANTES
conn.execute(#se crea la tabla ESTUDIANTES
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL);
    """
)

conn.execute(
    """
    INSERT INTO ESTUDIANTES(nombre, apellido, fecha_nacimiento)
    VALUES('Juan', 'Perez', '2000-05-15')
    """
)#para insertar una fecha AAAA-MM-DD
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('María', 'Lopez', '1999-08-20')
    """
)
print("\nEstudiantes:")
cursor= conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)

#CREACION DE LA TABLA MATRICULAS
#crear matriculas, por convencion si se jala un dato de otra tabla se escribe el nombre de la tabla en singular
conn.execute(
    """
    CREATE TABLE MATRICULA
    (id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    carrera_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
)

# Insertar datos de matricula
conn.execute(
    """
    INSERT INTO MATRICULA (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULA (estudiante_id, carrera_id, fecha) 
    VALUES (2, 2, '2024-01-20')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULA (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)

# Consultar datos de matricula
print("\nMATRICULA:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULA.fecha 
    FROM MATRICULA
    JOIN ESTUDIANTES ON MATRICULA.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULA.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)

#Listar datos de matriculacion
print("\nMatricula:")
cursor=conn.execute(
    "SELECT * FROM MATRICULA"
)

#Actualizar una fila de la tabla de matriculacion
conn.execute(
    """
    UPDATE MATRICULA
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)
for row in cursor:
    print(row)

# Eliminar una fila de la tabla de matricula
conn.execute(
    """
    DELETE FROM MATRICULA
    WHERE id = 3
    """
)

# Listar datos de matriculación
print("\nMATRICULA:")
cursor = conn.execute(
    "SELECT * FROM MATRICULA"
)

for row in cursor:
    print(row)

#Cerrar conexión
conn.close()