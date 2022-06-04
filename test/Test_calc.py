import sys, os, unittest
from lib.Calculadora import Calculadora

# LIBRERIAS
import sys, os, unittest

#   CLASES
class TestCalc(unittest.TestCase):
    """
    Clase de test de cálculo que irá conteniendo las funciones de prueba de las operaciones
    """

    def setUp(self):
        self.calculadora = Calculadora()
        self.datos_suma = [[2, 2, 4], [-2, -2, -4], [2, -2, 0], [350.25, 100.75, 451], [200, 100.5, 300.5]]
        self.datos_resta = [[2, 2, 0], [-2, -2, 0], [2, -2, 4], [350, 100.75, 249.25], [200, 100.5, 99.5]]
        self.datos_multiplicación = [[2, 2, 4], [-2, -2, 4], [2, -2, -4], [350, 100.75, 35262.5], [200, 100.5, 0]]


    def testSuma(self):
        """
        Método de test de suma de elementos con un esperado
        :param datos: Lista con las listas de datos de prueba
        """
        # arrrange, Inicializamos los parámetros de suma y para cada caso de la lista de casos
        for dato in self.datos_suma:
            a = dato[0]
            b = dato[1]
            esperado = dato[2]
            # act,  invocamos al método suma
            resultado = self.calculadora.suma(a, b)
            # asser, validamos los resultados
            error = f'la suma de {a} + {b} debería ser {esperado}'
            self.assertEqual(resultado, esperado, error)

    def testResta(self):
        """
        Método de test de resta de elementos con un esperado
        :param datos: Lista con las listas de datos de prueba
        """
        # arrrange, Inicializamos los parámetros de resta y para cada caso de la lista de casos
        for dato in self.datos_resta:
            a = dato[0]
            b = dato[1]
            esperado = dato[2]
            # act,  invocamos al método resta
            resultado = self.calculadora.resta(a, b)
            # asser, validamos los resultados
            error = f'la resta de {a} - {b} debería ser {esperado}'
            self.assertEqual(resultado, esperado, error)

    def testMultiplicacion(self):
        """
        Método de test de multiplicación de elementos con un esperado
        :param datos: Lista con las listas de datos de prueba
        """
        # arrrange, Inicializamos los parámetros de multiplicación y para cada caso de la lista de casos
        for dato in self.datos_multiplicación:
            a = dato[0]
            b = dato[1]
            esperado = dato[2]
            # act,  invocamos al método multiplicación
            resultado = self.calculadora.multiplicacion(a, b)
            # asser, validamos los resultados
            error = f'la multiplicación de {a} * {b} debería ser {esperado}'
            self.assertEqual(resultado, esperado, error)

#   MAIN
if __name__ == '__main__':
    unittest.main()
