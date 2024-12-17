# modelos/usuarios.py
class Usuario:
    def __init__(self, id, nombre, username, email, direccion, telefono, website, compania):
        self.id = id
        self.nombre = nombre
        self.username = username
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.website = website
        self.compania = compania

    def __str__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', username='{self.username}', email='{self.email}')"

class Tarea:
    def __init__(self, id, user_id, titulo, completada):
        self.id = id
        self.user_id = user_id
        self.titulo = titulo
        self.completada = completada

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea(id={self.id}, user_id={self.user_id}, titulo='{self.titulo}', estado='{estado}')"
