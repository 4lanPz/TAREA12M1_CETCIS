# Implementación de Listas Enlazadas en Python

## Problema 1: Gestión de Procesos

Se usa una lista enlazada simple donde cada nodo representa un proceso.
- Inserción al final de la lista.
- Recorrido para cambiar estado, eliminar y buscar.
- Reorganización de nodos para simular prioridad (mover al inicio).
- Cálculo de tiempo promedio acumulando tiempos de CPU.

---

## Problema 2: Editor de Texto

Se usa una lista enlazada donde cada nodo es una línea de texto.
- Inserción en cualquier posición recorriendo la lista.
- Eliminación y movimiento ajustando enlaces.
- Búsqueda usando comparación de texto.
- Reemplazo accediendo a una posición específica.
- Lectura y escritura de archivos para guardar/cargar contenido.

---

## Problema 3: Polinomios

Se utilizó una lista enlazada ordenada por exponentes.
- Inserción ordenada (mayor a menor exponente).
- Si un exponente se repite, se suman coeficientes.
- Operaciones:
  - Suma/resta: recorrer e insertar términos.
  - Multiplicación: doble recorrido.
  - Evaluación: cálculo directo.
  - Derivada e integral: fórmulas matemáticas aplicadas a cada nodo.

---

## Problema 4: Hoja de Cálculo Dispersa

Se implementó una estructura con **listas enlazadas por filas y columnas**.
- Solo se almacenan celdas con datos (estructura dispersa).
- Inserción enlazando en fila y columna.
- Eliminación ajustando ambos enlaces.
- Operaciones sobre rangos recorriendo filas.
- Inserción/eliminación de filas y columnas reconstruyendo la estructura.
- Comparación de memoria vs matriz completa.
