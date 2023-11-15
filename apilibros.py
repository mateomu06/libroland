from flask import Flask, jsonify, request
from waitress import serve
import requests, os

app = Flask(__name__)


def buscar_libros(query):
    if not query:
        raise ValueError('Debes proporcionar una consulta de búsqueda.')

    respuesta = requests.get(
        f'https://openlibrary.org/search.json?q={query}&fields=title,author_name,edition_key,cover_edition_key')

    if respuesta.status_code != 200:
        raise Exception(
            f'Error al realizar la solicitud: {respuesta.status_code}')

    data = respuesta.json()
    # Select the first 10 results
    libros = data.get('docs', [])[:10]

    libros_para_devolver = []
    for libro in libros:

        edition_key = libro.get('edition_key', [''])[-1]
        url_libro = f'https://openlibrary.org/books/{edition_key}' if edition_key else ''

        cover_edition_key = libro.get('cover_edition_key', '')
        if cover_edition_key:
            url_portada = f'https://covers.openlibrary.org/b/olid/{cover_edition_key}-M.jpg'
        else:
            url_portada = 'https://openlibrary.org/images/icons/avatar_book-sm.png'
        libros_para_devolver.append({
            'titulo': libro.get('title', ''),
            'autor': libro.get('author_name', [''])[0],
            'portada': url_portada,
            'url': url_libro
        })

    return libros_para_devolver


@app.route('/libros', methods=['GET'])
def obtener_libros():
    query = request.args.get('q')

    try:
        libros = buscar_libros(query)
        return jsonify(libros)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port)
