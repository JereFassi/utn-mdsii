from __future__ import annotations

# Componente base
class Notifier:
    def send(self, message: str) -> str:
        return f"Enviando: {message}"

# Decorador base
class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, message: str) -> str:
        return self._notifier.send(message)

# Decoradores concretos
class EmailDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        base = super().send(message)
        return f"{base} | canal=Email"

class SMSDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        base = super().send(message)
        return f"{base} | canal=SMS"

class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        base = super().send(message)
        return f"{base} | canal=Slack"

def main():
    base = Notifier()
    multi = SlackDecorator(SMSDecorator(EmailDecorator(base)))
    print(multi.send("Hola equipo"))

if __name__ == "__main__":
    main()
