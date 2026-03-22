#Ejercicio 2

class Linea:
    def __init__(self, texto):
        self.texto = texto
        self.siguiente = None

class EditorTexto:
    def __init__(self):
        self.cabeza = None

    # Contar líneas
    def contar_lineas(self):
        actual = self.cabeza
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    # Insertar línea en una posición
    def insertar_linea(self, texto, posicion):
        nueva = Linea(texto)
        if posicion <= 1 or self.cabeza is None:
            nueva.siguiente = self.cabeza
            self.cabeza = nueva
            return
        actual = self.cabeza
        indice = 1
        while actual.siguiente is not None and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1
        nueva.siguiente = actual.siguiente
        actual.siguiente = nueva

    # Eliminar línea por posición
    def eliminar_linea(self, posicion):
        if self.cabeza is None:
            return False
        if posicion == 1:
            self.cabeza = self.cabeza.siguiente
            return True
        actual = self.cabeza
        indice = 1
        while actual.siguiente is not None and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1
        if actual.siguiente is not None:
            actual.siguiente = actual.siguiente.siguiente
            return True
        return False

    # Obtener una línea por posición
    def obtener_linea(self, posicion):
        actual = self.cabeza
        indice = 1
        while actual is not None:
            if indice == posicion:
                return actual
            actual = actual.siguiente
            indice += 1
        return None

    # Mover una línea a otra posición
    def mover_linea(self, origen, destino):
        if self.cabeza is None:
            return False
        if origen == destino:
            return True
        actual = self.cabeza
        anterior = None
        indice = 1
        # Buscar línea de origen
        while actual is not None and indice < origen:
            anterior = actual
            actual = actual.siguiente
            indice += 1
        if actual is None:
            return False
        linea_mover = actual
        # Sacar línea de su lugar
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        # Insertar al inicio
        if destino <= 1:
            linea_mover.siguiente = self.cabeza
            self.cabeza = linea_mover
            return True
        actual = self.cabeza
        indice = 1
        while actual is not None and actual.siguiente is not None and indice < destino - 1:
            actual = actual.siguiente
            indice += 1
        linea_mover.siguiente = actual.siguiente
        actual.siguiente = linea_mover
        return True

    # Buscar texto en todas las líneas
    def buscar_texto(self, texto_buscar):
        actual = self.cabeza
        numero = 1
        encontrado = False
        while actual is not None:
            if texto_buscar.lower() in actual.texto.lower():
                print(f"Línea {numero}: {actual.texto}")
                encontrado = True
            actual = actual.siguiente
            numero += 1
        if not encontrado:
            print("Texto no encontrado.")

    # Reemplazar texto en una línea específica
    def reemplazar_linea(self, posicion, nuevo_texto):
        linea = self.obtener_linea(posicion)
        if linea is not None:
            linea.texto = nuevo_texto
            return True
        return False

    # Mostrar todas las líneas
    def mostrar_contenido(self):
        if self.cabeza is None:
            print("\nEl editor está vacío.")
            return
        actual = self.cabeza
        numero = 1
        print("\n--- CONTENIDO DEL EDITOR ---")
        while actual is not None:
            print(f"{numero}. {actual.texto}")
            actual = actual.siguiente
            numero += 1

    # Guardar en archivo
    def guardar_archivo(self, nombre_archivo):
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        actual = self.cabeza
        while actual is not None:
            archivo.write(actual.texto + "\n")
            actual = actual.siguiente
        archivo.close()

    # Cargar desde archivo
    def cargar_archivo(self, nombre_archivo):
        try:
            archivo = open(nombre_archivo, "r", encoding="utf-8")
            # Vaciar editor antes de cargar
            self.cabeza = None
            for linea in archivo:
                texto = linea.strip()
                self.insertar_linea(texto, self.contar_lineas() + 1)
            archivo.close()
            return True
        except FileNotFoundError:
            return False

editor = EditorTexto()
opcion = ""

while opcion != "8":
    print("\n===== MENU EDITOR =====")
    print("1. Insertar nueva línea")
    print("2. Eliminar línea")
    print("3. Mover línea")
    print("4. Buscar texto")
    print("5. Reemplazar línea")
    print("6. Guardar en archivo")
    print("7. Cargar desde archivo")
    print("8. Salir")
    print("9. Mostrar contenido")
    opcion = input("Opción: ")
    if opcion == "1":
        texto = input("Ingrese el texto de la nueva línea: ")
        posicion = int(input("Ingrese la posición donde desea insertarla: "))
        editor.insertar_linea(texto, posicion)
        print("Línea insertada.")
    elif opcion == "2":
        posicion = int(input("Ingrese la posición de la línea a eliminar: "))
        if editor.eliminar_linea(posicion):
            print("Línea eliminada.")
        else:
            print("No se pudo eliminar la línea.")
    elif opcion == "3":
        origen = int(input("Ingrese la posición de origen: "))
        destino = int(input("Ingrese la nueva posición: "))
        if editor.mover_linea(origen, destino):
            print("Línea movida.")
        else:
            print("No se pudo mover la línea.")
    elif opcion == "4":
        texto_buscar = input("Ingrese el texto a buscar: ")
        editor.buscar_texto(texto_buscar)
    elif opcion == "5":
        posicion = int(input("Ingrese la posición de la línea a reemplazar: "))
        nuevo_texto = input("Ingrese el nuevo texto: ")
        if editor.reemplazar_linea(posicion, nuevo_texto):
            print("Línea reemplazada.")
        else:
            print("No se encontró la línea.")
    elif opcion == "6":
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        editor.guardar_archivo(nombre_archivo)
        print("Contenido guardado.")
    elif opcion == "7":
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        if editor.cargar_archivo(nombre_archivo):
            print("Contenido cargado.")
        else:
            print("No se encontró el archivo.")
    elif opcion == "8":
        print("Fin del programa.")
    elif opcion == "9":
        editor.mostrar_contenido()
    else:
        print("Opción inválida.")