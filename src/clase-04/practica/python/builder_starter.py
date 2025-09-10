"""
Actividad 3 — Builder (Python)
Objetivo: Construir un UserProfile paso a paso (method chaining).

Requisitos:
- Clase UserProfile con campos opcionales: name, age, address, preferences (lista de str)
- Builder: UserProfileBuilder con métodos add_name, add_age, add_address, add_preference
- build() devuelve un UserProfile
- Demostración: construir perfiles completos y parciales
"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class UserProfile:
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[str] = None
    preferences: List[str] = field(default_factory=list)

class UserProfileBuilder:
    def __init__(self):
        # TODO: inicializar el objeto a construir
        pass

    def add_name(self, name: str):
        # TODO
        return self

    def add_age(self, age: int):
        # TODO
        return self

    def add_address(self, address: str):
        # TODO
        return self

    def add_preference(self, pref: str):
        # TODO
        return self

    def build(self) -> UserProfile:
        # TODO: devolver el objeto final
        raise NotImplementedError("Implementar build()")

if __name__ == "__main__":
    # TODO: construir un perfil completo y otro parcial, imprimirlos
    pass
