from lib.Calculadora import Calculadora
from tkinter import *
import re

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("ISA-CALC")
        self.ventana.geometry("580x300")
        self.pantalla = Text(ventana, state="disabled", width=60, height=3, background="thistle4", foreground="white",
                             font=("Helvetica", 15), ) # "Pantalla de la calculadora" mediante caja de texto
        self.pantalla.insert('end', 0)
        self.pantalla.grid(row=0, column=0, columnspan=6, padx=10, pady=10)  # Ubicar la pantalla en la ventana

        # Inicializar la operación mostrada en pantalla como string vacío
        self.operacion = ""
        # Botones de la calculadora
        boton1 = self.crearBoton(7)
        boton2 = self.crearBoton(8)
        boton3 = self.crearBoton(9)
        boton4 = self.crearBoton(u"\u232B", escribir=False)
        boton5 = self.crearBoton(4)
        boton6 = self.crearBoton(5)
        boton7 = self.crearBoton(6)
        boton8 = self.crearBoton(u"\u00F7")     # división
        boton9 = self.crearBoton(1)
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton("*", 'orange')
        boton13 = self.crearBoton(".")
        boton14 = self.crearBoton(0)
        boton15 = self.crearBoton("+")
        boton16 = self.crearBoton("-")
        boton17 = self.crearBoton(u"\u221a")  # raiz
        boton18 = self.crearBoton("=", escribir=False)

        # Ubicar los botones con el gestor grid
        botones = [boton1, boton2, boton3, boton17, boton8, boton4,
                   boton5, boton6, boton7, boton13, boton15, boton16,
                   boton9, boton10, boton11, boton14, boton12, boton18]
        contador = 0
        for fila in range(1, 4):
            for columna in range(6):
                botones[contador].grid(row=fila, column=columna)
                contador += 1
        return

        # Crea un botón mostrando el valor pasado por parámetro

    def crearBoton(self, valor, background='white', escribir=True, ancho=4, alto=3, ):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 15), bg=background,
       foreground="slate grey", command=lambda: self.click(valor, escribir))

        # Controla el evento disparado al hacer click en un botón

    def click(self, texto, escribir):
        # Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
        if not escribir:
            # Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
            if texto == "=" and self.operacion != "":
                # Reemplazar el valor unicode de la división por el operador división de Python '/'
                self.operacion = re.sub(u"\u00F7", "/", self.operacion)
                self.operacion = re.sub(u"\u221a", "r", self.operacion)
                # Llamamos a la función que trata el string, crea el objeto calculadora , llama a la operación
                # y devuelve el resultado
                resultado = self.preparaCalculo(self.operacion)
                self.operacion = ""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            # Si se presionó el botón de borrado, limpiar la pantalla
            elif texto == u"\u232B":
                self.operacion = ""
                self.limpiarPantalla()
        # Mostrar texto
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(texto)
        return

        # Borra el contenido de la pantalla de la calculadora

    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return

        # Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return

    def preparaCalculo(self,linea):

        self.calculadora = Calculadora()
        if '+' in linea:
            a, b = linea.split('+', 1)
            a = float(a)
            b = float(b)
            resultado = self.calculadora.suma(a, b)
        elif '-' in linea:
            a, b = linea.split('-', 1)
            a = float(a)
            b = float(b)
            resultado = self.calculadora.resta(a, b)
        elif '*' in linea:
            a, b = linea.split('*', 1)
            a = float(a)
            b = float(b)
            resultado = self.calculadora.multiplicacion(a, b)
        elif '/' in linea:
            a, b = linea.split('/', 1)
            a = float(a)
            b = float(b)
            resultado = self.calculadora.division(a, b)
        elif 'r' in linea:
            a, b = linea.split('r', 1)
            a = float(a)
            resultado = float(self.calculadora.raiz(a))

        if float(f"{resultado:.1f}") == float(f"{resultado:.0}"):  # si la parte fraccionaria, es 0, es decir es un entero
            resultado = int(resultado)  # como realiza cualquier calculadora, devolvemos un entero
        else:
            resultado = float(f"{resultado:.5f}")  # si no devolvemos un número real con precisión de 5
        return resultado

ventana = Tk()
calculadora = Interfaz(ventana)
ventana.mainloop()