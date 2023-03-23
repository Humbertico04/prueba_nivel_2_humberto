import database as db
import helpers

a = db.Punto(2, 3)
b = db.Punto(5, 5)
c = db.Punto(-3, -1)
d = db.Punto(0, 0)

helpers.limpiar_pantalla()
print(a.cuadrante())
print(c.cuadrante())
print(d.cuadrante())

print("\n")

print(a.vector(b))
print(b.vector(a))

print("\n")

print(a.distancia(b))
print(b.distancia(a))

print("\n")

print(a.distancia(db.Punto()))
print(b.distancia(db.Punto()))
print(c.distancia(db.Punto()))

print("\n")

rect = db.Rectangulo(a, b)
print(f"La base del rectangulo = {rect.base()}")
print(f"La altura del rectangulo = {rect.altura()}")
print(f"El area del rectangulo = {rect.area()}")
