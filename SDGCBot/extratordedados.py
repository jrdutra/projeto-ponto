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
    tabela = []
    linha = []
    controle = 0
    for i in range(0, len(dados)):
        linha.append(dados[i])
        controle += 1
        if controle > 11:
            controle = 0
            tabela.append(linha)
            linha = []
    return tabela

