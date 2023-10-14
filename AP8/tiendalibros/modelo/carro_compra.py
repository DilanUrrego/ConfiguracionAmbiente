class CarroCompras:
    # Defina metodo inicializador __init__(self)
    def __init__(self):
        self.items: list[itemCompra] = []

    # Defina el metodo agregar_item
    def agregar_item(self, libro, cantidad):
        item = ItemCompra(libro, cantidad)
        self.items.append(item)
        return item
    
    # Defina el metodo calcular_total
    def calcular_total(self):
        return sum([item.calcular_subtotal() for item in self.items])
    
    # Defina el metodo quitar_item
    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]