"""
Actividad 1 — Singleton (Python)
Objetivo: Implementar un Logger como Singleton.

Requisitos:
- Debe garantizar UNA instancia global.
- Método set_level(...) con niveles: INFO, DEBUG, WARN, ERROR.
- Método log(msg) que imprima: [NIVEL] mensaje
- Demostración: crear dos referencias y comprobar que apuntan a la misma instancia.
"""

class Logger:
    _instance = None  # TODO: usar para guardar la única instancia

    def __new__(cls):
        # TODO: implementar patrón Singleton aquí
        return super().__new__(cls)

    def __init__(self):
        # TODO: inicializar nivel por defecto (INFO) solo la primera vez
        pass

    def set_level(self, level: str) -> None:
        # TODO: validar y setear el nivel
        pass

    def log(self, message: str) -> None:
        # TODO: imprimir con el formato [NIVEL] mensaje
        pass


if __name__ == "__main__":
    # TODO: crear 2 referencias al Logger y demostrar que son la misma instancia
    # TODO: cambiar el nivel en una referencia y loguear desde la otra
    pass
