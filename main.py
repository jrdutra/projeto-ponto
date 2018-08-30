from SDGCBot import pontobiometrico
from SDGCBot import extratordedados
from SDGCBot import calculadoradehoras

# ================
# ENTRADA DE DADOS
# ================
mes = "08"
ano = "2018"
cpf = "08581603742"
matricula = "28142"
cargahorria = 6
login = "-"
senha= "-"
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

horas = calculadoradehoras.calcsaldomes(tabela, mes, ano, cargahorria)
print(horas)

