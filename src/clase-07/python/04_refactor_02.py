# Paso 1 — Refactor: usar sum con comprensión
def calcular_total(items):
    return sum(item.precio * item.cantidad for item in items)

# Cambio pequeño: más conciso, sin alterar comportamiento.
# Tests pasan: confirmación de que no se rompió nada.