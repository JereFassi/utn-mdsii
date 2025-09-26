import builtins
from python.observer.observer import Stock, EmailAlert, Dashboard

def test_observer_notify(monkeypatch, capsys):
    s = Stock()
    e = EmailAlert()
    d = Dashboard()
    s.subscribe(e)
    s.subscribe(d)

    s.set_price(10.5)
    out = capsys.readouterr().out
    assert "[Email] Nuevo precio: 10.5" in out
    assert "[Dashboard] Precio actualizado: 10.5" in out

def test_unsubscribe(monkeypatch, capsys):
    s = Stock()
    e = EmailAlert()
    s.subscribe(e)
    s.unsubscribe(e)

    s.set_price(99.9)
    out = capsys.readouterr().out
    assert out.strip() == ""
