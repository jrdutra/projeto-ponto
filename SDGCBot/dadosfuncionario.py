import csv


def dadosfuncionarios(filename):
    tabela = []
    with open(filename, newline='') as ficheiro:
        spamreader = csv.reader(ficheiro,  delimiter=';', quotechar='|')
        for row in spamreader:
            tabela.append(row)
    return tabela