from SDGCBot import pontobiometrico
from SDGCBot import extratordedados
from SDGCBot import calculadoradehoras
from SDGCBot import feriado
from SDGCBot import dadosfuncionario
import os


tabeladados = dadosfuncionario.dadosfuncionarios("dadosfuncionario.csv")


# ================
# ENTRADA DE DADOS JOAO
# ================
nome = str(tabeladados[0][0])
mes = str(tabeladados[0][1])
ano = str(tabeladados[0][2])
cpf = str(tabeladados[0][3])
matricula = str(tabeladados[0][4])
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

html_str = pontobiometrico.requisita(parametros_req)

#arquivo = open('ponto.html', 'w') # Abre novamente o arquivo (escrita)
#arquivo.write("fsdg")    # escreva o conteúdo criado anteriormente nele.
#arquivo.close()

print(html_str)
tabela = extratordedados.extrair(html_str)

os.system('cls')
print("---------------------------------------------------------------------------------------------------------")
print("                                   PONTO DO MÊS " + mes + " de " + nome)
print("---------------------------------------------------------------------------------------------------------")


print('{:^5}'.format('Data') + '{:{align}{width}}'.format('Dia', align='<', width='10') +
          '{:^9}'.format('Hora 1') + '{:^9}'.format('Hora 2') + '{:^9}'.format('Hora 3') +
          '{:^9}'.format('Hora 4') + '{:^9}'.format('Hora 5') + '{:^9}'.format('Hora 6') +
          '{:^9}'.format('Hora 7') + '{:^9}'.format('Hora 8') +
          '{:^9}'.format('Hora 9') + '{:^9}'.format('Hora 10'))

for i in range(0, len(tabela)):
    print('{:^5}'.format(tabela[i][0]) + '{:{align}{width}}'.format(tabela[i][1], align='<', width='10') +
          '{:^9}'.format(tabela[i][2]) + '{:^9}'.format(tabela[i][3]) + '{:^9}'.format(tabela[i][4]) +
          '{:^9}'.format(tabela[i][5]) + '{:^9}'.format(tabela[i][6]) + '{:^9}'.format(tabela[i][7]) +
          '{:^9}'.format(tabela[i][8]) + '{:^9}'.format(tabela[i][9]) +
          '{:^9}'.format(tabela[i][10]) + '{:^9}'.format(tabela[i][11]))
print("---------------------------------------------------------------------------------------------------------")

tabelaferiados = feriado.tabeladeferiados("feriados.csv")
horas = calculadoradehoras.calcsaldomes(tabela, tabelaferiados, mes, ano, cargahorria)
print("Saldo de: " + horas + "h")

print("---------------------------------------------------------------------------------------------------------")
