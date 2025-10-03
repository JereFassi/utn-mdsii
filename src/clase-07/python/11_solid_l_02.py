# Después: interfaces separadas
class Ave: pass

class AveVoladora(Ave):
    def volar(self):
        print("Volando...")

class Pinguino(Ave):
    def nadar(self):
        print("Nadando...")

# Cumple con LSP: Pinguino no hereda métodos que no usa.
# Más claro, fácil de mantener y extender.
# Cada clase tiene comportamientos apropiados.
