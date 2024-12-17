import requests
from auxiliares.constantes import SERPER_API_KEY

def buscar_google(consulta):
    """
    Realiza una búsqueda en Google utilizando la API de Serper.
    
    Parámetros:
    - consulta: String con los términos de búsqueda.
    
    Retorna:
    - JSON con los resultados de la búsqueda.
    """
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,  # Clave API en el encabezado correcto
        "Content-Type": "application/json"
    }
    payload = {"q": consulta}

    try:
        respuesta = requests.post(url, headers=headers, json=payload)
        if respuesta.status_code == 200:
            data = respuesta.json()
            if "organic" in data and len(data["organic"]) > 0:
                return data
            else:
                print("La búsqueda no devolvió resultados.")
                return {}
        elif respuesta.status_code == 403:
            print("Error 403: Clave API inválida o acceso denegado.")
        else:
            print(f"Error {respuesta.status_code}: {respuesta.text}")
        return {}
    except requests.RequestException as e:
        print(f"Error al conectar con la API Serper: {e}")
        return {}
