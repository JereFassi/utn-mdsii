from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, data): ...

class Publisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, sub: Subscriber):
        self._subscribers.append(sub)

    def unsubscribe(self, sub: Subscriber):
        self._subscribers.remove(sub)

    def notify(self, data):
        for sub in list(self._subscribers):
            sub.update(data)

class Stock(Publisher):
    def __init__(self):
        super().__init__()
        self._price = 0

    def set_price(self, p: float):
        self._price = p
        self.notify(self._price)

class EmailAlert(Subscriber):
    def update(self, price):
        print(f"[Email] Nuevo precio: {price}")

class MobileDisplay(Subscriber):
    def update(self, price):
        print(f"[App] Precio actualizado: {price}")

# Uso
stock = Stock()
ea = EmailAlert()
md = MobileDisplay()

stock.subscribe(ea)
stock.subscribe(md)
stock.set_price(100.5)
