import unittest
import database as db

class Test_database(unittest.TestCase):
    def set_up(self):
        self.a = db.Punto(2, 3)
        self.b = db.Punto(5, 5)
        self.c = db.Punto(-3, -1)
        self.d = db.Punto(0, 0)

    def test_cuadrante(self):
        self.assertequal(self.a.cuadrante(), "El punto (2, 3) está situado en el primer cuadrante")
        self.assertequal(self.b.cuadrante(), "El punto (5, 5) está situado en el primer cuadrante")
        self.assertequal(self.c.cuadrante(), "El punto (-3, -1) está situado en el tercer cuadrante")
        self.assertequal(self.d.cuadrante(), "El punto (0, 0) está situado sobre el origen")

    def test_vector(self):
        self.assertequal(self.a.vector(self.b), "El vector que va de (2, 3) --> (5, 5) = (3, 2)")
        self.assertequal(self.b.vector(self.a), "El vector que va de (5, 5) --> (2, 3) = (-3, -2)")
        