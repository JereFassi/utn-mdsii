from __future__ import annotations
from abc import ABC, abstractmethod

class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, origin: str, destination: str) -> str: ...

class CarRoute(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> str:
        return f"Ruta en auto de {origin} a {destination}"

class WalkRoute(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> str:
        return f"Ruta a pie de {origin} a {destination}"

class PublicTransportRoute(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> str:
        return f"Ruta en transporte público de {origin} a {destination}"

class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: RouteStrategy) -> None:
        self.strategy = strategy

    def build_route(self, origin: str, destination: str) -> str:
        return self.strategy.build_route(origin, destination)

if __name__ == "__main__":
    nav = Navigator(CarRoute())
    print(nav.build_route("Plaza", "Aeropuerto"))
    nav.set_strategy(WalkRoute())
    print(nav.build_route("Plaza", "Aeropuerto"))
