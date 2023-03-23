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
    
    
punto = Punto()
print(punto.cuadrante())
