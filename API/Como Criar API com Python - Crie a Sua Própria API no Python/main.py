# necessário flask e pandas, usar a barra lateral "packager"

import pandas as pd
from flask import Flask, jsonify

minhaapi = Flask(__name__)

@minhaapi.route("/")
def mensagem():
  return "Oláááááá!!!!"

@minhaapi.route('/pegarvendas')
def consulta():
  tabela = pd.read_csv('tabelabase.csv')
  total_vendas = tabela['Vendas'].sum()
  #resposta = {"Total de vendas: ": total_vendas}
  return jsonify({"Total_de_vendas": total_vendas})
  
  
# argumento host='0.0.0.0' faz a api rodar de forma publica na internet
minhaapi.run(host='0.0.0.0')
