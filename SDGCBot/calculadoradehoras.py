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


def calcpadraomes(tabela, cargahoraria, mes):
    tatalsegundos = 0
    hj = date.today()
    if hj.month == int(mes):
        diaderefernecia = hj.day
    else:
        diaderefernecia = 31
    for i in range(0, len(tabela)):
        dia = str(tabela[i][1])
        sabado = "Sábado"
        domingo = "Domingo"
        feriado = "Feriado"
        if (dia != sabado and dia != domingo and dia != feriado) and (int(tabela[i][0]) <= diaderefernecia):
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


def humanize_time(segundos):
    hora = segundos / 3600
    seg_rest = segundos % 3600
    minuto = 60 - (seg_rest / 60)
    minuto_rest = seg_rest % 60
    segundo = minuto_rest
    res = '{:02.0f}'.format(hora) + ":" + '{:02.0f}'.format(minuto) + ":" + '{:02.0f}'.format(segundo)
    return str(res)


def addferiados(tabela, tabelaferiados, mes, ano):
    for i in range(0, len(tabela)):
        for j in range(0, len(tabelaferiados)):
            if tabelaferiados[j][0] == ano:
                if tabelaferiados[j][1] == mes:
                    if tabelaferiados[j][2] == tabela[i][0]:
                        tabela[i][1] = "Feriado"
    return tabela


def calcsaldomes(tabela, tabelaferiados, mes, ano, cargahoraria):
    tabelatratada = addferiados(tabela, tabelaferiados, mes, ano)
    totaltrabalhado = calctotaltrabmes(tabelatratada, mes, ano)
    totalatrabalhar = calcpadraomes(tabelatratada, cargahoraria, mes)
    saldosegundos = totaltrabalhado - totalatrabalhar
    print(str(saldosegundos/3600))
    saldohoras = humanize_time(saldosegundos)

    return saldohoras
