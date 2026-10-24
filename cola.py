from collections import deque
class cola:
    """Implementación FIFO de una cola."""

    def __init__(self, elementos=()):
        self._elementos = deque(elementos)

    def encolar(self, elemento):
        self._elementos.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("No se puede desencolar una cola vacía")
        return self._elementos.popleft()

    def frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._elementos[0]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def __len__(self):
        return len(self._elementos)