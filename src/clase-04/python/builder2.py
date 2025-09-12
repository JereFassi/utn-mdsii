from typing import Dict, Optional

class UserProfile:
    def __init__(self, name: Optional[str] = None, age: Optional[int] = None, address: Optional[str] = None, preferences: Optional[Dict[str, str]] = None):
        self.name = name
        self.age = age
        self.address = address
        self.preferences = preferences or {}

    def is_valid(self):
    # Validación simple: consideramos válido si tiene nombre.
        return bool(self.name and isinstance(self.name, str) and self.name.strip())


    def __str__(self) -> str:
        return (f"UserProfile(name={self.name!r}, age={self.age!r}, "
        f"address={self.address!r}, preferences={self.preferences!r})")

class UserProfileBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = None
        self.age = None
        self.address = None
        self.preferences = {}
        return self

    def add_name(self, name: str):
        self.name = name
        return self

    def add_age(self, age: int):
        self.age = age
        return self

    def add_address(self, address: str):
        self.address = address
        return self

    def add_preferences(self, prefs: Dict[str, str]):
        self.preferences|=prefs
        return self

    def build(self):
        profile = UserProfile(
        name=self.name,
        age=self.age,
        address=self.address,
        preferences=dict(self.preferences),
        )
        return profile
    

builder = UserProfileBuilder()
perfil_completo = (builder.add_name("Juan Pérez")
.add_age(28)
.add_address("Calle Falsa 123")
.add_preferences({"theme": "dark", "lang": "es"})
.build())
print(perfil_completo)
print("¿Válido?", perfil_completo.is_valid())

perfil_parcial = builder.reset().add_name("Juan no Pérez").build()
print(perfil_parcial)
print("¿Válido?", perfil_parcial.is_valid())

perfil_vacio = builder.reset().build()
print(perfil_vacio)
print("¿Válido?", perfil_vacio.is_valid())

