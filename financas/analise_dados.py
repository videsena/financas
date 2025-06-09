import statistics, itertools, numpy
import scipy.stats

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

def correlacao(dados: list):
    series = list(dados[0].keys())

    correlacoes = {s: {} for s in series}

    for i in itertools.combinations(series, 2):
        serie_1 = [dados[i[0]] for dados in dados]
        serie_2 = [dados[i[1]] for dados in dados]
        correlacao = numpy.corrcoef(serie_1, serie_2)
        correlacoes[i[0]][i[1]] = correlacao[0][1]

    tabela = []
    for serie in series:
        aux = {}
        aux[''] = serie
        aux[serie] = 1
        for c in correlacoes[serie]:
            aux[c] = correlacoes[serie][c]
        tabela.append(aux)

    return tabela

def z_score(x, media, desvio_padrao):
    return (x - media) / desvio_padrao

def area_normal(z_score):
    return scipy.stats.norm.cdf(z_score)