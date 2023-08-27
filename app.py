from flask import Flask, render_template, request

app = Flask(__name__)
data = {
    "MYSQL": {
        "multiplataforma": "S",
        "relacional": "S",
        "software_libre": "S",
        "pesada": "N",
        "funciona_en_celulares": "N",
        "plsql": "N",
        "vertical": "N"
    },
    "POSTGRES": {
        "multiplataforma": "S",
        "relacional": "S",
        "software_libre": "S",
        "pesada": "N",
        "funciona_en_celulares": "N",
        "plsql": "S",
        "vertical": "S"
    },
    "ORACLE": {
        "multiplataforma": "S",
        "relacional": "S",
        "software_libre": "N",
        "pesada": "S",
        "funciona_en_celulares": "N",
        "plsql": "S",
        "vertical": "S"
    },
    "SQL-SERVER": {
        "multiplataforma": "N",
        "relacional": "S",
        "software_libre": "N",
        "pesada": "S",
        "funciona_en_celulares": "N",
        "plsql": "N",
        "vertical": "S"
    },
    "SQL-LITE": {
        "multiplataforma": "S",
        "relacional": "S",
        "software_libre": "S",
        "pesada": "N",
        "funciona_en_celulares": "S",
        "plsql": "N",
        "vertical": "N"
    },
    "MONGO-DB": {
        "multiplataforma": "S",
        "relacional": "N",
        "software_libre": "S",
        "pesada": "N",
        "funciona_en_celulares": "N",
        "plsql": "N",
        "vertical": "N"
    },
    "INFORMIX": {
        "multiplataforma": "N",
        "relacional": "S",
        "software_libre": "N",
        "pesada": "S",
        "funciona_en_celulares": "N",
        "plsql": "N",
        "vertical": "N"
    }
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Obtener respuestas del formulario
    answers = {
        'multiplataforma': request.form.get('multiplataforma'),
        'relacional': request.form.get('relacional'),
        'software_libre': request.form.get('software_libre'),
        'pesada': request.form.get('pesada'),
        'funciona_en_celulares': request.form.get('funciona_en_celulares'),
        'plsql': request.form.get('plsql'),
        'vertical': request.form.get('vertical')
    }

    # Comparar respuestas con datos
    matching_db = None
    for db, db_data in data.items():
        if all(answers[key] == db_data[key] for key in answers):
            matching_db = db
            break

    return render_template('result.html', matching_db=matching_db)

if __name__ == '__main__':
    app.run(debug=True)