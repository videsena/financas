import calculators

def tabela_sac(n: int, i: float, vp: float) -> list:
    tabela = []
    tabela.append({'n': 0, 'sd': vp, 'amortizacao': 0.0, 'juros': 0.0, 'parcela': 0.0})

    sd = vp
    for x in range(1,n+1):
        amort = calculators.percentual(n, x) * sd
        juros = sd * i
        pgto = amort + juros
        sd = sd - amort

        tabela.append({'n': x, 'sd': round(sd, 2), 'amortizacao': round(amort, 2), 'juros': round(juros, 2), 'parcela': round(pgto, 2)})

    return tabela

def tabela_price(n: int, i: float, vp: float) -> list:
    tabela = []
    tabela.append({'n': 0, 'sd': vp, 'amortizacao': 0.0, 'juros': 0.0, 'parcela': 0.0})

    pgto = (vp * i) / (1 - (1 + i) ** (-n))

    sd = vp
    for x in range(1,n+1):
        juros = sd * i
        amort = pgto - juros
        sd = sd - amort

        tabela.append({'n': x, 'sd': round(sd, 2), 'amortizacao': round(amort, 2), 'juros': round(juros, 2), 'parcela': round(pgto, 2)})

    return tabela