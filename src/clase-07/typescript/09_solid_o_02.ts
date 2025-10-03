// Después: polimorfismo (abierto a extensión)
interface ReglaPrecio {
  calcular(monto: number): number;
}

class Normal implements ReglaPrecio {
  calcular(monto: number) {
    return monto;
  }
}
class BlackFriday implements ReglaPrecio {
  calcular(monto: number) {
    return monto * 0.8;
  }
}
class Navidad implements ReglaPrecio {
  calcular(monto: number) {
    return monto * 0.7;
  }
}

function calcularPrecio(regla: ReglaPrecio, monto: number): number {
  return regla.calcular(monto);
}

// Uso:
const precioNormal = calcularPrecio(new Normal(), 100);
const precioBF = calcularPrecio(new BlackFriday(), 100);
const precioNavidad = calcularPrecio(new Navidad(), 100);
console.log(precioNormal, precioBF, precioNavidad);

// Más fácil agregar nuevas reglas sin modificar código existente
// (abierto a extensión, cerrado a modificación).

/**
 *
 * Principio: Interface Segregation Principle (ISP).
 *
 * Los clientes no deben verse obligados a depender de interfaces que no utilizan.
 * En lugar de tener una interfaz grande y monolítica, es mejor tener varias interfaces pequeñas y específicas.
 * Esto promueve la reutilización y la flexibilidad en el diseño del software.
 */
