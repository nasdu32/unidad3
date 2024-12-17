# modelos/albumes.py
class Album:
    def __init__(self, id, user_id, titulo):
        self.id = id
        self.user_id = user_id
        self.titulo = titulo

    def __str__(self):
        return f"Album(id={self.id}, user_id={self.user_id}, titulo='{self.titulo}')"

class Foto:
    def __init__(self, id, album_id, titulo, url, thumbnail_url):
        self.id = id
        self.album_id = album_id
        self.titulo = titulo
        self.url = url
        self.thumbnail_url = thumbnail_url

    def __str__(self):
        return f"Foto(id={self.id}, album_id={self.album_id}, titulo='{self.titulo}', url='{self.url}')"
