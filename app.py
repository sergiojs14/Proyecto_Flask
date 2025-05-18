from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def cargar_misiones():
    ruta = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

misiones = cargar_misiones()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/xxxs')
def xxxs():
    return render_template('xxxs.html')

@app.route('/listaxxxs', methods=['POST'])
def listaxxxs():
    nombre_busqueda = request.form.get('nombre', '').strip().lower()
    if not nombre_busqueda:
        # Si está vacío, mostrar todas
        resultados = misiones
    else:
        # Filtrar por coincidencia al inicio (case-insensitive)
        resultados = [
            m for m in misiones
            if m['nombreMision'].lower().startswith(nombre_busqueda)
        ]

    return render_template('listaxxxs.html', resultados=resultados)

@app.route('/xxx/<id_mision>')
def detalle_por_path(id_mision):
    m = next((x for x in misiones if x['idMision'] == id_mision), None)
    if not m:
        abort(404)
    return render_template('mision.html', mision=m)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
