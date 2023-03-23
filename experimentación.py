# • (Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
# • (Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más
# lejos del origen, punto (0,0).
# • Crea un rectángulo utilizando los puntos A y B.
# • Consulta la base, altura y área del rectángulo.

import database as db

a = db.Punto(2, 3)
b = db.Punto(5, 5)
c = db.Punto(-3, -1)
d = db.Punto(0, 0)

print(a.cuadrante())
print(c.cuadrante())
print(d.cuadrante())

print(a.vector(b))
print(b.vector(a))

