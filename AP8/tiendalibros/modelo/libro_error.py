from tiendalibros.modelo.libro import Libro

class LibroError(Exception):
    def __init__(self, libro: Libro):
        self.libro = libro

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn: {self.isbn} ya existe en el catálogo"

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        try:
            super().__init__()
        except Exception as e:
            print(f"Error al inicializar: {e}")
            raise e  # relanzar la excepción
        self.titulo = titulo
        self.isbn = isbn
