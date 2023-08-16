import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def mostrar(self):
        print("Las coordenadas del punto son",self.x,self.y)
    def mover(self,x,y):
        self.x = x
        self.y = y
    def calcular_distancia(self, punto2):
        distancia=math.sqrt((self.x - punto2.x)**2 + (self.y - punto2.y)**2)
        print(distancia)
punto1 = Punto(4,1)    
punto2 = Punto(8,5)

punto1.mostrar()
punto2.mover(5,3)
punto2.mostrar()
punto1.calcular_distancia(punto2)