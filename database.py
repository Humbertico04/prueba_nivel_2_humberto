import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x>0 and self.y>0:
            return f"El punto ({self.x}, {self.y}) está situado en el primer cuadrante"
        elif self.x>0 and self.y<0:
            return f"El punto ({self.x}, {self.y}) está situado en el cuarto cuadrante"
        elif self.x<0 and self.y<0:
            return f"El punto ({self.x}, {self.y}) está situado en el tercer cuadrante"
        elif self.x<0 and self.y>0:
            return f"El punto ({self.x}, {self.y}) está situado en el segundo cuadrante"
        elif self.x==0 and self.y!=0:
            return f"El punto ({self.x}, {self.y}) está situado sobre el eje y"
        elif self.x!=0 and self.y==0:
            return f"El punto ({self.x}, {self.y}) está situado sobre el eje x"
        else:
            return f"El punto ({self.x}, {self.y}) está situado sobre el origen"
        
    def vector(self, x=0, y=0):
        punto2 = Punto(x, y)
        vectorx = punto2.x - self.x
        vectory = punto2.y - self.y
        return f"El vector que va de ({self.x}, {self.y}) --> {punto2} = {Punto(vectorx, vectory)}"
    
    def distancia(self, x=0, y=0):
        punto2 = Punto(x, y)
        distancia = math.sqrt((punto2.x - self.x)**2 + (punto2.y - self.y)**2)
        return f"La distancia que hay de ({self.x}, {self.y}) --> {punto2} = {distancia}"
    
class Rectangulo:
    def __init__(self, Punto1=Punto(), Punto2=Punto()):
        self.Punto1 = Punto1
        self.Punto2 = Punto2
    def base(self):
        return f"La base = {abs(self.Punto1.x - self.Punto2.x)}"

    
punto = Punto(1, 1)
punto2= Punto(3, 5)
print(punto.cuadrante())
print(punto.vector(3, 5))
print(punto.distancia(2, 2))

rect = Rectangulo(punto, punto2)
print(rect.base())

