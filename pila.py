from collections import deque
class pila:
    """Implementación LIFO de una pila."""

    def __init__(self, elementos=()):
        self._elementos = deque(elementos)

    def apilar(self, elemento):
        self._elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("No se puede desapilar una pila vacía")
        return self._elementos.pop()

    def cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._elementos[-1]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def __len__(self):
        return len(self._elementos)