from negocio.encriptacion import encriptar
from servicios.api_jsonplaceholder import obtener_datos, enviar_datos
from servicios.api_serper import buscar_google
from datos.crud import crear_tabla, insertar_datos, obtener_todos, verificar_existencia_tabla
from negocio.procesamiento import procesar_publicaciones

def inicializar_base_datos():
    """
    Inicializa la base de datos creando las tablas necesarias si no existen.
    """
    tablas = {
        "publicaciones": """
            CREATE TABLE IF NOT EXISTS publicaciones (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                contenido TEXT NOT NULL
            )
        """
    }

    for tabla, query in tablas.items():
        if not verificar_existencia_tabla(tabla):
            crear_tabla(query)

def menu_principal():
    """
    Menú principal que ejecuta las opciones requeridas.
    """
    while True:
        print("\nMenú Principal")
        print("1. Encriptación de contraseña")
        print("2. Obtener y guardar datos desde la API (HTTP GET)")
        print("3. Enviar datos a la API (HTTP POST)")
        print("4. Realizar búsqueda con autenticación (API Serper)")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_encriptacion()
        elif opcion == "2":
            gestionar_obtencion_datos()
        elif opcion == "3":
            gestionar_envio_datos()
        elif opcion == "4":
            gestionar_busqueda_serper()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def gestionar_encriptacion():
    """
    Solicita una contraseña, la encripta y la compara con el original.
    """
    texto = input("Ingrese la contraseña: ")
    texto_encriptado = encriptar(texto)
    print(f"Contraseña ingresada: {texto}")
    print(f"Contraseña encriptada: {texto_encriptado}")

    texto_comparar = input("Ingrese nuevamente la contraseña para comparar: ")
    if encriptar(texto_comparar) == texto_encriptado:
        print("¡La contraseña coincide!")
    else:
        print("La contraseña no coincide.")

def gestionar_obtencion_datos():
    """
    Permite capturar y guardar un conjunto específico de datos desde la API.
    """
    print("\nSelecciona el tipo de datos a capturar:")
    print("1. Publicaciones (posts)")
    print("2. Comentarios (comments)")
    print("3. Álbumes (albums)")
    print("4. Fotos (photos)")
    print("5. Usuarios (users)")
    print("6. Tareas (todos)")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        capturar_publicaciones()
    elif opcion == "2":
        capturar_comentarios()
    elif opcion == "3":
        capturar_albumes()
    elif opcion == "4":
        capturar_fotos()
    elif opcion == "5":
        capturar_usuarios()
    elif opcion == "6":
        capturar_tareas()
    else:
        print("Opción no válida.")

def capturar_publicaciones():
    """
    Captura y guarda publicaciones (posts) en la base de datos.
    """
    print("Obteniendo datos de publicaciones...")
    datos = obtener_datos("posts")
    publicaciones = procesar_publicaciones(datos)
    for publicacion in publicaciones:
        insertar_datos("publicaciones", publicacion.__dict__)
    print("¡Datos de publicaciones guardados en la base de datos!")

    print("\nConsultando datos recién guardados:")
    registros = obtener_todos("publicaciones")
    if registros:
        for registro in registros:
            print(f"ID: {registro[0]}, Título: {registro[1]}, Contenido: {registro[2]}")
    else:
        print("No hay datos en la tabla 'publicaciones'.")

def capturar_comentarios():
    """
    Captura y guarda comentarios (comments) en la base de datos.
    """
    print("Obteniendo datos de comentarios...")
    datos = obtener_datos("comments")
    print(f"Se capturaron {len(datos)} comentarios. (Ejemplo de datos: {datos[:2]})")

def capturar_albumes():
    """
    Captura y guarda álbumes (albums) en la base de datos.
    """
    print("Obteniendo datos de álbumes...")
    datos = obtener_datos("albums")
    print(f"Se capturaron {len(datos)} álbumes. (Ejemplo de datos: {datos[:2]})")

def capturar_fotos():
    """
    Captura y guarda fotos (photos) en la base de datos.
    """
    print("Obteniendo datos de fotos...")
    datos = obtener_datos("photos")
    print(f"Se capturaron {len(datos)} fotos. (Ejemplo de datos: {datos[:2]})")

def capturar_usuarios():
    """
    Captura y guarda usuarios (users) en la base de datos.
    """
    print("Obteniendo datos de usuarios...")
    datos = obtener_datos("users")
    print(f"Se capturaron {len(datos)} usuarios. (Ejemplo de datos: {datos[:2]})")

def capturar_tareas():
    """
    Captura y guarda tareas (todos) en la base de datos.
    """
    print("Obteniendo datos de tareas...")
    datos = obtener_datos("todos")
    print(f"Se capturaron {len(datos)} tareas. (Ejemplo de datos: {datos[:2]})")

def gestionar_envio_datos():
    """
    Envía un objeto a la API utilizando POST.
    """
    print("\nCreando datos para enviar a la API...")
    titulo = input("Ingrese el título del objeto: ")
    contenido = input("Ingrese el contenido del objeto: ")
    user_id = input("Ingrese el ID de usuario: ")

    data = {"title": titulo, "body": contenido, "userId": user_id}

    print("Enviando datos a la API...")
    respuesta = enviar_datos("posts", data)
    if respuesta and respuesta.status_code == 201:
        print("¡Datos enviados correctamente! Respuesta 200:")
        print(respuesta.json())
    else:
        print(f"Error al enviar datos. Código: {respuesta.status_code}")

def gestionar_busqueda_serper():
    """
    Realiza una búsqueda en la API Serper con autenticación.
    """
    query = input("Ingrese el término de búsqueda: ")
    print("\nRealizando búsqueda en Google a través de la API Serper...")
    resultados = buscar_google(query)
    if "organic" in resultados:
        print("\nResultados de la búsqueda:")
        for idx, resultado in enumerate(resultados["organic"], 1):
            print(f"{idx}. {resultado['title']} - {resultado['link']}")
    else:
        print("No se encontraron resultados.")

if __name__ == "__main__":
    inicializar_base_datos()
    menu_principal()
