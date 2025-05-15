from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def cargar_misiones():
    try:
        with open("data.json", 'r', encoding='utf-8') as archivo:
            misiones = [json.loads(line) for line in archivo if line.strip()]
        return misiones
    except FileNotFoundError:
        print("El fichero no fue encontrado.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return []


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

    if nombre_busqueda == '':
        resultados = misiones  # Muestra todas si no hay búsqueda
    else:
        resultados = [
            m for m in misiones
            if m['nombreMision'].lower().startswith(nombre_busqueda)
        ]

    return render_template('listaxxxs.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)

