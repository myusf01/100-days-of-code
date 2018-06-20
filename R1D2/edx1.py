from math import tan, pi

def polysum(n,s):
    area = (0.25 * n * (s ** 2))/ tan(pi/n)
    prmtr = n * s
    summ = area + (prmtr ** 2)
    return round(summ, 4)