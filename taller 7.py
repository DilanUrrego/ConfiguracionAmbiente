from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other: object) -> bool:
        return self.nombre == other.nombre
    
class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.elementos = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(nombre=f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevo_conjunto = Conjunto(nombre=f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.elementos:
            if conjunto2.contiene(elemento):
                nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elem.nombre for elem in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"