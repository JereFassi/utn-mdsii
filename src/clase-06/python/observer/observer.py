from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, data) -> None: ...

class Publisher:
    def __init__(self) -> None:
        self._subscribers: List[Observer] = []

    def subscribe(self, sub: Observer) -> None:
        self._subscribers.append(sub)

    def unsubscribe(self, sub: Observer) -> None:
        self._subscribers.remove(sub)

    def _notify(self, data) -> None:
        # Se usa copia para evitar problemas si alguien se desuscribe durante la iteración
        for sub in list(self._subscribers):
            sub.update(data)

class Stock(Publisher):
    def __init__(self) -> None:
        super().__init__()
        self._price: float = 0.0

    def set_price(self, value: float) -> None:
        self._price = value
        self._notify(self._price)

class EmailAlert(Observer):
    def update(self, data) -> None:
        print(f"[Email] Nuevo precio: {data}")

class Dashboard(Observer):
    def update(self, data) -> None:
        print(f"[Dashboard] Precio actualizado: {data}")

if __name__ == "__main__":
    s = Stock()
    e = EmailAlert()
    d = Dashboard()
    s.subscribe(e)
    s.subscribe(d)
    s.set_price(123.45)
