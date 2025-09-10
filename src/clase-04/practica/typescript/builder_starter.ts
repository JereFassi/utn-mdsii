// Actividad 3 — Builder (TypeScript)
// Objetivo: Construir un UserProfile paso a paso (method chaining).
//
// Requisitos:
// - Clase UserProfile con campos opcionales: name, age, address, preferences: string[]
// - Builder: UserProfileBuilder con métodos addName, addAge, addAddress, addPreference
// - build() devuelve UserProfile
// - Demostración: construir perfiles completos y parciales

class UserProfile {
  name?: string;
  age?: number;
  address?: string;
  preferences: string[] = [];

  toString(): string {
    return `UserProfile(name=${this.name}, age=${this.age}, address=${this.address}, preferences=[${this.preferences.join(", ")}])`;
  }
}

class UserProfileBuilder {
  // TODO: guardar instancia en construcción
  // private profile: UserProfile;

  constructor() {
    // TODO: inicializar
  }

  addName(name: string): this {
    // TODO
    return this;
  }

  addAge(age: number): this {
    // TODO
    return this;
  }

  addAddress(address: string): this {
    // TODO
    return this;
  }

  addPreference(pref: string): this {
    // TODO
    return this;
  }

  build(): UserProfile {
    // TODO: devolver el objeto final
    throw new Error("TODO: implementar build()");
  }
}

// Uso (descomentar al completar)
// const b = new UserProfileBuilder();
// const p1 = b.addName("Ana").addAge(21).addPreference("dark-mode").build();
// console.log(p1.toString());
