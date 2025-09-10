"""
Actividad 2 — Factory Method (Python)
Objetivo: Implementar una UserFactory que cree distintos tipos de usuarios.

Requisitos:
- Interfaz/Clase base: User (método permissions() -> list[str])
- Clases concretas: AdminUser, MemberUser, GuestUser
- Factory: UserFactory.create_user(kind: str) -> User
- Demostración: crear usuarios y mostrar sus permisos.
"""
from abc import ABC, abstractmethod
from typing import List

class User(ABC):
    @abstractmethod
    def permissions(self) -> List[str]:
        pass

# TODO: implementar clases concretas con permisos apropiados
# class AdminUser(User): ...
# class MemberUser(User): ...
# class GuestUser(User): ...

class UserFactory:
    def create_user(self, kind: str) -> User:
        kind_lower = kind.lower()
        # TODO: devolver la clase correcta según kind_lower
        # if kind_lower == "admin": return AdminUser()
        # elif kind_lower == "member": return MemberUser()
        # elif kind_lower == "guest": return GuestUser()
        # else: raise ValueError(...)
        raise NotImplementedError("Completar la fábrica")

if __name__ == "__main__":
    # TODO: crear 'admin', 'member', 'guest' y mostrar sus permisos
    pass
