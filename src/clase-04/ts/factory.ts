// Clase 4 — Patrones Creacionales
// Ejemplo: Factory Method (TypeScript)
// ------------------------------------

// Producto abstracto
interface Shape {
  draw(): string;
}

// Productos concretos
class Circle implements Shape {
  draw(): string {
    return "Dibujando un Círculo";
  }
}

class Square implements Shape {
  draw(): string {
    return "Dibujando un Cuadrado";
  }
}

// Factory
class ShapeFactory {
  createShape(type: string): Shape {
    const t = type.toLowerCase();
    if (t === "circle") return new Circle();
    if (t === "square") return new Square();
    throw new Error(`Forma no reconocida: ${type}`);
  }
}

// Uso
const factory = new ShapeFactory();
const shape1 = factory.createShape("circle");
const shape2 = factory.createShape("square");
console.log(shape1.draw());
console.log(shape2.draw());
