from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/conversion/<string:tipo>/<string:saldo>/<string:tipoCambio>')
def conversion(tipo,saldo,tipoCambio):
    resultadoConversion = float(saldo)*getTasaConversion(tipo, tipoCambio)
    return jsonify({tipoCambio: resultadoConversion})

def getTasaConversion(tipo, tipoCambio):
    tasaPeso = {"dollar":.048, "yenes": 5.60, "euros": .044, "won": 58.28, "soles": .18, "bolivares": .21, "quetzal": .37, "yuanes": .31, "rupia": 3.67}
    tasa = 0.0

    if tipo == "peso":tasa = tasaPeso[tipoCambio]
    return tasa




if __name__=="__main__":
    app.run(debug=True)

