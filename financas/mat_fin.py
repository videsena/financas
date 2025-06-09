import math
from . import tools
import copy, itertools

def fv(pv, n, i):
    return pv * (1 + i) ** (n)

def pv(fv, n, i):
    return fv / (1 + i) ** (n)

def n(pv, fv, i):
    return - math.log(fv/pv) / math.log(1 + i)

def i(pv, fv, n):
    return (pv/fv) ** (1/n) - 1

def pmt(pv, i, n):
    return  (pv * i) / (1 - (1 + i) ** (-n))

class conversions:
    def year_month(i):
        return (1 + i) ** (1/12) - 1
    
    def year_day(i):
        return (1 + i) ** (1/252) - 1
    
    def month_year(i):
        return (1 + i) ** (12) - 1
    
    def month_day(i):
        return (1 + i) ** (1/21) - 1
    
    def day_year(i):
        return (1 + i) ** (252) - 1
    
    def day_month(i):
        return (1 + i) ** (21) - 1
    
def vpl(fluxos_caixa: list, i: float):
    investimento = fluxos_caixa[0]
    fluxos_vl_presente = vpl_fluxos(fluxos_caixa, i)

    return investimento + sum(fluxo for fluxo in fluxos_vl_presente)

def vpl_fluxos(fluxos_caixa: list, i: float):
    fluxos_vl_presente = []

    for n, fluxo in enumerate(fluxos_caixa):
        if n != 0:
            vl = fluxo / (1 + i) ** (n)
            fluxos_vl_presente.append(vl)

    return fluxos_vl_presente

def taxa_real(taxa_nominal: float, inflacao: float):
    return (1 + taxa_nominal) / (1 + inflacao) - 1

def taxa_nominal(taxa_real: float, inflacao: float):
    return (1 + taxa_real) * (1 + inflacao) - 1

def taxa_inflacao(taxa_nominal: float, taxa_real: float):
    return (1 + taxa_nominal) / (1 + taxa_real) - 1

def payback(fluxos_caixa: list):
    investimento = fluxos_caixa[0]
    for n, fluxo in enumerate(fluxos_caixa):
        if n != 0:
            investimento += fluxo
            if investimento + fluxos_caixa[n + 1] >= 0:
                return n + abs(investimento) / fluxos_caixa[n + 1]

    return "Não há payback"

def payback_descontado(fluxos_caixa: list, i: float):
    investimento = fluxos_caixa[0]
    fluxos_caixa = vpl_fluxos(fluxos_caixa, i)
    for n, fluxo in enumerate(fluxos_caixa, start=1):
        investimento += fluxo
        if investimento + fluxos_caixa[n + 1] >= 0:
            return n + abs(investimento) / fluxos_caixa[n + 1]

    return "Não há payback"