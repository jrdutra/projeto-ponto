from SDGCBot import pontobiometrico
from SDGCBot import extratordedados
from SDGCBot import calculadoradehoras


parametros_req = {
    'login': 'pelisangela',
    'senha': 'daiana',
    'matricula': '27330',
    'cpf': '11666683710',
    'datafinal': '08-2018',
    'datainicial': '08-2018'
}

#html_str = pontobiometrico.requisita(parametros_req)
#dados = extratordedados.extrair(html_str)
#dados[5][2] + dados[5][3]
#dif = calculadoradehoras.calcintervalo("1/12/2001 - 07:40:00", "1/12/2001 - 13:36:00")
linha = ['1', 'Quarta', '08:02:00', '13:09:00', '', '', '', '', '', '', '', '']
linha = calculadoradehoras.formatalinha(linha, "08", "2018")
print(linha)

