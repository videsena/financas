import math

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