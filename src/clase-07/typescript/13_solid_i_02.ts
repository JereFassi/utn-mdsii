// Después: interfaces separadas
interface Programador {
  programar(): void;
}

interface Diseñador {
  diseñar(): void;
}

interface Tester {
  testear(): void;
}

class Dev implements Programador, Tester {
  programar() {}
  testear() {}
}

class UX implements Diseñador {
  diseñar() {}
}

class QA implements Tester {
  testear() {}
}

// Cada clase implementa solo lo que necesita.
// Más fácil de mantener y extender sin afectar otras clases.
// (abierto a extensión, cerrado a modificación).

/**
 *
 * Principio: Interface Segregation Principle (ISP).
 *
 * Los clientes no deben verse obligados a depender de interfaces que no utilizan.
 * En lugar de tener una interfaz grande y monolítica, es mejor tener varias interfaces pequeñas y específicas.
 * Esto promueve la reutilización y la flexibilidad en el diseño del software.
 */
