class Database:
    def connect(self) -> str:
        return "DB: conexión establecida"
    def query(self, q: str) -> str:
        return f"DB: ejecutando '{q}'"
    def close(self) -> str:
        return "DB: conexión cerrada"

class Auth:
    def init(self) -> str:
        return "Auth: inicializado"
    def login(self, user: str) -> str:
        return f"Auth: login de {user} ok"
    def shutdown(self) -> str:
        return "Auth: apagado"

class Logger:
    def start(self) -> str:
        return "Logger: activo"
    def log(self, msg: str) -> str:
        return f"Logger: {msg}"
    def stop(self) -> str:
        return "Logger: detenido"
