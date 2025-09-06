# Python – pip + venv

## 1) Crear entorno virtual
```bash
python3 -m venv venv

# Activar (Linux/Mac)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate
```

## 2) Instalar dependencias
```bash
pip install -r requirements.txt
```

## 3) Ejecutar app Flask
```bash
python app.py
# -> http://localhost:5000/
```

## 4) Correr tests
```bash
pytest -q
```

> `venv/` no se incluye; se crea localmente.