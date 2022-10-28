from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
# ---- Partidos ---- #
@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)
# ---- fin partidos ---- #
# ---- mesa ---- #
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas", methods=['POST'])
def createMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
# ---- fin mesas ---- #
# ---- rel partido - candidato ---- #
@app.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartido(id, id_partido):
    json = miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)
# ---- fin rel partido - candidato ---- #
# ---- resultado ---- #
@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['POST'])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['PUT'])
def updateResultado(id_resultado, id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado,data,id_mesa, id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>", methods=['DELETE'])
def deleteResult(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)
# ---- fin resultado ---- #
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
#probando cluster del proyecto guia
ca = certifi.where()
#cadena del proyecto pruba
#client = pymongo.MongoClient("mongodb+srv://usuario-pruebas:prueba123@cluster0.qfgmf.mongodb.net/bd-registro-academico?retryWrites=true&w=majority",tlsCAFile=ca)
#cadena de mi proyecto
client = pymongo.MongoClient("mongodb+srv://ss5gc4team5:6Kgrlbk7lN8QY2bL@clusterteam5.m2noqns.mongodb.net/votaciones2022?retryWrites=true&w=majority")

db = client.test
print(db)
baseDatos = client["votaciones2022"]
print(baseDatos.list_collection_names())