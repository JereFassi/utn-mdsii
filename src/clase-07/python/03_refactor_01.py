def calcular_total(items):
    total = 0
    for item in items:
        total += item.precio * item.cantidad
    return total
