from adapter import Adapter
from old_system import OldSystem

def test_adapter_normaliza_salida():
    ad = Adapter(OldSystem())
    out = ad.request()
    assert out.endswith("(normalizado)")
    assert "{'msg':'Respuesta del sistema antiguo'}" in out
