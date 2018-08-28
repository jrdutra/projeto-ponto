import requests

POST_LOGIN_URL = "https://www.sdgc.com.br/sdgc/login.php"
REQUEST_URL = "https://www.sdgc.com.br/sdgc/frequencia/lancarponto.php"

payload={'nome_usuario': "pelisangela",
         'senha_usuario': 'daiana',
         'alterarSenha': '',
         'verifica': '1'}

payload2={'cpf': "11666683710",
          'pass': "",
          'exibir': "1",
          'busca_sub_sec': "1",
          'biometrico': "sim",
          'oco': "nao",
          'valor_mes_ano_inicial': "08-2018",
          'valor_mes_ano_final': "08-2018"}

with requests.Session() as session:
     response = session.post(POST_LOGIN_URL, data=payload)
     #print(response.text)
     #response = session.post(REQUEST_URL, data=payload2)
     #print(response.text)
     response = session.get("https://sdgc.com.br/sdgc/frequencia/ponto")
     print(response.text)
