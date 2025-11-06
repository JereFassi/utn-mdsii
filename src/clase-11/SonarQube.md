### Implementación práctica: agregar SonarQube al proyecto

---

#### 🔹 Paso 1: Instalar SonarQube localmente con Docker

La forma más simple de ejecutar SonarQube en desarrollo es mediante Docker.
Ejemplo de **`docker-compose.yml`**:

```yaml
version: "3.9"
services:
  sonarqube:
    image: sonarqube:community
    container_name: sonarqube
    ports:
      - "9000:9000"
    environment:
      - SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_extensions:/opt/sonarqube/extensions

  sonardb:
    image: postgres:15
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=sonar
      - POSTGRES_DB=sonarqube
    volumes:
      - sonardb_data:/var/lib/postgresql/data

volumes:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_extensions:
  sonardb_data:
```

**Acceso:**
Luego de ejecutar `docker-compose up -d`, ingresar en `http://localhost:9000`
Usuario inicial: `admin` / Contraseña: `admin`.

---

#### 🔹 Paso 2: Crear un proyecto en SonarQube

1. Iniciar sesión en el panel web.
2. Crear un **nuevo proyecto** → elegir “manual”.
3. Asignar un nombre (por ejemplo, _ProyectoIntegrador_).
4. Generar un **token de autenticación** (se usará para el análisis).

---

#### 🔹 Paso 3: Instalar el _scanner_ en el proyecto

Para proyectos **Node.js / TypeScript**, se usa el **SonarScanner CLI** o el plugin de npm.

Opción A — CLI:

```bash
npm install -g sonar-scanner
```

Opción B — Dependencia local:

```bash
npm install sonar-scanner --save-dev
```

Verificar instalación:

```bash
npx sonar-scanner -v
```

---

#### 🔹 Paso 4: Configurar el análisis

Crear un archivo `sonar-project.properties` en la raíz del proyecto:

```properties
sonar.projectKey=proyecto-integrador
sonar.projectName=Proyecto Integrador
sonar.sourceEncoding=UTF-8
sonar.sources=src
sonar.language=ts
sonar.host.url=http://localhost:9000
sonar.login=<TOKEN_GENERADO>
sonar.exclusions=**/node_modules/**,**/tests/**
sonar.tests=tests
sonar.test.inclusions=**/*.test.ts
```

---

#### 🔹 Paso 5: Ejecutar el análisis

Desde la raíz del proyecto:

```bash
npx sonar-scanner
```

El proceso compila el código, analiza métricas y envía los resultados al servidor SonarQube.
Cuando finaliza, el panel web mostrará el proyecto con sus métricas principales (bugs, code smells, cobertura, etc.).

---

#### 🔹 Paso 6: Integración con scripts npm

Agregar un script al `package.json` para simplificar la ejecución:

```json
"scripts": {
  "analyze": "sonar-scanner"
}
```

Luego basta ejecutar:

```bash
npm run analyze
```

---

#### 🔹 Paso 7: Integración opcional con CI/CD

En entornos de integración continua (GitHub Actions, GitLab CI, etc.), puede añadirse un paso en el pipeline para ejecutar SonarQube en cada _push_ o _pull request_.

Ejemplo mínimo (GitHub Actions):

```yaml
- name: Run SonarQube analysis
  run: npx sonar-scanner \
    -Dsonar.host.url=http://sonarqube:9000 \
    -Dsonar.login=${{ secrets.SONAR_TOKEN }}
```
