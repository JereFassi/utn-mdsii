from notifier import Notifier
from decorators import EmailDecorator, SMSDecorator, SlackDecorator

def test_decorator_compone_canales():
    base = Notifier()
    multi = SlackDecorator(SMSDecorator(EmailDecorator(base)))
    res = multi.send("Hola equipo")
    assert "canal=Email" in res and "canal=SMS" in res and "canal=Slack" in res

def test_decorator_cambia_orden():
    base = Notifier()
    multi = EmailDecorator(SlackDecorator(SMSDecorator(base)))
    res = multi.send("Hola equipo")
    # Debe contener los tres canales sin importar el orden
    for canal in ("Email", "SMS", "Slack"):
        assert f"canal={canal}" in res
