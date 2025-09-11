export class Notifier {
  send(message: string): string {
    return `Enviando: ${message}`;
  }
}

export class NotifierDecorator extends Notifier {
  constructor(protected notifier: Notifier) {
    super();
  }

  send(message: string): string {
    return this.notifier.send(message);
  }
}

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
