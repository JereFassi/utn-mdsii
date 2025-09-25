export class Database {
  connect(): string { return "DB: conexión establecida"; }
  query(q: string): string { return `DB: ejecutando '${q}'`; }
  close(): string { return "DB: conexión cerrada"; }
}

export class Auth {
  init(): string { return "Auth: inicializado"; }
  login(user: string): string { return `Auth: login de ${user} ok`; }
  shutdown(): string { return "Auth: apagado"; }
}

export class Logger {
  start(): string { return "Logger: activo"; }
  log(msg: string): string { return `Logger: ${msg}`; }
  stop(): string { return "Logger: detenido"; }
}
