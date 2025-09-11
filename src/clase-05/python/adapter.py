from __future__ import annotations
from abc import ABC, abstractmethod

# Interfaz objetivo que el cliente espera
class NewInterface(ABC):
    @abstractmethod
    def request(self) -> str:  # pragma: no cover
        pass

# Clase existente (incompatible) que no podemos modificar
class OldSystem:
    def specific_request(self) -> str:
        return "Respuesta del sistema antiguo (XML → datos brutos)"

# Adapter: traduce la interfaz de OldSystem a NewInterface
class Adapter(NewInterface):
    def __init__(self, adaptee: OldSystem):
        self._adaptee = adaptee

    def request(self) -> str:
        raw = self._adaptee.specific_request()
        normalized = raw.replace(" (XML → datos brutos)", " (normalizado)")
        return normalized

def main():
    old = OldSystem()
    adapter = Adapter(old)
    print(adapter.request())  # "Respuesta del sistema antiguo (normalizado)"

if __name__ == "__main__":
    main()
