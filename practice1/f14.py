import math

def f14(n):
    if(n==0):
        return 5
    else:
        return (f14(n-1)/41-math.tan(f14(n-1)))
