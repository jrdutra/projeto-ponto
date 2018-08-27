import requests

URL = "https://www.sdgc.com.br/sdgc/login.php"
r = requests.post(URL, data={'nome_usuario': "pelisangela",
                             'senha_usuario': '---',
                             'alterarSenha': '',
                             'verifica': '1'})
print(r.status_code, r.reason)
page_html = r.text[:]

URL_ponto = "https://www.sdgc.com.br/sdgc/frequencia/lancarponto"

