"""
Clase 4 — Patrones Creacionales
Ejemplo: Singleton (Python)
--------------------------------
Garantiza una única instancia y acceso global.
Versión simple de Logger.
"""

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creando instancia única de Logger")
            cls._instance = super(Logger, cls).__new__(cls)
            # estado interno mínimo (evitar mutabilidad global en la vida real)
            cls._instance._level = "INFO"
        return cls._instance

    def set_level(self, level: str) -> None:
        if level not in ("INFO", "DEBUG", "WARN", "ERROR"):
            raise ValueError("Nivel inválido")
        self._level = level

    def log(self, message: str) -> None:
        print(f"[{self._level}] {message}")


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    print("¿Misma instancia?", logger1 is logger2)  # True
    logger1.set_level("DEBUG")
    logger2.log("Sistema iniciado")  # Usa el mismo estado
