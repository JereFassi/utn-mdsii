# Clase 2 — Git & GitHub (Material para Alumnos)

Este repositorio contiene ejemplos mínimos y una estructura sugerida para iniciar proyectos con Git.

## Estructura

```
/docs
/src
  /python
  /node
README.md
```

## Objetivos

- Practicar comandos básicos de Git (init, add, commit, branch, merge, push, pull, tag).
- Crear un repositorio remoto en GitHub y conectar el repositorio local.
- Aplicar versionado semántico con tags (vX.Y.Z).

## Pasos rápidos

1. Inicializar repo local:

   ```bash
   git init
   git add .
   git commit -m "Proyecto base: estructura y ejemplos"
   ```

2. Conectar a GitHub (reemplazar `USUARIO` y `NOMBRE_REPO`):

   ```bash
   git remote add origin https://github.com/USUARIO/NOMBRE_REPO.git
   git branch -M main
   git push -u origin main
   ```

3. Crear una rama de feature:

   ```bash
   git checkout -b feature/ejemplo
   # (hacer cambios, commits...)
   git push -u origin feature/ejemplo
   ```

4. Al cerrar el sprint (merge develop -> main), crear un tag de release:
   ```bash
   git checkout main
   git pull origin main
   git merge develop
   git tag -a v1.0.0 -m "Release inicial"
   git push origin main
   git push origin v1.0.0
   ```
