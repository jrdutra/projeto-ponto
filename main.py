import requests

POST_LOGIN_URL = "https://www.sdgc.com.br/sdgc/login.php"
PESQUISA_URL = "https://sdgc.com.br/sdgc/frequencia/ponto?id=ponto"
PONTO_URL = "https://www.sdgc.com.br/sdgc/frequencia/lancarponto"

payload={'nome_usuario': "pelisangela",
         'senha_usuario': 'daiana',
         'alterarSenha': '',
         'verifica': '1'}

payload1={'organiza': 'nome_info',
            'nome': '',
            'matricula': '27330',
            'cpf': '',
            'valor_mes_ano_final': '08-2018',
            'valor_mes_ano_inicial': '08-2018',
            'pesquisa': '1',
            'enviou': '1'
    }

payload2={'cpf': "11666683710",
          'pass': "",
          'exibir': "1",
          'busca_sub_sec': "1",
          'biometrico': "sim",
          'oco': "nao",
          'valor_mes_ano_inicial': "08-2018",
          'valor_mes_ano_final': "08-2018",
          'Submit2': 'Confirmar'}

with requests.Session() as session:
     response = session.post(POST_LOGIN_URL, data=payload)
     response = session.get(PESQUISA_URL)
     response = session.post(PESQUISA_URL, data=payload1)
     response = session.post(PONTO_URL, data=payload2)
     print(response.text)
