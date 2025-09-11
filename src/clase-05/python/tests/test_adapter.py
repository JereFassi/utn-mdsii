import adapter

def test_adapter_translates_interface():
    old = adapter.OldSystem()
    ad = adapter.Adapter(old)
    assert ad.request().endswith("(normalizado)")
