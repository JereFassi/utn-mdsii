# Clase 6 – Patrones de Comportamiento
Este paquete contiene **archivos base** (Python y TypeScript) con ejemplos y tests mínimos para:
- **Observer**
- **Strategy**
- **Command**

## Estructura
- `python/` → código y tests con `pytest`
- `typescript/` → ejemplos y tests simples (sin framework), ejecutables con `ts-node` o compilando con `tsc`

---

## Python
**Requisitos**: Python 3.10+ y `pytest`.

```bash
cd python
pytest -q
```

## TypeScript
**Requisitos**: Node 18+, TypeScript.

```bash
cd typescript
# opcional: inicializar si hace falta
npm init -y
npm i typescript ts-node -D
npx tsc --init

# ejecutar un archivo
npx ts-node observer/observer.ts
npx ts-node strategy/strategy.ts
npx ts-node command/command.ts

# "tests" simples
npx ts-node observer/test_observer.ts
npx ts-node strategy/test_strategy.ts
npx ts-node command/test_command.ts
```

> Nota: Los tests en TypeScript son verificaciones básicas sin framework, pensados para validar rápidamente el flujo.
