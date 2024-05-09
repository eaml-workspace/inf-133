#en espacios de consulta preguntar por que no solo se crean dos tablas :)

import sqlite3

conn = sqlite3.connect("personal.db")

try:
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("DEPARTAMENTOS no existe")

try:
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("CARGOS no existe")

try:
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
    )
except sqlite3.OperationalError:
    print("EMPLEADOS no existe")

try:
    conn.execute("""
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        salario FLOAT NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        empleado_id INTEGER NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
    """)
except sqlite3.OperationalError:
    print("SALARIOS no existe")

##### registros ##########
## departamentos
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('Ventas', '2020-04-10')
    """
)

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('Marketing', '2020-04-11')
    """
)
## cargos
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Gerente de Ventas', 'Senior','2020-04-10')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Analista de Marketing', 'Junior', '2020-04-11')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Representante de Ventas', 'Junior','2020-04-12')
    """
)
## empleados
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id)
    VALUES ('Juan', 'Gonzales', 'Pérez', '2023-05-15', 1, 1)
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id)
    VALUES ('María', 'Lopex', 'Martinex', '2023-06-20', 2, 2)
    """
)
## salarios
conn.execute(
    """
    INSERT INTO SALARIOS (salario, fecha_inicio, fecha_fin, fecha_creacion, empleado_id)
    VALUES (3000, '2023-04-01', '2025-04-30', '2023-05-15', 1)
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (salario, fecha_inicio, fecha_fin, fecha_creacion, empleado_id)
    VALUES (3500, '2023-07-01', '2025-04-30', '2023-06-20', 2)
    """
)
### consultas
print("\n Empleados y salarios")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario
    FROM SALARIOS
    JOIN EMPLEADOS ON SALARIOS.empleado_id = EMPLEADOS.id
    """
)
for row in cursor:
    print(row)

print("\nEmpleado, departamento, cargo")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    """
)
for row in cursor:
    print(row)

print("\nEmpleado, departamento, cargo, salario")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    """
)
for row in cursor:
    print(row)

## update

conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)

conn.execute(
    """
    UPDATE EMPLEADOS
    SET EMPLEADOS.cargo_id=3
    WHERE id = 2
    """
)

#### delete
conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)
conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)
## otra vez crear
conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id)
    VALUES ('Carlos', 'Sanchéz', 'Rodríguez', '2024-04-09', 2, 3)
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (salario, fecha_inicio, fecha_fin, fecha_creacion, empleado_id)
    VALUES (3500, '2024-04-09', '2025-04-30', '2023-06-20', 2)
    """
)


conn.commit()
conn.close()