from notifier import Notifier

class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, message: str) -> str:
        return self._notifier.send(message)

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
