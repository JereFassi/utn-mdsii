from abc import ABC, abstractmethod
from typing import List

class User(ABC):

    @abstractmethod
    def permissions(self) -> List[str]:
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"

class AdminUser(User):
    def permissions(self) -> List[str]:
        return ["read", "write", "delete", "manage_users"]

class MemberUser(User):
    def permissions(self) -> List[str]:
        return ["read", "write"]

class GuestUser(User):
    def permissions(self) -> List[str]:
        return ["read"]

class UserFactory:
    def create_user(self, user_type: str) -> User:
        t = user_type.strip().lower()
        if t == "admin":
            return AdminUser()
        elif t == "member":
            return MemberUser()
        elif t in ("guest", "visitor"):
            return GuestUser()
        else:
            raise ValueError(f"Tipo de usuario no reconocido: {user_type}")
        
factory = UserFactory()
for type in ("admin", "member", "guest"):
    user = factory.create_user(type)
    print(f"{user!r} -> permisos: {user.permissions()}")

try:
    factory.create_user("unknown")
except ValueError as e:
    print("Error esperado al pedir tipo desconocido:", e)