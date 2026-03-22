#Ejercicio 1

# Estados:
# 1 = listo
# 2 = ejecucion
# 3 = bloqueado
# 4 = terminado

class Proceso:
    def __init__(self, id_proceso, nombre, estado, tiempo_creacion, tiempo_cpu):
        self.id = id_proceso
        self.nombre = nombre
        self.estado = estado
        self.tiempo_creacion = tiempo_creacion
        self.tiempo_cpu = tiempo_cpu
        self.siguiente = None

class ListaProcesos:
    def __init__(self):
        self.cabeza = None
        self.contador_id = 1 

    # Generar ID automáticamente
    def generar_id(self):
        id_actual = self.contador_id
        self.contador_id += 1
        return id_actual

    # Agregar proceso al final
    def agregar_proceso(self, nombre, estado, tiempo_creacion, tiempo_cpu):
        id_proceso = self.generar_id()  # se genera solo
        nuevo = Proceso(id_proceso, nombre, estado, tiempo_creacion, tiempo_cpu)
        if self.cabeza is None:
            self.cabeza = nuevo
            return id_proceso
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo
        return id_proceso

    # Cambiar estado
    def cambiar_estado(self, id_proceso, nuevo_estado):
        actual = self.cabeza
        while actual is not None:
            if actual.id == id_proceso:
                actual.estado = nuevo_estado
                return True
            actual = actual.siguiente
        return False

    # Eliminar procesos terminados (estado 4)
    def eliminar_terminados(self):
        eliminados = 0
        while self.cabeza is not None and self.cabeza.estado == 4:
            self.cabeza = self.cabeza.siguiente
            eliminados += 1
        actual = self.cabeza
        while actual is not None and actual.siguiente is not None:
            if actual.siguiente.estado == 4:
                actual.siguiente = actual.siguiente.siguiente
                eliminados += 1
            else:
                actual = actual.siguiente
        return eliminados

    # Mover al inicio
    def mover_al_inicio(self, id_proceso):
        if self.cabeza is None:
            return False
        if self.cabeza.id == id_proceso:
            return True
        anterior = None
        actual = self.cabeza
        while actual is not None and actual.id != id_proceso:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            return False
        anterior.siguiente = actual.siguiente
        actual.siguiente = self.cabeza
        self.cabeza = actual
        return True

    # Mostrar procesos
    def mostrar_procesos(self):
        if self.cabeza is None:
            print("\nNo hay procesos.")
            return
        actual = self.cabeza
        print("\n--- PROCESOS ---")
        while actual is not None:
            print(
                f"ID: {actual.id} | Nombre: {actual.nombre} | "
                f"Estado: {actual.estado} | Creación: {actual.tiempo_creacion} | CPU: {actual.tiempo_cpu}"
            )
            actual = actual.siguiente

    # Promedio de espera
    def promedio_espera(self):
        actual = self.cabeza
        suma = 0
        acumulado = 0
        cantidad = 0
        while actual is not None:
            suma += acumulado
            acumulado += actual.tiempo_cpu
            cantidad += 1
            actual = actual.siguiente
        if cantidad == 0:
            return 0
        return suma / cantidad

lista = ListaProcesos()

opcion = ""

while opcion != "7":
    print("\n===== MENU =====")
    print("1. Añadir proceso")
    print("2. Cambiar estado")
    print("3. Eliminar terminados")
    print("4. Mover proceso al inicio")
    print("5. Mostrar procesos")
    print("6. Promedio de espera")
    print("7. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        print("Estados: 1=listo, 2=ejecucion, 3=bloqueado, 4=terminado")
        estado = int(input("Estado: "))
        tiempo_creacion = int(input("Tiempo de creación: "))
        tiempo_cpu = int(input("Tiempo CPU: "))
        id_generado = lista.agregar_proceso(nombre, estado, tiempo_creacion, tiempo_cpu)
        print(f"Proceso agregado con ID automático: {id_generado}")
    elif opcion == "2":
        id_proceso = int(input("ID del proceso: "))
        print("Estados: 1=listo, 2=ejecucion, 3=bloqueado, 4=terminado")
        nuevo_estado = int(input("Nuevo estado: "))
        if lista.cambiar_estado(id_proceso, nuevo_estado):
            print("Estado actualizado.")
        else:
            print("Proceso no encontrado.")
    elif opcion == "3":
        eliminados = lista.eliminar_terminados()
        print("Procesos eliminados:", eliminados)
    elif opcion == "4":
        id_proceso = int(input("ID a mover: "))
        if lista.mover_al_inicio(id_proceso):
            print("Movido al inicio.")
        else:
            print("No encontrado.")
    elif opcion == "5":
        lista.mostrar_procesos()
    elif opcion == "6":
        print("Promedio de espera:", lista.promedio_espera())
    elif opcion == "7":
        print("Fin del programa.")
    else:
        print("Opción inválida.")