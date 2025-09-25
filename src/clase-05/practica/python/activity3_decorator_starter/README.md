# Actividad 3 – Decorator (Starter + Tests)

## Objetivo
Agregar canales dinámicamente a `Notifier` mediante decoradores (Email, SMS, Slack).

## Ejecutar tests
```bash
python -m pip install -U pytest
pytest -q
```

## Tarea
Componer decoradores en distinto orden y verificar que se agreguen sufijos:
`| canal=Email`, `| canal=SMS`, `| canal=Slack`.
