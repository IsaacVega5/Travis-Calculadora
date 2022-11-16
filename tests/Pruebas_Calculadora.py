import unittest
from Calculadora.app import sumar, dividir, restar, multiplicar

class Pruebas_Calculadora(unittest.TestCase):
    def prueba_sumar(self):
        result = sumar(2,3)
        self.assertEqual(result, 5, "El resultado debería ser 5")

    def prueba_restar(self):
        result = restar(5,4)
        self.assertEqual(result, 1, "El resultado debería ser 1")

    def prueba_multiplicar(self):
        result = multiplicar(3,4)
        self.assertEqual(result, 12, "El resultado debería ser 12")

    def prueba_dividir(self):
        result = dividir(12,3)
        self.assertEqual(result, 4, "El resultado debería ser 4")


if __name__ == "__main__":
    unittest.main()
