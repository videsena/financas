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