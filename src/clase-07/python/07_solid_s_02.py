# Después: responsabilidades separadas
class Reporte:
    def __init__(self, ventas):
        self.ventas = ventas

    def calcular_total(self):
        return sum(v.monto for v in self.ventas)

class ExportadorCSV:
    def exportar(self, ventas):
        with open("reporte.csv", "w") as f:
            for v in ventas:
                f.write(f"{v.fecha},{v.monto}\n")

# Cada clase tiene una única responsabilidad.
# Más fácil de mantener, probar y extender.

# Cumple con SRP: cambios en exportación no afectan cálculo.