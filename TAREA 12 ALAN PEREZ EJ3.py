#Ejercicio 3

# Cada nodo guarda:
# coeficiente
# exponente
# siguiente

class Termino:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None

    # Insertar término ordenado por exponente de mayor a menor
    def insertar_termino(self, coeficiente, exponente):
        if coeficiente == 0:
            return
        nuevo = Termino(coeficiente, exponente)
        # Insertar al inicio
        if self.cabeza is None or exponente > self.cabeza.exponente:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return
        actual = self.cabeza
        anterior = None
        # Buscar posición correcta
        while actual is not None and actual.exponente > exponente:
            anterior = actual
            actual = actual.siguiente
        # Si ya existe el exponente, sumar coeficientes
        if actual is not None and actual.exponente == exponente:
            actual.coeficiente += coeficiente
            # Si queda en 0, eliminar término
            if actual.coeficiente == 0:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
            return
        # Insertar entre nodos
        nuevo.siguiente = actual
        if anterior is not None:
            anterior.siguiente = nuevo

    # Mostrar polinomio
    def mostrar(self):
        if self.cabeza is None:
            print("0")
            return
        actual = self.cabeza
        texto = ""
        while actual is not None:
            c = actual.coeficiente
            e = actual.exponente
            # Signo
            if texto != "":
                if c >= 0:
                    texto += " + "
                else:
                    texto += " - "
                    c = -c
            else:
                if c < 0:
                    texto += "-"
                    c = -c
            # Formato del término
            if e == 0:
                texto += str(c)
            elif e == 1:
                if c == 1:
                    texto += "x"
                else:
                    texto += str(c) + "x"
            else:
                if c == 1:
                    texto += "x^" + str(e)
                else:
                    texto += str(c) + "x^" + str(e)
            actual = actual.siguiente
        print(texto)

    # Evaluar polinomio
    def evaluar(self, x):
        actual = self.cabeza
        resultado = 0
        while actual is not None:
            resultado += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente
        return resultado

    # Derivar polinomio
    def derivar(self):
        derivada = Polinomio()
        actual = self.cabeza
        while actual is not None:
            if actual.exponente != 0:
                nuevo_coef = actual.coeficiente * actual.exponente
                nuevo_exp = actual.exponente - 1
                derivada.insertar_termino(nuevo_coef, nuevo_exp)
            actual = actual.siguiente
        return derivada

    # Integrar polinomio
    def integrar(self):
        integral = Polinomio()
        actual = self.cabeza
        while actual is not None:
            nuevo_coef = actual.coeficiente / (actual.exponente + 1)
            nuevo_exp = actual.exponente + 1
            integral.insertar_termino(nuevo_coef, nuevo_exp)
            actual = actual.siguiente
        return integral

    # Vaciar polinomio
    def limpiar(self):
        self.cabeza = None

# Sumar dos polinomios
def sumar_polinomios(p1, p2):
    resultado = Polinomio()
    actual = p1.cabeza
    while actual is not None:
        resultado.insertar_termino(actual.coeficiente, actual.exponente)
        actual = actual.siguiente
    actual = p2.cabeza
    while actual is not None:
        resultado.insertar_termino(actual.coeficiente, actual.exponente)
        actual = actual.siguiente
    return resultado

# Restar dos polinomios
def restar_polinomios(p1, p2):
    resultado = Polinomio()
    actual = p1.cabeza
    while actual is not None:
        resultado.insertar_termino(actual.coeficiente, actual.exponente)
        actual = actual.siguiente
    actual = p2.cabeza
    while actual is not None:
        resultado.insertar_termino(-actual.coeficiente, actual.exponente)
        actual = actual.siguiente
    return resultado

# Multiplicar dos polinomios
def multiplicar_polinomios(p1, p2):
    resultado = Polinomio()
    a = p1.cabeza
    while a is not None:
        b = p2.cabeza
        while b is not None:
            coef = a.coeficiente * b.coeficiente
            exp = a.exponente + b.exponente
            resultado.insertar_termino(coef, exp)
            b = b.siguiente
        a = a.siguiente
    return resultado

# Escoger polinomio
def seleccionar_polinomio(opcion, p1, p2, p3):
    if opcion == "1":
        return p1
    elif opcion == "2":
        return p2
    elif opcion == "3":
        return p3
    else:
        return None

# Crear polinomios base
p1 = Polinomio()
p2 = Polinomio()
p3 = Polinomio()

opcion = ""

while opcion != "9":
    print("\n===== MENU POLINOMIOS =====")
    print("1. Agregar término a un polinomio")
    print("2. Mostrar polinomios")
    print("3. Sumar dos polinomios")
    print("4. Restar dos polinomios")
    print("5. Multiplicar dos polinomios")
    print("6. Evaluar un polinomio")
    print("7. Derivar un polinomio")
    print("8. Integrar un polinomio")
    print("9. Salir")
    print("10. Limpiar un polinomio")
    opcion = input("Opción: ")
    if opcion == "1":
        print("Seleccione polinomio: 1=P1, 2=P2, 3=P3")
        cual = input("Polinomio: ")
        poli = seleccionar_polinomio(cual, p1, p2, p3)
        if poli is None:
            print("Polinomio no válido.")
        else:
            coef = float(input("Coeficiente: "))
            exp = int(input("Exponente: "))
            poli.insertar_termino(coef, exp)
            print("Término agregado.")
    elif opcion == "2":
        print("\nP1 = ", end="")
        p1.mostrar()
        print("P2 = ", end="")
        p2.mostrar()
        print("P3 = ", end="")
        p3.mostrar()
    elif opcion == "3":
        print("Seleccione los polinomios a sumar")
        a = input("Primer polinomio (1,2,3): ")
        b = input("Segundo polinomio (1,2,3): ")
        pa = seleccionar_polinomio(a, p1, p2, p3)
        pb = seleccionar_polinomio(b, p1, p2, p3)
        if pa is None or pb is None:
            print("Selección no válida.")
        else:
            resultado = sumar_polinomios(pa, pb)
            print("Resultado = ", end="")
            resultado.mostrar()
    elif opcion == "4":
        print("Seleccione los polinomios a restar")
        a = input("Polinomio 1 (minuendo): ")
        b = input("Polinomio 2 (sustraendo): ")
        pa = seleccionar_polinomio(a, p1, p2, p3)
        pb = seleccionar_polinomio(b, p1, p2, p3)
        if pa is None or pb is None:
            print("Selección no válida.")
        else:
            resultado = restar_polinomios(pa, pb)
            print("Resultado = ", end="")
            resultado.mostrar()
    elif opcion == "5":
        print("Seleccione los polinomios a multiplicar")
        a = input("Primer polinomio (1,2,3): ")
        b = input("Segundo polinomio (1,2,3): ")
        pa = seleccionar_polinomio(a, p1, p2, p3)
        pb = seleccionar_polinomio(b, p1, p2, p3)
        if pa is None or pb is None:
            print("Selección no válida.")
        else:
            resultado = multiplicar_polinomios(pa, pb)
            print("Resultado = ", end="")
            resultado.mostrar()
    elif opcion == "6":
        print("Seleccione polinomio: 1=P1, 2=P2, 3=P3")
        cual = input("Polinomio: ")
        poli = seleccionar_polinomio(cual, p1, p2, p3)
        if poli is None:
            print("Polinomio no válido.")
        else:
            x = float(input("Valor de x: "))
            print("Resultado =", poli.evaluar(x))
    elif opcion == "7":
        print("Seleccione polinomio: 1=P1, 2=P2, 3=P3")
        cual = input("Polinomio: ")
        poli = seleccionar_polinomio(cual, p1, p2, p3)
        if poli is None:
            print("Polinomio no válido.")
        else:
            resultado = poli.derivar()
            print("Derivada = ", end="")
            resultado.mostrar()
    elif opcion == "8":
        print("Seleccione polinomio: 1=P1, 2=P2, 3=P3")
        cual = input("Polinomio: ")
        poli = seleccionar_polinomio(cual, p1, p2, p3)
        if poli is None:
            print("Polinomio no válido.")
        else:
            resultado = poli.integrar()
            print("Integral = ", end="")
            resultado.mostrar()
            print(" + C")
    elif opcion == "9":
        print("Fin del programa.")
    elif opcion == "10":
        print("Seleccione polinomio: 1=P1, 2=P2, 3=P3")
        cual = input("Polinomio: ")
        poli = seleccionar_polinomio(cual, p1, p2, p3)
        if poli is None:
            print("Polinomio no válido.")
        else:
            poli.limpiar()
            print("Polinomio limpiado.")
    else:
        print("Opción inválida.")