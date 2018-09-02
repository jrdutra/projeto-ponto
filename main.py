from SDGCBot import pontobiometrico
from SDGCBot import extratordedados
from SDGCBot import calculadoradehoras
from SDGCBot import feriado

# ================
# ENTRADA DE DADOS JOAO
# ================
mes = "08"
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

tabelaferiados = feriado.tabeladeferiados("feriados.csv")
horas = calculadoradehoras.calcsaldomes(tabela, tabelaferiados, mes, ano, cargahorria)
print("Saldo de João no mês " + mes + ": " + horas + "h")



# ==============================================================================================

# ================
# ENTRADA DE DADOS JOAO
# ================
mes = "08"
ano = "2018"
cpf = "08581603742"
matricula = "28142"
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

tabelaferiados = feriado.tabeladeferiados("feriados.csv")
horas = calculadoradehoras.calcsaldomes(tabela, tabelaferiados, mes, ano, cargahorria)
print("Saldo de Amauri no mês " + mes + ": " + horas + "h")
