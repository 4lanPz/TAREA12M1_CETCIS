#Ejercicio 4

# Cada celda guarda:
# fila
# columna
# valor
# derecha = siguiente en la fila
# abajo = siguiente en la columna

class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.derecha = None
        self.abajo = None

class HojaDispersa:
    def __init__(self):
        self.filas = {}      # encabezados por fila
        self.columnas = {}   # encabezados por columna

    # Buscar una celda exacta
    def buscar_celda(self, fila, columna):
        if fila not in self.filas:
            return None
        actual = self.filas[fila]
        while actual is not None:
            if actual.columna == columna:
                return actual
            actual = actual.derecha
        return None

    # Insertar o actualizar una celda
    def insertar_actualizar(self, fila, columna, valor):
        existente = self.buscar_celda(fila, columna)
        # Si ya existe, solo cambia valor
        if existente is not None:
            existente.valor = valor
            return
        nueva = Celda(fila, columna, valor)
        # Insertar en lista de fila
        if fila not in self.filas or self.filas[fila] is None or self.filas[fila].columna > columna:
            nueva.derecha = self.filas.get(fila)
            self.filas[fila] = nueva
        else:
            actual = self.filas[fila]
            while actual.derecha is not None and actual.derecha.columna < columna:
                actual = actual.derecha
            nueva.derecha = actual.derecha
            actual.derecha = nueva
        # Insertar en lista de columna
        if columna not in self.columnas or self.columnas[columna] is None or self.columnas[columna].fila > fila:
            nueva.abajo = self.columnas.get(columna)
            self.columnas[columna] = nueva
        else:
            actual = self.columnas[columna]
            while actual.abajo is not None and actual.abajo.fila < fila:
                actual = actual.abajo
            nueva.abajo = actual.abajo
            actual.abajo = nueva

    # Eliminar celda
    def eliminar_celda(self, fila, columna):
        encontrada = False
        # Eliminar de la lista por fila
        if fila in self.filas:
            actual = self.filas[fila]
            anterior = None
            while actual is not None and actual.columna != columna:
                anterior = actual
                actual = actual.derecha
            if actual is not None:
                encontrada = True
                if anterior is None:
                    self.filas[fila] = actual.derecha
                else:
                    anterior.derecha = actual.derecha
        # Eliminar de la lista por columna
        if columna in self.columnas:
            actual = self.columnas[columna]
            anterior = None
            while actual is not None and actual.fila != fila:
                anterior = actual
                actual = actual.abajo
            if actual is not None:
                if anterior is None:
                    self.columnas[columna] = actual.abajo
                else:
                    anterior.abajo = actual.abajo
        return encontrada

    # Obtener valor de una celda
    def obtener_valor(self, fila, columna):
        celda = self.buscar_celda(fila, columna)
        if celda is not None:
            return celda.valor
        return None

    # Sumar un rango
    def sumar_rango(self, fila_inicio, col_inicio, fila_fin, col_fin):
        suma = 0
        for fila in range(fila_inicio, fila_fin + 1):
            if fila in self.filas:
                actual = self.filas[fila]
                while actual is not None:
                    if col_inicio <= actual.columna <= col_fin:
                        if isinstance(actual.valor, (int, float)):
                            suma += actual.valor
                    actual = actual.derecha
        return suma

    # Promediar un rango
    def promediar_rango(self, fila_inicio, col_inicio, fila_fin, col_fin):
        suma = 0
        cantidad = 0
        for fila in range(fila_inicio, fila_fin + 1):
            if fila in self.filas:
                actual = self.filas[fila]
                while actual is not None:
                    if col_inicio <= actual.columna <= col_fin:
                        if isinstance(actual.valor, (int, float)):
                            suma += actual.valor
                            cantidad += 1
                    actual = actual.derecha
        if cantidad == 0:
            return 0
        return suma / cantidad

    # Insertar una fila completa
    def insertar_fila(self, fila_insertar):
        nuevas_filas = {}
        nuevas_columnas = {}
        # Recoger todas las celdas
        celdas = []
        for fila in self.filas:
            actual = self.filas[fila]
            while actual is not None:
                if actual.fila >= fila_insertar:
                    celdas.append((actual.fila + 1, actual.columna, actual.valor))
                else:
                    celdas.append((actual.fila, actual.columna, actual.valor))
                actual = actual.derecha
        # Reiniciar estructura
        self.filas = {}
        self.columnas = {}
        # Reinsertar
        for fila, columna, valor in celdas:
            self.insertar_actualizar(fila, columna, valor)

    # Eliminar una fila completa
    def eliminar_fila(self, fila_eliminar):
        celdas = []
        for fila in self.filas:
            actual = self.filas[fila]
            while actual is not None:
                if actual.fila != fila_eliminar:
                    if actual.fila > fila_eliminar:
                        celdas.append((actual.fila - 1, actual.columna, actual.valor))
                    else:
                        celdas.append((actual.fila, actual.columna, actual.valor))
                actual = actual.derecha
        self.filas = {}
        self.columnas = {}
        for fila, columna, valor in celdas:
            self.insertar_actualizar(fila, columna, valor)

    # Insertar una columna completa
    def insertar_columna(self, columna_insertar):
        celdas = []
        for fila in self.filas:
            actual = self.filas[fila]
            while actual is not None:
                if actual.columna >= columna_insertar:
                    celdas.append((actual.fila, actual.columna + 1, actual.valor))
                else:
                    celdas.append((actual.fila, actual.columna, actual.valor))
                actual = actual.derecha
        self.filas = {}
        self.columnas = {}
        for fila, columna, valor in celdas:
            self.insertar_actualizar(fila, columna, valor)

    # Eliminar una columna completa
    def eliminar_columna(self, columna_eliminar):
        celdas = []
        for fila in self.filas:
            actual = self.filas[fila]
            while actual is not None:
                if actual.columna != columna_eliminar:
                    if actual.columna > columna_eliminar:
                        celdas.append((actual.fila, actual.columna - 1, actual.valor))
                    else:
                        celdas.append((actual.fila, actual.columna, actual.valor))
                actual = actual.derecha
        self.filas = {}
        self.columnas = {}
        for fila, columna, valor in celdas:
            self.insertar_actualizar(fila, columna, valor)

    # Mostrar en forma tabular
    def mostrar_hoja(self, max_filas, max_columnas):
        print("\n--- HOJA DISPERSA ---")
        for i in range(1, max_filas + 1):
            fila_texto = []
            for j in range(1, max_columnas + 1):
                valor = self.obtener_valor(i, j)
                if valor is None:
                    fila_texto.append(".")
                else:
                    fila_texto.append(str(valor))
            print("\t".join(fila_texto))

    # Guardar en archivo
    def guardar_archivo(self, nombre_archivo):
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        for fila in self.filas:
            actual = self.filas[fila]
            while actual is not None:
                archivo.write(f"{actual.fila},{actual.columna},{actual.valor}\n")
                actual = actual.derecha
        archivo.close()

    # Cargar desde archivo
    def cargar_archivo(self, nombre_archivo):
        try:
            archivo = open(nombre_archivo, "r", encoding="utf-8")
            self.filas = {}
            self.columnas = {}
            for linea in archivo:
                fila, columna, valor = linea.strip().split(",")
                # convertir a número si se puede
                if valor.replace(".", "", 1).isdigit():
                    if "." in valor:
                        valor = float(valor)
                    else:
                        valor = int(valor)
                self.insertar_actualizar(int(fila), int(columna), valor)
            archivo.close()
            return True
        except FileNotFoundError:
            return False

    # Contar celdas ocupadas
    def contar_celdas_ocupadas(self):
        total = 0
        for fila in self.filas:
            actual = self.filas[fila]
            while actual is not None:
                total += 1
                actual = actual.derecha
        return total

    # Comparación simple con matriz completa
    def comparar_memoria(self, max_filas, max_columnas):
        matriz_completa = max_filas * max_columnas
        dispersa = self.contar_celdas_ocupadas()
        print("\n--- COMPARACIÓN DE MEMORIA ---")
        print("Celdas de matriz completa:", matriz_completa)
        print("Celdas almacenadas en hoja dispersa:", dispersa)

hoja = HojaDispersa()
opcion = ""

while opcion != "11":
    print("\n===== MENU HOJA DISPERSA =====")
    print("1. Insertar o actualizar celda")
    print("2. Eliminar celda")
    print("3. Obtener valor de una celda")
    print("4. Sumar rango")
    print("5. Promediar rango")
    print("6. Insertar fila")
    print("7. Eliminar fila")
    print("8. Insertar columna")
    print("9. Eliminar columna")
    print("10. Mostrar hoja")
    print("11. Salir")
    print("12. Guardar archivo")
    print("13. Cargar archivo")
    print("14. Comparar memoria")
    opcion = input("Opción: ")
    if opcion == "1":
        fila = int(input("Fila: "))
        columna = int(input("Columna: "))
        valor_texto = input("Valor: ")
        # convertir a número si se puede
        if valor_texto.replace(".", "", 1).isdigit():
            if "." in valor_texto:
                valor = float(valor_texto)
            else:
                valor = int(valor_texto)
        else:
            valor = valor_texto
        hoja.insertar_actualizar(fila, columna, valor)
        print("Celda guardada.")
    elif opcion == "2":
        fila = int(input("Fila: "))
        columna = int(input("Columna: "))
        if hoja.eliminar_celda(fila, columna):
            print("Celda eliminada.")
        else:
            print("La celda no existe.")
    elif opcion == "3":
        fila = int(input("Fila: "))
        columna = int(input("Columna: "))
        valor = hoja.obtener_valor(fila, columna)
        if valor is None:
            print("Celda vacía.")
        else:
            print("Valor:", valor)
    elif opcion == "4":
        fila1 = int(input("Fila inicial: "))
        col1 = int(input("Columna inicial: "))
        fila2 = int(input("Fila final: "))
        col2 = int(input("Columna final: "))
        print("Suma:", hoja.sumar_rango(fila1, col1, fila2, col2))
    elif opcion == "5":
        fila1 = int(input("Fila inicial: "))
        col1 = int(input("Columna inicial: "))
        fila2 = int(input("Fila final: "))
        col2 = int(input("Columna final: "))
        print("Promedio:", hoja.promediar_rango(fila1, col1, fila2, col2))
    elif opcion == "6":
        fila = int(input("Número de fila a insertar: "))
        hoja.insertar_fila(fila)
        print("Fila insertada.")
    elif opcion == "7":
        fila = int(input("Número de fila a eliminar: "))
        hoja.eliminar_fila(fila)
        print("Fila eliminada.")
    elif opcion == "8":
        columna = int(input("Número de columna a insertar: "))
        hoja.insertar_columna(columna)
        print("Columna insertada.")
    elif opcion == "9":
        columna = int(input("Número de columna a eliminar: "))
        hoja.eliminar_columna(columna)
        print("Columna eliminada.")
    elif opcion == "10":
        max_filas = int(input("Mostrar hasta fila: "))
        max_columnas = int(input("Mostrar hasta columna: "))
        hoja.mostrar_hoja(max_filas, max_columnas)
    elif opcion == "11":
        print("Fin del programa.")
    elif opcion == "12":
        nombre = input("Nombre del archivo: ")
        hoja.guardar_archivo(nombre)
        print("Hoja guardada.")
    elif opcion == "13":
        nombre = input("Nombre del archivo: ")
        if hoja.cargar_archivo(nombre):
            print("Hoja cargada.")
        else:
            print("Archivo no encontrado.")
    elif opcion == "14":
        max_filas = int(input("Cantidad de filas de referencia: "))
        max_columnas = int(input("Cantidad de columnas de referencia: "))
        hoja.comparar_memoria(max_filas, max_columnas)
    else:
        print("Opción inválida.")