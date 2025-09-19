from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Notification:
    subject: str
    body: str
    # recipients: mapping channel -> list of destination addresses/ids
    recipients: Dict[str, List[str]] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)


# Componente base
class Notifier:
    def send(self, notification: Notification) -> str:
        # Aquí podría ir la lógica de auditoría central, persistencia, etc.
        return f"Dispatch iniciado: subject='{notification.subject}'"


# Decorador base
class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, notification: Notification) -> str:
        return self._notifier.send(notification)

def _validate_email(addr: str) -> bool:
    return "@" in addr and "." in addr.split("@")[-1]


def _validate_phone(number: str) -> bool:
    digits = [c for c in number if c.isdigit()]
    return len(digits) >= 8

def _validate_slack(channel: str) -> bool:
    return channel.startswith("#") or channel.startswith("@") or channel.startswith("C")


def _send_email(addr: str, subject: str, body: str) -> str:
    if not _validate_email(addr):
        return f"Email a '{addr}': INVALID"
    return f"Email a '{addr}': OK"


def _send_sms(number: str, body: str) -> str:
    if not _validate_phone(number):
        return f"SMS a '{number}': INVALID"
    return f"SMS a '{number}': OK"


def _send_slack(channel: str, body: str) -> str:
    if not _validate_slack(channel):
        return f"Slack '{channel}': INVALID"
    return f"Slack '{channel}': OK"


# Decoradores concretos
class EmailDecorator(NotifierDecorator):
    def send(self, notification: Notification) -> str:
        base_log = super().send(notification)

        results = []
        for addr in notification.recipients.get("email", []):
            res = _send_email(addr, notification.subject, notification.body)
            results.append(res)

        if not results:
            results.append("Email: SKIPPED (sin destinatarios)")

        return f"{base_log} | " + " | ".join(results)


class SMSDecorator(NotifierDecorator):
    def send(self, notification: Notification) -> str:
        base_log = super().send(notification)

        results = []
        for num in notification.recipients.get("sms", []):
            res = _send_sms(num, notification.body)
            results.append(res)

        if not results:
            results.append("SMS: SKIPPED (sin destinatarios)")

        return f"{base_log} | " + " | ".join(results)


class SlackDecorator(NotifierDecorator):
    def send(self, notification: Notification) -> str:
        base_log = super().send(notification)

        results = []
        for chan in notification.recipients.get("slack", []):
            res = _send_slack(chan, notification.body)
            results.append(res)

        if not results:
            results.append("Slack: SKIPPED (sin destinatarios)")

        return f"{base_log} | " + " | ".join(results)


def main():
    note = Notification(
        subject="Nueva versión disponible",
        body="Se liberó la versión 2.1.2. Revisar notas de la release.",
        recipients={
            "email": ["ana@example.com", "invalid-email"],
            "sms": ["+54 9 11 1234 5678"],
            "slack": ["#releases", "invalid_channel"]
        },
        metadata={"env": "staging", "severity": "info"},
    )

    core = Notifier()
    multi = SlackDecorator(SMSDecorator(EmailDecorator(core)))

    result_log = multi.send(note)
    print(result_log)


if __name__ == "__main__":
    main()
