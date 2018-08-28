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

test = {'Content-type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
        'origin':'https://www.sdgc.com.br',
        'referer':'https://www.sdgc.com.br'}


with requests.Session() as session:
    response = session.get('https://www.sdgc.com.br/sdgc/login.php')
    phpssid = response.cookies.get_dict()
    print(phpssid['PHPSESSID'])

    print(response.cookies)
    cookie = response.cookies
    response = session.post(POST_LOGIN_URL, data=payload, cookies=cookie)
    cookie = response.cookies
    cookie2 = cookies=[{'PHPSESSID': phpssid['PHPSESSID'],
                        'CreationTime': 'Tue 28 Aug 2018 11:53:24 GMT',
                        'Domain': 'www.sdgc.com.br',
                        'Expires': 'Session',
                        'HostOnly': True,
                        'HttpOnly': False,
                        'LastAcessed': "Tue 28 Aug 2018 11:52:24 GMT",
                        'Path': '/',
                        'Secure': False,
                        'sameSite': 'Unset'}]

    response = session.post(REQUEST_URL, data=payload2, cookies=cookie2)
    print(response.text)   #or whatever else you want to do with the request data!