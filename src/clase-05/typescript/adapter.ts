// Interfaz objetivo
export interface NewInterface {
  request(): string;
}

// Clase existente (incompatible)
export class OldSystem {
  specificRequest(): string {
    return "Respuesta del sistema antiguo (XML → datos brutos)";
  }
}

// Adapter: implementa la interfaz objetivo delegando en OldSystem
export class Adapter implements NewInterface {
  constructor(private adaptee: OldSystem) {}

  request(): string {
    const raw = this.adaptee.specificRequest();
    const normalized = raw.replace(" (XML → datos brutos)", " (normalizado)");
    return normalized;
  }
}

// Demo
if (require.main === module) {
  const oldSys = new OldSystem();
  const adapter = new Adapter(oldSys);
  // eslint-disable-next-line no-console
  console.log(adapter.request());
}
