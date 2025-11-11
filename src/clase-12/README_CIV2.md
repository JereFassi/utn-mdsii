# CI Unificado (Node.js) – README_CIV2

Este workflow (`.github/workflows/ci_v2.yml`) muestra una canalización completa para proyectos Node.js/TypeScript: se ejecuta en cada `push` a `main` o `develop`, y en todo `pull_request`. Además, aplica cancelación de ejecuciones en paralelo mediante `concurrency` para ahorrar minutos.

## Estructura

```
src/clase-12/
├── README.md             # Workflow Python (ci.yml)
├── README_CIV2.md        # Este archivo
└── .github/workflows/
    ├── ci.yml
    └── ci_v2.yml         # Workflow Node.js
```

## Resumen del pipeline

- **Trigger**: `push` (main/develop) y `pull_request`.
- **Concurrency**: evita ejecutar múltiples CI en la misma rama (`ci-${{ github.ref }}`) cancelando la anterior.
- **Permissions**: `contents: read` + `pull-requests: write` (por si alguna acción anota comentarios).
- **Jobs**:
  - `quality-and-tests` (Ubuntu):
    1. Checkout del repo.
    2. Setup de Node 20 con cache `npm`.
    3. `npm ci` para instalar dependencias bloqueadas por `package-lock.json`.
    4. `npm run lint` para reglas ESLint.
    5. `npm run format:check` para validar Prettier sin modificar archivos.
    6. `npm test -- --coverage` para ejecutar la suite y generar `coverage/lcov.info`.
    7. `npm run build` para comprobar que la app compila/empaca.
    8. `actions/upload-artifact` publica `coverage/lcov.info` (incluso si hay fallos previos, gracias al `if: always()`).
  - `sonar` (opcional): solo se ejecuta si existe el `secret` `SONAR_TOKEN` y el evento no es `pull_request_target`. Descarga el artefacto de cobertura, prepara Java 17 y lanza `SonarSource/sonarcloud-github-action`.

## Requisitos del repo

- `package.json` con scripts:
  ```json
  {
    "scripts": {
      "lint": "eslint .",
      "format:check": "prettier --check .",
      "test": "jest",
      "build": "tsc -p tsconfig.build.json"
    }
  }
  ```
  Ajusta los comandos a tus herramientas reales (Vitest, Playwright, etc.).
- `package-lock.json` para aprovechar `npm ci`.
- `coverage/lcov.info` debe generarse con el comando de tests (Jest, Vitest, etc.).
- Variables de entorno/secretos:
  - `SONAR_TOKEN` (solo si vas a usar el job `sonar`).
  - `SONAR_PROJECT_KEY` y `SONAR_ORGANIZATION` pueden configurarse como secretos o `env` para evitar hardcodear valores en `ci_v2.yml`.

## Cómo usarlo

1. Copiá `ci_v2.yml` al directorio `.github/workflows/` de tu repo.
2. Revisa el `node-version`, comandos npm y rutas antes de hacer commit.
3. Configurá `SONAR_TOKEN` en GitHub → Settings → Secrets (opcional).
4. Hacé push o abrí un PR; la canalización se activará automáticamente.

## Reproducción local

```bash
npm ci
npm run lint
npm run format:check
npm test -- --coverage
npm run build
```

Si necesitás el análisis de SonarCloud local, instalá el scanner CLI o usá `sonar-scanner` con los mismos parámetros (`sonar.javascript.lcov.reportPaths=coverage/lcov.info`).

## Ajustes recomendados

- Agregar `actions/cache` por workspace adicional (por ejemplo, `.next/cache` o `~/.pnpm-store` si cambiás a pnpm).
- Usar matrices (`strategy.matrix`) cuando quieras validar múltiples versiones de Node.
- Añadir más artefactos (por ejemplo, `npm run build` → carpeta `dist/`) para facilitar depuración.
- Separar jobs (lint, tests, build) si necesitás ejecutar en paralelo o reutilizar resultados.

Con esta configuración cubrís linting, formateo, tests con cobertura, build y análisis estático, logrando un pipeline completo listo para proyectos Node en la materia.
