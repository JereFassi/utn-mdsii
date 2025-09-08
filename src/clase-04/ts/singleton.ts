// Clase 4 — Patrones Creacionales
// Ejemplo: Singleton (TypeScript)
// --------------------------------
// Garantiza una única instancia y acceso global (Logger).

class Logger {
  private static instance: Logger;
  private level: "INFO" | "DEBUG" | "WARN" | "ERROR" = "INFO";

  private constructor() {
    console.log("Creando instancia única de Logger");
  }

  public static getInstance(): Logger {
    if (!Logger.instance) {
      Logger.instance = new Logger();
    }
    return Logger.instance;
  }

  public setLevel(level: "INFO" | "DEBUG" | "WARN" | "ERROR"): void {
    this.level = level;
  }

  public log(message: string): void {
    console.log(`[${this.level}] ${message}`);
  }
}

// Uso (ejecutar con ts-node o compilar a JS)
const logger1 = Logger.getInstance();
const logger2 = Logger.getInstance();
console.log("¿Misma instancia?", logger1 === logger2); // true
logger1.setLevel("DEBUG");
logger2.log("Sistema iniciado");
