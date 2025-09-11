import { Notifier, EmailDecorator, SMSDecorator, SlackDecorator } from "../decorator";

test("Decorator compone múltiples canales", () => {
  const base = new Notifier();
  const multi = new SlackDecorator(new SMSDecorator(new EmailDecorator(base)));
  const res = multi.send("Hola equipo");
  expect(res).toContain("canal=Email");
  expect(res).toContain("canal=SMS");
  expect(res).toContain("canal=Slack");
});
