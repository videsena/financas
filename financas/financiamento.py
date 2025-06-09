from . import calculos
from . import tools

def tabela_sac(periodos: int, taxa: float, principal: float, extraordinarias: dict = {}) -> list:
    tabela = []
    tabela.append({'periodo': 0, 'saldo_devedor': principal, 'juros': 0.0, 'amortizacao_base': 0.0, 'amortizacao_extra': 0.0, 'parcela': 0.0})

    saldo_devedor = principal
    for x in range(1, periodos + 1):
        if saldo_devedor <= 0.0:
            continue

        amort_base = calculos.percentual(periodos, x) * saldo_devedor
        amort_extra = extraordinarias.get(x, 0.0)
        juros = saldo_devedor * taxa
        pgto_base = amort_base + juros
        saldo_devedor = saldo_devedor - amort_base - amort_extra

        tabela.append({'periodo': x, 'saldo_devedor': saldo_devedor, 'juros': juros, 'amortizacao_base': amort_base, 'amortizacao_extra': amort_extra,  'parcela': pgto_base + amort_extra})

    return tabela

def tabela_price(periodos: int, taxa: float, principal: float, extraordinarias: dict = {}) -> list:
    tabela = []
    tabela.append({'periodo': 0, 'saldo_devedor': principal, 'juros': 0.0, 'amortizacao_base': 0.0, 'amortizacao_extra': 0.0, 'parcela': 0.0})

    pgto = (principal * taxa) / (1 - (1 + taxa) ** (-periodos))

    saldo_devedor = principal
    for x in range(1, periodos + 1):
        if saldo_devedor <= 0.0:
            continue

        juros = saldo_devedor * taxa
        amort_base = pgto - juros
        amort_extra = extraordinarias.get(x, 0.0)
        saldo_devedor = saldo_devedor - amort_base - amort_extra

        tabela.append({'periodo': x, 'saldo_devedor': saldo_devedor, 'juros': juros, 'amortizacao_base': amort_base, 'amortizacao_extra': amort_extra,  'parcela': pgto + amort_extra})

    return tabela

def tabela_mista(periodos: int, taxa: float, principal: float, extraordinarias: dict = {}) -> list:
    lista_tabela_sac = tabela_sac(periodos, taxa, principal, extraordinarias)
    lista_tabela_price = tabela_price(periodos, taxa, principal, extraordinarias)

    tabela = []
    tabela.append({'periodo': 0, 'saldo_devedor': principal, 'juros': 0.0, 'amortizacao_base': 0.0, 'amortizacao_extra': 0.0, 'parcela': 0.0})

    saldo_devedor = principal
    for s, p in zip(lista_tabela_sac, lista_tabela_price):
        periodo = s['periodo']
        if periodo != 0:
            parcela = (s['parcela'] + p['parcela']) / 2
            juros = saldo_devedor * taxa
            amort_base = parcela - juros
            amort_extra = s['amortizacao_extra']
            saldo_devedor = saldo_devedor - amort_base - amort_extra

            tabela.append({'periodo': periodo, 'saldo_devedor': saldo_devedor, 'juros': juros, 'amortizacao_base': amort_base, 'amortizacao_extra': amort_extra,  'parcela': parcela})

    return tabela

def tabela_americana(periodos: int, taxa: float, principal: float, extraordinarias: dict = {}) -> list:
    tabela = []
    tabela.append({'periodo': 0, 'saldo_devedor': principal, 'juros': 0.0, 'amortizacao_base': 0.0, 'amortizacao_extra': 0.0, 'parcela': 0.0})

    saldo_devedor = principal
    for x in range(1, periodos):
        if saldo_devedor <= 0.0:
            continue

        juros = saldo_devedor * taxa
        tabela.append({'periodo': x, 'saldo_devedor': saldo_devedor, 'juros': juros, 'amortizacao_base': 0.0, 'amortizacao_extra': 0.0,  'parcela': juros})

    tabela.append({'periodo': x + 1, 'saldo_devedor': saldo_devedor, 'juros': juros, 'amortizacao_base': saldo_devedor, 'amortizacao_extra': 0.0,  'parcela': juros + saldo_devedor})

    return tabela