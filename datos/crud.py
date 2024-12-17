from datos.conexion_db import obtener_conexion

def crear_tabla(query):
    """
    Crea una tabla en la base de datos usando el query proporcionado.
    """
    conexion = obtener_conexion()
    with conexion:
        conexion.execute(query)
    print(f"Tabla creada con éxito.")
    
def verificar_existencia_tabla(tabla):
    """
    Verifica si una tabla existe en la base de datos.

    Parámetros:
    - tabla: Nombre de la tabla a verificar.

    Retorna:
    - True si la tabla existe, False en caso contrario.
    """
    conexion = obtener_conexion()
    try:
        with conexion:
            cursor = conexion.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (tabla,)
            )
            resultado = cursor.fetchone()
        return resultado is not None
    except Exception as e:
        print(f"Error al verificar la tabla: {e}")
        return False
    finally:
        conexion.close()
def insertar_datos(tabla, datos):
    """
    Inserta un registro en la tabla especificada.
    
    Parámetros:
    - tabla: Nombre de la tabla donde insertar los datos.
    - datos: Diccionario con los datos a insertar. Las claves deben coincidir con las columnas de la tabla.
    """
    conexion = obtener_conexion()
    columnas = ", ".join(datos.keys())
    placeholders = ", ".join(["?"] * len(datos))
    valores = tuple(datos.values())

    with conexion:
        conexion.execute(
            f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})",
            valores
        )
    print(f"Datos insertados en la tabla '{tabla}'.")

def obtener_todos(tabla):
    """
    Devuelve todos los registros de una tabla.
    """
    conexion = obtener_conexion()
    with conexion:
        cursor = conexion.execute(f"SELECT * FROM {tabla}")
        resultados = cursor.fetchall()
    return resultados

def obtener_por_id(tabla, id):
    """
    Devuelve un registro por su ID.
    """
    conexion = obtener_conexion()
    with conexion:
        cursor = conexion.execute(f"SELECT * FROM {tabla} WHERE id = ?", (id,))
        resultado = cursor.fetchone()
    return resultado

def actualizar_dato(tabla, id, datos):
    """
    Actualiza un registro en la tabla por su ID.
    
    Parámetros:
    - tabla: Nombre de la tabla donde se actualizarán los datos.
    - id: ID del registro a actualizar.
    - datos: Diccionario con las columnas a actualizar y sus nuevos valores.
    """
    conexion = obtener_conexion()
    columnas = ", ".join([f"{key} = ?" for key in datos.keys()])
    valores = tuple(datos.values()) + (id,)

    with conexion:
        conexion.execute(
            f"UPDATE {tabla} SET {columnas} WHERE id = ?",
            valores
        )
    print(f"Registro con ID {id} actualizado en la tabla '{tabla}'.")

def eliminar_por_id(tabla, id):
    """
    Elimina un registro de la tabla por su ID.
    """
    conexion = obtener_conexion()
    with conexion:
        conexion.execute(f"DELETE FROM {tabla} WHERE id = ?", (id,))
    print(f"Registro con ID {id} eliminado de la tabla '{tabla}'.")
