# Actividad 2 – Adapter (Starter + Tests)

## Objetivo
Adaptar `OldSystem` hacia la interfaz objetivo `NewInterface` para entregar datos normalizados (simular XML → JSON).

## Ejecutar tests
```bash
python -m pip install -U pytest
pytest -q
```

## Tarea
Completá/validá `Adapter.request()` para que convierta la salida de:
`<data><msg>Respuesta del sistema antiguo</msg></data> (XML → datos brutos)`
a algo que termine con `(normalizado)` y simule JSON: `{'msg':'Respuesta del sistema antiguo'}`.
