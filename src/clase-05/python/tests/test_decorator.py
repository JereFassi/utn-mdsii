import decorator

def test_decorator_composes_channels():
    base = decorator.Notifier()
    multi = decorator.SlackDecorator(decorator.SMSDecorator(decorator.EmailDecorator(base)))
    result = multi.send("Hola equipo")
    assert "canal=Email" in result and "canal=SMS" in result and "canal=Slack" in result
