from SDGCBot import pontobiometrico
from SDGCBot import extratordedados

parametros_req = {
    'login': 'pelisangela',
    'senha': 'daiana',
    'matricula': '27330',
    'cpf': '11666683710',
    'datafinal': '08-2018',
    'datainicial': '08-2018'
}

html_str = pontobiometrico.requisita(parametros_req)
dados = extratordedados.extrair(html_str)
print(dados[5][2])
