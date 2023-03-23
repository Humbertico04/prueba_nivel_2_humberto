import unittest
import database as db

class Test_database(unittest.TestCase):
    def set_up(self):
        self.a = db.Punto(2, 3)
        self.b = db.Punto(5, 5)
        self.c = db.Punto(-3, -1)
        self.d = db.Punto(0, 0)
