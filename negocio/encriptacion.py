# negocio/encriptacion.py
from hashlib import sha256

def encriptar(texto):
    return sha256(texto.encode()).hexdigest()
