# Clase 12 – GitHub Actions CI

Este módulo contiene un flujo de integración continua de ejemplo para los ejercicios de la materia. El objetivo es mostrar una configuración mínima de **GitHub Actions** que ejecute linters y tests de un proyecto Python en cada `push` o `pull_request`.

## Contenido

```
src/clase-12/
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## ¿Qué hace el workflow?

Archivo: `.github/workflows/ci.yml`

- Dispara la CI en `push` a `main` o `develop`, y en cualquier Pull Request.
- Ejecuta un único job (`tests`) sobre `ubuntu-latest`.
- Instala Python 3.11 y actualiza `pip`.
- Instala dependencias del proyecto (si existe `requirements.txt`) más `pytest` y `flake8`.
- Corre `flake8 src` para validar estilo y convenciones.
- Ejecución de `pytest -q` para asegurar que la suite pasa antes de mergear.

> Si tu código vive fuera de `src/`, ajusta las rutas de `flake8` y `pytest` para que apunten al directorio correcto.

## Cómo usarlo en tu repo

1. Crea tu código y tests dentro de `src/` (o ajusta la ruta en el workflow).
2. Define las dependencias en `requirements.txt` para que `pip install -r requirements.txt` funcione.
3. Conmita el workflow dentro del directorio `.github/workflows/` del repositorio.
4. Abrí un Pull Request o hacé push a `main`/`develop`: GitHub Actions se ejecutará automáticamente.

## Reproducir localmente

```bash
python -m venv .venv
source .venv/bin/activate   # .venv\Scripts\activate en Windows
pip install --upgrade pip
pip install -r requirements.txt  # opcional, si existe
pip install pytest flake8
flake8 src
pytest -q
```

Recomendaciones:

- Agregá un archivo `setup.cfg` o `.flake8` si necesitás reglas personalizadas de lint.
- Si tu proyecto requiere otra versión de Python, cambiá la clave `python-version` del workflow.
- Para proyectos grandes, considerá agregar cache de dependencias (`actions/cache`) o jobs paralelos (lint y tests separados).

Con este workflow tenés la validación básica automatizada y se facilita el control de calidad en las entregas de la materia.
