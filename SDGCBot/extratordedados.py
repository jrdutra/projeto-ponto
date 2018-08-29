import bs4


def extrair(html_str):
    dados = []
    soup = bs4.BeautifulSoup(html_str, "html.parser")
    for td in soup.find_all(class_='Titulo'):
        dado = str(td.find())
        dado = dado.replace("<center>", "")
        dado = dado.replace("</center>", "")
        dados.append(dado)
    dados.remove("<sub>CPF</sub>")
    dados.remove("<sub>NOME</sub>")
    return dados

