from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple

class Observer(ABC):
    @abstractmethod
    def update(self, data) -> None: ...

class Publisher:
    def __init__(self) -> None:
        self._subscribers: List[Tuple[int, Observer]] = []

    def subscribe(self, sub: Observer, priority: int = 0) -> None:
        self._subscribers.append((priority, sub))
        self._subscribers.sort(key=lambda x: x[0], reverse=True)

    def unsubscribe(self, sub: Observer) -> None:
        self._subscribers = [(p, s) for (p, s) in self._subscribers if s != sub]

    def _notify(self, data) -> None:
        for _, sub in list(self._subscribers):
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
        print(f"[Email] Notificación enviada. Precio={data}")

class Dashboard(Observer):
    def update(self, data) -> None:
        print(f"[Dashboard] Actualización en pantalla. Precio={data}")

class RiskSystem(Observer):
    def update(self, data) -> None:
        print(f"[Riesgo] Evaluando volatilidad con precio={data}")

if __name__ == "__main__":
    s = Stock()
    s.subscribe(RiskSystem(), priority=10)
    s.subscribe(EmailAlert(), priority=5)
    s.subscribe(Dashboard(), priority=1)

    s.set_price(100.0)
