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
        
    def vector(self, punto2):
        vectorx = punto2.x - self.x
        vectory = punto2.y - self.y
        return f"El vector que va de ({self.x}, {self.y}) --> {punto2} = {Punto(vectorx, vectory)}"
    
    def distancia(self, punto2):
        distancia = math.sqrt((punto2.x - self.x)**2 + (punto2.y - self.y)**2)
        return f"La distancia que hay de ({self.x}, {self.y}) --> {punto2} = {distancia}"
    
class Rectangulo:
    def __init__(self, Punto1=Punto(), Punto2=Punto()):
        self.Punto1 = Punto1
        self.Punto2 = Punto2

    def base(self):
        return abs(self.Punto1.x - self.Punto2.x)
    
    def altura(self):
        return abs(self.Punto1.y - self.Punto2.y)
    
    def area(self):
        area = self.base() * self.altura()
        return area

# punto = Punto(1, 1)
# punto2= Punto(3, 5)
# print(punto.cuadrante())
# print(punto.vector(punto2))
# print(punto.distancia(punto2))

# rect = Rectangulo(punto, punto2)
# print(rect.base())
# print(rect.altura())
# print(rect.area())
