import math
from . import tools
import copy

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

class periods:
    def year_month(i):
        return (1 + i) ** (1/12) - 1
    
    def year_day(i):
        return (1 + i) ** (1/252) - 1
    
    def month_year(i):
        return (1 + i) ** (12) - 1
    
    def month_day(i):
        return (1 + i) ** (12) - 1
    
    def day_year(i):
        return (1 + i) ** (252) - 1
    
    def day_month(i):
        return (1 + i) ** (21) - 1
    

def converte_taxas_paralelo(taxas):
    func = periods.year_month
    return tools.paralelo(func, taxas)

def converte_taxas_serie(taxas):
    lista_taxas = []
    for i, taxa in enumerate(taxas):
        lista_taxas.append(periods.year_month(taxa[0]))
        print(i, end='\r')

    return lista_taxas