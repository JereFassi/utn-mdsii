import { Database, Auth, Logger } from "./subsystems";

export class SystemFacade {
  private db = new Database();
  private auth = new Auth();
  private logger = new Logger();

  startApp(user: string): string {
    const steps = [
      this.logger.start(),
      this.db.connect(),
      this.auth.init(),
      this.auth.login(user),
      this.db.query("SELECT 1"),
      this.logger.log("Sistema inicializado"),
    ];
    return steps.join(" | ");
  }

  shutdown(): string {
    const steps = [
      this.logger.stop(),
      this.auth.shutdown(),
      this.db.close(),
    ];
    return steps.join(" | ");
  }
}
