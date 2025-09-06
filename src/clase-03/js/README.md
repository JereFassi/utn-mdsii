# JS – npm/yarn

## 1) Inicializar proyecto (opcional si ya tenés package.json)
```bash
npm init -y
# o
yarn init -y
```

## 2) Instalar dependencias
```bash
# Si ya tenés package.json
npm install
# o
yarn install

# Sino
# Producción (runtime)
npm install express
# Desarrollo (dev)
npm install -D jest eslint prettier

# Equivalente yarn:
yarn add express
yarn add -D jest eslint prettier
```

## 3) Scripts (package.json)
- `dev`: levantar servidor
- `test`: correr pruebas
- `lint`: ejemplo de lint (instalar eslint para usarlo)
- `build`: placeholder (agregar tsc/vite si hace falta)
- `start`: modo producción

## 4) Ejecución
```bash
# Usar versión de Node definida en .nvmrc (recomendado)
nvm install
nvm use

# Instalar con lockfile reproducible (CI)
npm ci
# o instalación flexible
npm install

# Levantar en dev
npm run dev

# Tests
npm test
```