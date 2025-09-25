import { Notifier } from "./notifier";

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
