class Calculadora():
    """
    Clase calculadora con los métodos de cálculo de numeros reales
    :return: numero real resultado del cálculo
    """

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Dividir un numero entre 0 no tiene un resultado bien definido"
        else:
            return a / b

    def raiz(self, a):
        """
       Interpretación propia Basada en Algoritmo babilónico: Va buscando mediante sucesiones la base X altura
       más próxima al cuadrado perfecto del área cuyo número queremos hacer la raíz cuadrada, es decir es un
       algoritmo para aproximarse a la raíz cuadrada del número a calcular, en nuestro caso vamos a parar cuando
       los dos números que se van aproximando tengan los 5 primeros dígitos decimales iguales
        :param a: valor a calcular
        :return: raíz del numero
        """
        if a < 0:  # Control de números negativos
            return "No es un número positivo"
        elif a == 0:  # control de 0
            return 0
        seguimos = True
        x1 = a  # empezamos con a como primer elemento de la sucesión o 'base'
        while seguimos:  # Mientras no logremos la precisión objetivo
            x2 = 0.5 * (x1 + (a / x1))  # fórmula del algoritmo babilónico, calcula la 'Altura'
            if float(f"{x1:.5f}") == float(f"{x2:.5f}"):  # Comprobación que marca la precisión a lograr
                seguimos = False  # Hemos logrado el objetivo, salimos
            x1 = x2  # Si no objetivo, seguimos con la sucesión
        if float(f"{x1:.1f}") == float(f"{x1:.0}"):  # si la parte fraccionaria, es 0, es decir es un entero
            x1 = int(x1)  # como realiza cualquier calculadora, devolvemos un entero
        else:
            x1 = float(f"{x1:.5f}")  # si no devolvemos un número real con precisión de 5
        return x1
