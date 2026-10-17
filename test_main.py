import unittest
from main import saludar, sumar

class TestMain(unittest.TestCase):
    def test_saludar_default(self):
        self.assertEqual(saludar(), "Hola, Mundo!")

    def test_saludar_nombre(self):
        self.assertEqual(saludar("Ana"), "Hola, Ana!")

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()