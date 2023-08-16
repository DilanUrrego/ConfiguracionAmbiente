import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2

    def perimetro(self):
        ancho = self.vertice2.x - self.vertice1.x
        alto = self.vertice2.y - self.vertice1.y
        return 2 * (ancho + alto)
    
    def area(self):
        ancho = self.vertice2.x - self.vertice1.x
        alto = self.vertice2.y - self.vertice1.y
        return ancho * alto
    
    def cuadrado(self):
        ancho = self.vertice2.x - self.vertice1.x
        alto = self.vertice2.y - self.vertice1.y
        if ancho == alto:
            print("Es cuadrado")
        else:
            print("No es cuadrado")
    
esquina = Punto(0,0)
otra_esquina = Punto(5,10)
rectangulo=Rectangulo(esquina, otra_esquina)
print(rectangulo.perimetro())
print(rectangulo.area())
print(rectangulo.cuadrado())