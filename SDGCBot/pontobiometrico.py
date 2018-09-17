import requests

POST_LOGIN_URL = "https://www.sdgc.com.br/sdgc/login.php"
PESQUISA_URL = "https://sdgc.com.br/sdgc/frequencia/ponto?id=ponto"
PONTO_URL = "https://www.sdgc.com.br/sdgc/frequencia/lancarponto"


def requisita(parametros):

    dadoslogin = {'nome_usuario': parametros['login'],
                   'senha_usuario': parametros['senha'],
                   'alterarSenha': '',
                   'verifica': '1'}

    dadospesquisa = {'organiza': 'nome_info',
                        'nome': '',
                        'matricula': parametros['matricula'],
                        'cpf': '',
                        'valor_mes_ano_final': parametros['datafinal'],
                        'valor_mes_ano_inicial': parametros['datainicial'],
                        'pesquisa': '1',
                        'enviou': '1'}

    dadosfolha = {'cpf': parametros['cpf'],
                'pass': "",
                'exibir': "1",
                'busca_sub_sec': "1",
                'biometrico': "sim",
                'oco': "nao",
                'valor_mes_ano_inicial':  parametros['datafinal'],
                'valor_mes_ano_final': parametros['datainicial'],
                'Submit2': 'Confirmar'}

    with requests.Session() as session:
        response = session.post(POST_LOGIN_URL, data=dadoslogin)
        response = session.get(PESQUISA_URL)
        response = session.post(PESQUISA_URL, data=dadospesquisa)
        response = session.post(PONTO_URL, data=dadosfolha)
        html_str = response.text
    return html_str

def requisitaPesquisa(parametros):
    dadoslogin = {'nome_usuario': parametros['login'],
                   'senha_usuario': parametros['senha'],
                   'alterarSenha': '',
                   'verifica': '1'}

    dadospesquisa = {'organiza': 'nome_info',
                        'nome': '',
                        'matricula': parametros['matricula'],
                        'cpf': '',
                        'valor_mes_ano_final': parametros['datafinal'],
                        'valor_mes_ano_inicial': parametros['datainicial'],
                        'pesquisa': '1',
                        'enviou': '1'}
    
    with requests.Session() as session:
        response = session.post(POST_LOGIN_URL, data=dadoslogin)
        response = session.get(PESQUISA_URL)
        response = session.post(PESQUISA_URL, data=dadospesquisa)
    html_str = response.text
    return html_str
