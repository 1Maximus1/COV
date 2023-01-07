import math

def log(a,b):
    if a>0 and a!=1 and b>0:
        return math.log(b,a) 
    else:
        raise ValueError("Error: invalid value")

def ln(b):
    if b>0:
        return math.log(b)
    else:
        raise ValueError("Error: invalid value")

def lg(b):
    if b>0:
        return math.log10(b)
    else:
        raise ValueError("Error: invalid value")
