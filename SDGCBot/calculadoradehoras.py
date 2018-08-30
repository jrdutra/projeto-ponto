from datetime import datetime
from datetime import timedelta


def calcintervalo(hora1, hora2):
    datetime_format = "%d/%m/%Y - %H:%M:%S"
    hora1_dt = datetime.strptime(hora1, datetime_format)
    hora2_dt = datetime.strptime(hora2, datetime_format)
    dif = hora2_dt - hora1_dt
    return dif


def formatalinha(linha, mes, ano):
    for i in range(0, 11):
        strhora = linha[i]
        if strhora.find(":") >= 0:
            strhora = linha[0] + "/" + mes + "/" + ano + " - " + linha[i]
            linha[i] = strhora
    return linha


def verificamarcacaodia(linha):
    flag = False
    for i in range(0, 11):
        strhora = linha[i]
        if strhora.find(":") >= 0:
           flag = True
    return flag
