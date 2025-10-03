// Después: dependencia invertida
interface Mailer {
  send(to: string, msg: string): void;
}

class SESMailer implements Mailer {
  send(to: string, msg: string) {
    /* ... */
  }
}
class ConsoleMailer implements Mailer {
  send(to: string, msg: string) {
    console.log(msg);
  }
}

class Notificador {
  constructor(private mailer: Mailer) {}
  enviar(to: string, msg: string) {
    this.mailer.send(to, msg);
  }
}

// Uso:
const notificador = new Notificador(new ConsoleMailer());
notificador.enviar(
  "destinatario@example.com",
  "Hola, este es un mensaje de prueba."
);

// Ahora Notificador depende de la abstracción Mailer, no de una implementación concreta.
// Más fácil cambiar la implementación de envío sin modificar Notificador.
// (abierto a extensión, cerrado a modificación).

/**
 *
 * Principio: Dependency Inversion Principle (DIP).
 * Modulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
 *
 * Tipos de dependencias
 *
 * 12_solid_i_01.ts: Notificador crea y depende de SESMailer (clase concreta).
 * 13_solid_i_02.ts: Notificador depende de Mailer (interfaz/abstracción).
 * Acoplamiento
 *
 * 12: Acoplamiento estrecho a SESMailer. Cualquier cambio o intercambio requiere editar Notificador.
 * 13: Acoplamiento débil. Cualquier implementación de Mailer (SESMailer, ConsoleMailer, mocks) puede ser inyectada.
 * Construcción
 *
 * 12: Dependencia oculta creada dentro de la clase (new SESMailer()).
 * 13: Inyección de dependencias a través del constructor (constructor(private mailer: Mailer)).
 * Extensibilidad (OCP)
 *
 * 12: Viola el principio OCP; agregar un nuevo mailer necesita modificar Notificador.
 * 13: Abierto a extensión; agregar una nueva implementación de Mailer sin cambiar Notificador.
 * Testabilidad
 *
 * 12: Difícil de probar; necesita el verdadero SESMailer.
 * 13: Fácil de probar; pasa un Mailer falso/simulado.
 * Abstracciones vs detalles
 *
 * 12: Notificador de alto nivel depende de un detalle de bajo nivel (SESMailer).
 * 13: Tanto Notificador como las implementaciones dependen de la abstracción Mailer, satisfaciendo el principio DIP.
 */
