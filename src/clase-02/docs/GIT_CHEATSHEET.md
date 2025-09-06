# Git Cheatsheet — Clase 2

## Configuración inicial

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "tu@email.com"
```

## Ciclo básico

```bash
git init
git status
git add <archivo>      # o 'git add .' para agregar todo
git commit -m "mensaje descriptivo"
```

## Ramas y merges

```bash
git branch
git checkout -b feature/nueva-funcionalidad
git checkout main
git merge feature/nueva-funcionalidad
```

## Remoto

```bash
git remote add origin https://github.com/USUARIO/REPO.git
git branch -M main
git push -u origin main
git pull origin main
```

## Tags (versiones)

```bash
# Tag anotado (recomendado)
git tag -a v1.0.0 -m "Primera release"
git push origin v1.0.0

# Listar tags y ver detalle
git tag
git show v1.0.0
```
