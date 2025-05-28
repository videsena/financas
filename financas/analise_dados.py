import statistics

def estatistica_descritiva(dados):
    tabela = []

    media = statistics.mean(dados)
    mediana = statistics.median(dados)
    moda = statistics.mode(dados)
    desvio_padrao = statistics.stdev(dados)
    variancia = statistics.variance(dados)
    minimo = min(dados)
    maximo = max(dados)
    amplitude = maximo - minimo
    coeficiente_variacao = (desvio_padrao / media)
    contagem = len(dados)

    metricas = ['media', 'mediana', 'moda', 'desvio_padrao', 'variancia', 'minimo', 'maximo', 'amplitude', 'coeficiente_variacao', 'contagem']
    for metrica in metricas:
        aux = {}
        aux['metrica'] = metrica
        aux['valor'] = eval(metrica)
        tabela.append(aux)

    return tabela