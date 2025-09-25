import { Notifier } from "../notifier";
import { EmailDecorator, SMSDecorator, SlackDecorator } from "../decorators";

test("Decorator compone múltiples canales", () => {
  const base = new Notifier();
  const multi = new SlackDecorator(new SMSDecorator(new EmailDecorator(base)));
  const res = multi.send("Hola equipo");
  expect(res).toContain("canal=Email");
  expect(res).toContain("canal=SMS");
  expect(res).toContain("canal=Slack");
});

test("Decorator en otro orden sigue agregando todos los canales", () => {
  const base = new Notifier();
  const multi = new EmailDecorator(new SlackDecorator(new SMSDecorator(base)));
  const res = multi.send("Hola equipo");
  ["Email", "SMS", "Slack"].forEach(c => expect(res).toContain(`canal=${c}`));
});
