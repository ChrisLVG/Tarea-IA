from cola import cola
from pila import pila

matriz = [
    [2, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 3],
]

def marcar(posicion, matriz):
    fila,columna=posicion
    matriz[fila][columna] = "*"
    

def obtener_vecinos(inicio, matriz):
    vecinos = []
    filas = len(matriz)
    columnas = len(matriz[0])
    fila, columna = inicio

    # Arriba
    if fila > 0:
        vecinos.append((fila - 1, columna))
    # Abajo
    if fila < filas - 1:
        vecinos.append((fila + 1, columna))
    # Izquierda
    if columna > 0:
        vecinos.append((fila, columna - 1))
    # Derecha
    if columna < columnas - 1:
        vecinos.append((fila, columna + 1))

    return vecinos



def explorar_con_cola(matriz, inicio):
    matriz_cola = [fila[:] for fila in matriz]
    visitados = list()
    paredes=list()
    pendientes = cola()
    pendientes.encolar(inicio)
    pasos = 0

    while not pendientes.esta_vacia():
        posicion = pendientes.desencolar()
        if posicion == (3, 3):  # Verifica si se ha llegado a la posición final
            break
        fila,columna=posicion
        if matriz_cola[fila][columna] == 1: # Verifica si el valor de nuestra posicion actual es una pared (1)
            if posicion not in paredes: # verifica si la pared ya ha sido antes encontrada
                paredes.append(posicion)
                pasos += 1
        else:
            for vecino in obtener_vecinos(posicion, matriz):
                 if vecino!= inicio and vecino not in visitados: #verifica si el vecino no es el inicio y no ha sido visitado
                    pendientes.encolar(vecino) #agregamos los vecinos a la cola para seguir explorando
            if posicion!=inicio and posicion not in visitados: # Verifica si el vecino no ha sido visitado
                visitados.append(posicion)
                pasos += 1
    for pos in visitados:
        marcar(pos, matriz_cola)
    return visitados, pasos, matriz_cola

def explorar_con_pila(matriz, inicio):
    matriz_pila = [fila[:] for fila in matriz]
    paredes=list()
    visitados = list()
    recorrido = pila()
    recorrido.apilar(inicio)
    pasos = 0

    while not recorrido.esta_vacia():
        posicion = recorrido.desapilar()
        if posicion == (3, 3):  # Verifica si se ha llegado a la posición final
            break
        fila,columna=posicion
        if matriz_pila[fila][columna] == 1: # Verifica si el valor de nuestra posicion actual es una pared (1) 
            if posicion not in paredes: # Verifica que no se haya visto antes la misma pared
                paredes.append(matriz_pila[fila][columna]) # se puede usar tanto posicion como las coordenadas de la matriz ya que paredes es una lista de tuplas 
                pasos += 1
        else:
            for vecino in obtener_vecinos(posicion, matriz):
                if vecino!= inicio and vecino not in visitados: #verifica si el vecino no es el inicio y no ha sido visitado
                    recorrido.apilar(vecino) #agregamos los vecinos a la pila para seguir explorando
            if posicion!=inicio and posicion not in visitados: # Verifica si el vecino no ha sido visitado
                visitados.append(posicion)
                pasos += 1
    for paso in visitados:
        marcar(paso,matriz_pila)
    return visitados, pasos, matriz_pila

print("Exploración con cola (BFS):")
visitados_cola, pasos_cola, matriz_cola = explorar_con_cola(matriz, (0, 0))
print("Posiciones visitadas:", visitados_cola)
print("Pasos realizados:", pasos_cola)
print("Matriz después de la exploración con cola:")
for fila in matriz_cola:
    print(fila)
print()
print("Exploración con pila (DFS):")
visitados_pila, pasos_pila, matriz_pila = explorar_con_pila(matriz, (0, 0))
print("Posiciones visitadas:", visitados_pila)
print("Pasos realizados:", pasos_pila)
print("Matriz después de la exploración con pila:")
for fila in matriz_pila:
    print(fila)