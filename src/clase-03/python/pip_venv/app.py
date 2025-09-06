from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def root():
    return jsonify(ok=True, msg='Hola desde Clase 3 (Python) - Flask (pip+venv)')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)