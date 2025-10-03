# Antes: violación de LSP
class Ave:
    def volar(self):
        print("Volando...")

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no vuelan")

