import calculators

def tabela_sac(periodos: int, taxa: float, principal: float) -> list:
    tabela = []
    tabela.append({'periodo': 0, 'saldo_devedor': principal, 'amortizacao': 0.0, 'juros': 0.0, 'parcela': 0.0})

    saldo_devedor = principal
    for x in range(1,periodos+1):
        amort = calculators.percentual(periodos, x) * saldo_devedor
        juros = saldo_devedor * taxa
        pgto = amort + juros
        saldo_devedor = saldo_devedor - amort

        tabela.append({'periodo': x, 'saldo_devedor': saldo_devedor, 'amortizacao': amort, 'juros': juros, 'parcela': pgto})

    return tabela

def tabela_price(periodos: int, taxa: float, principal: float) -> list:
    tabela = []
    tabela.append({'periodo': 0, 'saldo_devedor': principal, 'amortizacao': 0.0, 'juros': 0.0, 'parcela': 0.0})

    pgto = (principal * taxa) / (1 - (1 + taxa) ** (-periodos))

    saldo_devedor = principal
    for x in range(1,periodos+1):
        juros = saldo_devedor * taxa
        amort = pgto - juros
        saldo_devedor = saldo_devedor - amort

        tabela.append({'periodo': x, 'saldo_devedor':saldo_devedor, 'amortizacao': amort, 'juros': juros, 'parcela': pgto})

    return tabela