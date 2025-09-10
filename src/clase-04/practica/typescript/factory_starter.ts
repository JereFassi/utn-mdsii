// Actividad 2 — Factory Method (TypeScript)
// Objetivo: Implementar una UserFactory que cree distintos tipos de usuarios.
//
// Requisitos:
// - Interfaz User con método permissions(): string[]
// - Clases concretas: AdminUser, MemberUser, GuestUser
// - Factory: createUser(kind: string): User
// - Demostración: crear usuarios y mostrar permisos

interface User {
  permissions(): string[];
}

// TODO: implementar clases concretas
// class AdminUser implements User { ... }
// class MemberUser implements User { ... }
// class GuestUser implements User { ... }

class UserFactory {
  createUser(kind: string): User {
    const k = kind.toLowerCase();
    // TODO: devolver la clase correcta según k
    // if (k === "admin") return new AdminUser();
    // if (k === "member") return new MemberUser();
    // if (k === "guest") return new GuestUser();
    throw new Error("TODO: implementar createUser");
  }
}

// Uso (descomentar al completar)
// const f = new UserFactory();
// const u1 = f.createUser("admin");
// const u2 = f.createUser("member");
// const u3 = f.createUser("guest");
// console.log(u1.permissions(), u2.permissions(), u3.permissions());
