import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

    def punto_en_circulo(self, punto):
        distancia = self.centro.calcular_distancia(punto)
        return distancia <= self.radio

mitad_circulo = Punto(2, 2)
radio = 4

circulo = Circulo(mitad_circulo, radio)

print("Área: ", circulo.calcular_area())
print("Perímetro: ", circulo.calcular_perimetro())

punto = Punto(2, 3)
print("El punto (",punto.x,",", punto.y, ") pertenece al círculo: ", circulo.punto_en_circulo(punto))
