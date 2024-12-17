import requests
from auxiliares.constantes import BASE_URL

def obtener_datos(endpoint):
    """
    Realiza una solicitud HTTP GET a la API jsonplaceholder para obtener datos.

    Parámetros:
    - endpoint: String que especifica el endpoint de la API (por ejemplo, 'posts', 'comments').

    Retorna:
    - JSON con los datos obtenidos.
    """
    url = f"{BASE_URL}/{endpoint}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si ocurre un error HTTP
        return respuesta.json()
    except requests.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return []

def enviar_datos(endpoint, data):
    """
    Realiza una solicitud HTTP POST a la API jsonplaceholder para enviar datos.

    Parámetros:
    - endpoint: String que especifica el endpoint de la API (por ejemplo, 'posts').
    - data: Diccionario con los datos a enviar.

    Retorna:
    - Objeto Response de la solicitud HTTP.
    """
    url = f"{BASE_URL}/{endpoint}"
    try:
        respuesta = requests.post(url, json=data)
        respuesta.raise_for_status()  # Lanza una excepción si ocurre un error HTTP
        return respuesta
    except requests.RequestException as e:
        print(f"Error al enviar datos a la API: {e}")
        return None
