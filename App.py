import pandas as pd
from flask import Flask, jsonify
from Scrapper import Scrapper

scrapper = Scrapper()
listaUsuarios = []
listaUsuarios.append("equacionacompaulopereira/")
listaUsuarios.append("cienciasemfim/")
listaUsuarios.append("universidadedosdados/")

app = Flask(__name__)
@app.route('/')
def homepage():
    return 'Hello World!'
@app.route('/usuarios')
def iniciar():
  result = {}
  for url in listaUsuarios:
     usuario = scrapper.iniciarBusca(url)
     result.__setitem__(url, usuario)
  return jsonify(result)
app.run()
