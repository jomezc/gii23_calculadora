import sys, os, unittest
from lib.Calculadora import pr

# LIBRERIAS
import sys, os, unittest


#   CLASES
class TestCalc(unittest.TestCase):
    """
    Clase de test de cálculo que irá conteniendo las funciones de prueba de las operaciones
    """

    def setUp(self):
        self.datos_suma = [[2, 2, 4], [-2, -2, -4], [2, -2, 0]]

    def testSuma(self):
        """
        Función de test de suma de elementos con un esperado
        :param datos: Lista con las listas de datos de prueba
        """
        # arrrange, Inicializamos los parámetros de suma y para cada caso de la lista de casos
        for dato in self.datos_suma:
            a = dato[0]
            b = dato[1]
            esperado = dato[2]
            # act,  invocamos al método suma
            resultado = a+b
            # asser, validamos los resultados
            self.assertEqual(resultado, esperado, f'la suma de {a} + {b} debería ser {esperado}')


#   MAIN
if __name__ == '__main__':
    unittest.main()
