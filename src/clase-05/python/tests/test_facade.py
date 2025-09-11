import facade

def test_facade_workflow_sequence():
    f = facade.SystemFacade()
    out = f.run_workflow("SELECT 1")
    assert out.startswith("A: conexión establecida") and out.endswith("A: conexión cerrada")
