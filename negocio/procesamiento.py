# negocio/procesamiento.py
from modelos.publicaciones import Publicacion
from modelos.albumes import Album, Foto
from modelos.usuarios import Usuario, Tarea

def procesar_publicaciones(datos_api):
    publicaciones = []
    for dato in datos_api:
        publicacion = Publicacion(
            id=dato["id"],
            titulo=dato["title"],
            contenido=dato["body"]
        )
        publicaciones.append(publicacion)
    return publicaciones

def procesar_albumes_y_fotos(datos_albumes, datos_fotos):
    albumes = []
    fotos = []

    for dato in datos_albumes:
        album = Album(
            id=dato["id"],
            user_id=dato["userId"],
            titulo=dato["title"]
        )
        albumes.append(album)

    for dato in datos_fotos:
        foto = Foto(
            id=dato["id"],
            album_id=dato["albumId"],
            titulo=dato["title"],
            url=dato["url"],
            thumbnail_url=dato["thumbnailUrl"]
        )
        fotos.append(foto)

    return albumes, fotos

def procesar_usuarios_y_tareas(datos_usuarios, datos_tareas):
    usuarios = []
    tareas = []

    for dato in datos_usuarios:
        usuario = Usuario(
            id=dato["id"],
            nombre=dato["name"],
            username=dato["username"],
            email=dato["email"],
            direccion=dato["address"],
            telefono=dato["phone"],
            website=dato["website"],
            compania=dato["company"]
        )
        usuarios.append(usuario)

    for dato in datos_tareas:
        tarea = Tarea(
            id=dato["id"],
            user_id=dato["userId"],
            titulo=dato["title"],
            completada=dato["completed"]
        )
        tareas.append(tarea)

    return usuarios, tareas
