import math

def quadratic(a, b, c):
    if a == 0:
        return
    y = math.pow(b,2) - 4*a*c
    x1 = 2*c/(-b + math.sqrt(y))
    x2 = 2*c/(-b - math.sqrt(y))
    return x1,x2
