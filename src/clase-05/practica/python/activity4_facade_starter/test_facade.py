from facade import SystemFacade

def test_facade_start_and_shutdown():
    f = SystemFacade()
    start = f.start_app("alice")
    assert start.startswith("Logger: activo") and "DB: conexión establecida" in start
    assert start.endswith("Logger: Sistema inicializado")
    stop = f.shutdown()
    assert stop == "Logger: detenido | Auth: apagado | DB: conexión cerrada"
