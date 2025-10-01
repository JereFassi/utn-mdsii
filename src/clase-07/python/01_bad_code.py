def procesar_pedido(pedido):
    total = 0
    for item in pedido.items:
        total += item.precio * item.cantidad
    
    # Aplicar descuento si hay más de 5 ítems
    if len(pedido.items) > 5:
        total *= 0.9
    
    # Guardar en base de datos
    save_order(pedido, total)

    # Notificar por email
    enviar_email(pedido.cliente, total)

    return total
