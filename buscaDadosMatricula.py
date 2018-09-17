from SDGCBot import pontobiometrico
from SDGCBot import extratordedados
from SDGCBot import calculadoradehoras
from SDGCBot import feriado
from SDGCBot import dadosfuncionario
import os


tabeladados = dadosfuncionario.dadosfuncionarios("dadosfuncionario.csv")
matricula = input("Entre com a matricula>>>")

# ================
# ENTRADA DE DADOS JOAO
# ================
nome = str(tabeladados[0][0])
mes = str(tabeladados[0][1])
ano = str(tabeladados[0][2])
cpf = str(tabeladados[0][3])
matricula = matricula
cargahorria = int(tabeladados[0][5])
login = "-"
senha = "-"
# ================

datafinal = mes + '-' + ano
datainicial = datafinal

parametros_req = {
    'login': login,
    'senha': senha,
    'matricula': matricula,
    'cpf': cpf,
    'datafinal': datafinal,
    'datainicial': datainicial
}

html_str = pontobiometrico.requisitaPesquisa(parametros_req)
print(html_str)





