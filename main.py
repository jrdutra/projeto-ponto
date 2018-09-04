from SDGCBot import pontobiometrico
from SDGCBot import extratordedados
from SDGCBot import calculadoradehoras
from SDGCBot import feriado

# ================
# ENTRADA DE DADOS JOAO
# ================
mes = "09"
ano = "2018"
cpf = "11666683710"
matricula = "27330"
cargahorria = 6
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

html_str = pontobiometrico.requisita(parametros_req)
tabela = extratordedados.extrair(html_str)

for i in range(0, len(tabela)):
    print(tabela[i])


tabelaferiados = feriado.tabeladeferiados("feriados.csv")
horas = calculadoradehoras.calcsaldomes(tabela, tabelaferiados, mes, ano, cargahorria)
print("Saldo de: " + horas + "h")