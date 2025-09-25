from subsystems import Database, Auth, Logger

class SystemFacade:
    def __init__(self):
        self.db = Database()
        self.auth = Auth()
        self.logger = Logger()

    def start_app(self, user: str) -> str:
        steps = [
            self.logger.start(),
            self.db.connect(),
            self.auth.init(),
            self.auth.login(user),
            self.db.query("SELECT 1"),
            self.logger.log("Sistema inicializado"),
        ]
        return " | ".join(steps)

    def shutdown(self) -> str:
        steps = [
            self.logger.stop(),
            self.auth.shutdown(),
            self.db.close(),
        ]
        return " | ".join(steps)
