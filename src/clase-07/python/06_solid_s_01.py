# Antes: clase con demasiadas responsabilidades
class Reporte:
    def __init__(self, ventas):
        self.ventas = ventas

    def calcular_total(self):
        return sum(v.monto for v in self.ventas)

    def exportar_csv(self):
        with open("reporte.csv", "w") as f:
            for v in self.ventas:
                f.write(f"{v.fecha},{v.monto}\n")
