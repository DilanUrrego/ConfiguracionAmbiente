from tiendalibros.modelo.libro_error import LibroError

class LibroAgotadoError(LibroError):

    # Defina metodo inicializador
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    # Defina metodo especial
    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} esta agotado"