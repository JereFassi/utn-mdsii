// Componente
export interface INotifier {
  send(message: string): string;
}

// Componente concreto
export class Notifier implements INotifier {
  send(message: string): string {
    return `Enviando: ${message}`;
  }
}

// Decorador base
export class NotifierDecorator implements INotifier {
  constructor(protected readonly notifier: INotifier) {}

  send(message: string): string {
    return this.notifier.send(message);
  }
}

// Decoradores concretos
export class EmailDecorator extends NotifierDecorator {
  send(message: string): string {
    return `${super.send(message)} | canal=Email`;
  }
}

export class SMSDecorator extends NotifierDecorator {
  send(message: string): string {
    return `${super.send(message)} | canal=SMS`;
  }
}

export class SlackDecorator extends NotifierDecorator {
  send(message: string): string {
    return `${super.send(message)} | canal=Slack`;
  }
}

if (require.main === module) {
  const base = new Notifier();
  const multi = new SlackDecorator(new SMSDecorator(new EmailDecorator(base)));
  // eslint-disable-next-line no-console
  console.log(multi.send("Hola equipo"));
}
