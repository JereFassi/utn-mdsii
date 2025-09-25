# Actividad 4 – Facade (Starter + Tests)

## Objetivo
Crear una **Fachada** que oculte la complejidad de varios subsistemas y exponga `start_app()` y `shutdown()`.

## Ejecutar tests
```bash
python -m pip install -U pytest
pytest -q
```

## Tarea
Completar/validar `SystemFacade` para orquestar `Database`, `Auth` y `Logger`.
