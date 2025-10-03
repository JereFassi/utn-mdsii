// Antes: dependencia concreta
class Notificador {
  private mailer = new SESMailer();
  enviar(to: string, msg: string) {
    this.mailer.send(to, msg);
  }
}
