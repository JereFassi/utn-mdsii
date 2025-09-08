"""
Clase 4 — Patrones Creacionales
Ejemplo: Factory Method (Python)
--------------------------------
Encapsula la creación de objetos. El cliente no usa 'new' directamente.
"""
from abc import ABC, abstractmethod

# Producto abstracto
class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass

# Productos concretos
class Circle(Shape):
    def draw(self) -> str:
        return "Dibujando un Círculo"

class Square(Shape):
    def draw(self) -> str:
        return "Dibujando un Cuadrado"

# Factory
class ShapeFactory:
    def create_shape(self, shape_type: str) -> Shape:
        st = shape_type.lower()
        if st == "circle":
            return Circle()
        elif st == "square":
            return Square()
        else:
            raise ValueError(f"Forma no reconocida: {shape_type}")

if __name__ == "__main__":
    factory = ShapeFactory()
    shape1 = factory.create_shape("circle")
    shape2 = factory.create_shape("square")
    print(shape1.draw())
    print(shape2.draw())
