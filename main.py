from SDGCBot import pontobiometrico
from SDGCBot import extratordedados
from SDGCBot import calculadoradehoras

# ================
# ENTRADA DE DADOS
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

#arquivo = open('ponto.html', 'w') # Abre novamente o arquivo (escrita)
#arquivo.write("fsdg")    # escreva o conteúdo criado anteriormente nele.
#arquivo.close()

print(html_str)
tabela = extratordedados.extrair(html_str)

horas = calculadoradehoras.calcsaldomes(tabela, mes, ano, cargahorria)
print("Saldo de: " + horas + " horas")

