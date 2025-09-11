from __future__ import annotations

class SubsystemA:
    def connect(self) -> str:
        return "A: conexión establecida"
    def query(self, q: str) -> str:
        return f"A: ejecutando '{q}'"
    def close(self) -> str:
        return "A: conexión cerrada"

class SubsystemB:
    def init(self) -> str:
        return "B: inicializado"
    def process(self, data: str) -> str:
        return f"B: procesando [{data}]"
    def shutdown(self) -> str:
        return "B: apagado"

# Facade: interfaz simple que orquesta los subsistemas
class SystemFacade:
    def __init__(self):
        self.a = SubsystemA()
        self.b = SubsystemB()

    def run_workflow(self, query: str) -> str:
        steps = [
            self.a.connect(),
            self.b.init(),
            self.a.query(query),
            self.b.process("resultado intermedio"),
            self.b.shutdown(),
            self.a.close(),
        ]
        return " | ".join(steps)

def main():
    facade = SystemFacade()
    print(facade.run_workflow("SELECT * FROM users"))

if __name__ == "__main__":
    main()
