from datetime import datetime
from datetime import date
from datetime import timedelta


def calcintervalo(hora1, hora2):
    datetime_format = "%d/%m/%Y - %H:%M:%S"
    hora1_dt = datetime.strptime(hora1, datetime_format)
    hora2_dt = datetime.strptime(hora2, datetime_format)
    dif = hora2_dt - hora1_dt
    return dif


def calctotaldia(linha, mes, ano):
    linha = formatalinha(linha, mes, ano)
    periodo1 = calcintervalo(linha[2], linha[3])
    periodo2 = calcintervalo(linha[4], linha[5])
    periodo3 = calcintervalo(linha[6], linha[7])
    periodo4 = calcintervalo(linha[8], linha[9])
    periodo5 = calcintervalo(linha[10], linha[11])
    horastrabalhadasdia = periodo1 + periodo2 + periodo3 + periodo4 + periodo5
    return horastrabalhadasdia


def calctotaltrabmes(tabela, mes, ano):
    saldodomes = calctotaldia(tabela[0], mes, ano)
    for i in range(1, len(tabela)):
        saldodomes = saldodomes + calctotaldia(tabela[i], mes, ano)
    return int(saldodomes.total_seconds())


def calcpadraomes(tabela, cargahoraria):
    tatalsegundos = 0
    hj = date.today()
    diadehoje = hj.day
    for i in range(0, len(tabela)):
        dia = str(tabela[i][1])
        sabado = "Sábado"
        domingo = "Domingo"
        if (dia != sabado and dia != domingo) and (int(tabela[i][0]) <= diadehoje):
            tatalsegundos = tatalsegundos + (cargahoraria * 3600)
    return tatalsegundos


def formatalinha(linha, mes, ano):
    flag = True
    for i in range(0, 12):
        strhora = linha[i]
        if strhora.find(":") >= 0:
            strhora = linha[0] + "/" + mes + "/" + ano + " - " + linha[i]
            linha[i] = strhora
            ultimahora = strhora
            flag = False
        if flag and i > 1:
            strhora = linha[0] + "/" + mes + "/" + ano + " - " + "00:00:00"
            ultimahora = strhora
            linha[i] = ultimahora
        if i > 1 and strhora == "":
            linha[i] = ultimahora
    return linha


def verificamarcacaodia(linha):
    flag = False
    for i in range(0, 11):
        strhora = linha[i]
        if strhora.find(":") >= 0:
           flag = True
    return flag


def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)


def calcsaldomes(tabela, mes, ano, cargahoraria):
    totaltrabalhado = calctotaltrabmes(tabela, mes, ano)
    totalatrabalhar = calcpadraomes(tabela, cargahoraria)
    saldosegundos = totaltrabalhado - totalatrabalhar

    saldohoras = humanize_time(saldosegundos)

    return saldohoras
