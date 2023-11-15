from flask import Flask, render_template, request
from waitress import serve
import requests, os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    libros = []
    if request.method == 'POST':
        query = request.form.get('q')
        respuesta = requests.get(f'http://api:5000/libros?q={query}')
        if respuesta.status_code == 200:
            libros = respuesta.json()

    return render_template('index.html', libros=libros)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    serve(app, host='0.0.0.0', port=port)
