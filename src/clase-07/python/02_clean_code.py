def calcular_total(pedido):
    return sum(item.precio * item.cantidad for item in pedido.items)

def aplicar_descuento(total, pedido):
    return total * 0.9 if len(pedido.items) > 5 else total

def guardar_pedido(pedido, total):
    save_order(pedido, total)

def notificar_cliente(cliente, total):
    enviar_email(cliente, total)

def procesar_pedido(pedido):
    total = calcular_total(pedido)
    total = aplicar_descuento(total, pedido)
    guardar_pedido(pedido, total)
    notificar_cliente(pedido.cliente, total)
    return total
