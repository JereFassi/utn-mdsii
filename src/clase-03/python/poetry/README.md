# Python – Poetry

## 1) Instalar Poetry (según SO)

https://python-poetry.org/docs/#installation

## 2) Inicializar (si fuera desde cero)

```bash
poetry init
```

## 3) Instalar dependencias del proyecto

```bash
poetry install
```

## 4) Agregar dependencias - No es necesario si ya están en el pyproject.toml

```bash
poetry add flask
poetry add --group dev pytest black flake8
```

## 5) Ejecutar app

```bash
poetry run python app_poetry.py
# -> http://localhost:5000/
```

## 6) Tests

```bash
poetry run pytest -q
```
