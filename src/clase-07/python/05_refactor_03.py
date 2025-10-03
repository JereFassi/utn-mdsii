# Paso 2 — Refactor: delegar lógica a la clase Item

class Item:
    def __init__(self, precio, cantidad):
        self.precio = precio
        self.cantidad = cantidad
    
    def subtotal(self):
        return self.precio * self.cantidad

def calcular_total(items):
    return sum(item.subtotal() for item in items)

# Ahora la lógica está donde corresponde (responsabilidad de Item).
# Código más fácil de mantener y extender.