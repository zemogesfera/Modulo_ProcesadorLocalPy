from flask import Flask, render_template, request, jsonify, send_file
import os
import json
from etl.extract import extract_data


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    ruta = request.form['ruta']
    
    if not os.path.exists(ruta):
        return jsonify({"error": "Ruta no encontrada"}), 400
    
    resultado = extract_data(ruta, cantidad=None)
    
    # Guardar el JSON generado en la carpeta especificada
    json_path = os.path.join(ruta, "resultado.json")
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(resultado, json_file, ensure_ascii=False, indent=4)
    
    # Enviar el resultado para mostrarlo en la página
    return jsonify({"resultado": resultado, "json_path": json_path})

@app.route('/descargar', methods=['GET'])
def descargar():
    ruta = request.args.get('ruta')
    json_path = os.path.join(ruta, "resultado.json")
    
    if os.path.exists(json_path):
        return send_file(json_path, as_attachment=True)
    else:
        return jsonify({"error": "Archivo no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)

