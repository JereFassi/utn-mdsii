export class SubsystemA {
  connect(): string {
    return "A: conexión establecida";
  }
  query(q: string): string {
    return `A: ejecutando '${q}'`;
  }
  close(): string {
    return "A: conexión cerrada";
  }
}

export class SubsystemB {
  init(): string {
    return "B: inicializado";
  }
  process(data: string): string {
    return `B: procesando [${data}]`;
  }
  shutdown(): string {
    return "B: apagado";
  }
}

export class SystemFacade {
  private a = new SubsystemA();
  private b = new SubsystemB();

  runWorkflow(query: string): string {
    const steps = [
      this.a.connect(),
      this.b.init(),
      this.a.query(query),
      this.b.process("resultado intermedio"),
      this.b.shutdown(),
      this.a.close(),
    ];
    return steps.join(" | ");
  }
}

if (require.main === module) {
  const facade = new SystemFacade();
  // eslint-disable-next-line no-console
  console.log(facade.runWorkflow("SELECT * FROM users"));
}
