// Antes: una interfaz enorme
interface Trabajador {
  programar(): void;
  diseñar(): void;
  testear(): void;
}

class Programador implements Trabajador {
  programar() {}
  diseñar() {
    throw new Error("No implementado");
  }
  testear() {
    throw new Error("No implementado");
  }
}
