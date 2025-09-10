// Actividad 1 — Singleton (TypeScript)
// Objetivo: Implementar un Logger como Singleton.
//
// Requisitos:
// - ÚNICA instancia global (propiedad estática + constructor privado)
// - setLevel(level) con niveles: INFO | DEBUG | WARN | ERROR
// - log(message): imprime `[NIVEL] mensaje`
// - Demostración: dos referencias apuntan a la misma instancia

type Level = "INFO" | "DEBUG" | "WARN" | "ERROR";

class Logger {
  // TODO: propiedad estática para guardar la instancia
  // private static instance: Logger;

  // TODO: estado interno (nivel actual)
  // private level: Level = "INFO";

  // TODO: constructor privado
  // private constructor() {}

  static getInstance(): Logger {
    // TODO: crear y/o devolver la única instancia
    throw new Error("TODO: implementar getInstance()");
  }

  setLevel(level: Level): void {
    // TODO: validar y setear el nivel
  }

  log(message: string): void {
    // TODO: imprimir formato [NIVEL] mensaje
  }
}

// Uso de ejemplo (descomentar al completar)
// const l1 = Logger.getInstance();
// const l2 = Logger.getInstance();
// console.log("¿Misma instancia?", l1 === l2);
// l1.setLevel("DEBUG");
// l2.log("Sistema iniciado");
