import math, scipy


def kupiec(n, x, p):
    dividend = (((1-p) ** (n-x)) * (p ** x))
    divisor = ((1-(x/n)) ** (n-x)) * ((x/n) ** x)
    return -2 * math.log(dividend/divisor)
    
def kupiec_limits(n, p):
    chi2 = float(scipy.stats.distributions.chi2.ppf((1-p), df=1))
    
    x = 0
    while kupiec(n, x, p) > chi2: x += 1     

    x1 = x - 1
    while kupiec(n, x, p) < chi2: x += 1        

    return x1, x