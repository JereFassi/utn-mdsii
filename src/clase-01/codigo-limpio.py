# Ejemplo de código limpio en Python

TAX_RATES = {
    "standard": 0.21,
    "reduced": 0.105,
    "intermediate": 0.15
}

def calculate_total_tax(prices, tax_type="standard"):
    """Calcula el impuesto total para una lista de precios según el tipo de tasa."""
    if tax_type not in TAX_RATES:
        raise ValueError(f"Tipo de tasa inválido: {tax_type}")

    rate = TAX_RATES[tax_type]

    total_tax = 0
    for price in prices:
        total_tax += price * rate

    return total_tax

# Ejemplo de uso:
# total = calculate_total_tax([100, 200, 300], tax_type="standard")