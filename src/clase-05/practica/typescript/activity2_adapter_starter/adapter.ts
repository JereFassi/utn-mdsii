// Interfaz objetivo
export interface NewInterface {
  request(): string;
}

// Clase existente (incompatible)
export class OldSystem {
  specificRequest(): string {
    return "<data><msg>Respuesta del sistema antiguo</msg></data> (XML → datos brutos)";
  }
}

// Adapter que traduce a la interfaz objetivo (XML → JSON simulado)
export class Adapter implements NewInterface {
  constructor(private adaptee: OldSystem) {}

  request(): string {
    const raw = this.adaptee.specificRequest();
    return raw
      .replace(" (XML → datos brutos)", " (normalizado)")
      .replace("<data><msg>", "{'msg':'")
      .replace("</msg></data>", "'}");
  }
}
