class TiendaLibros:
    pass
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn: str, titulo:str, precio: float, existencias: int):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        elif libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)
        self.carrito.agregar_item(libro, cantidad)

    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)