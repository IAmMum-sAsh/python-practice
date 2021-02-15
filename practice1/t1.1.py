import math

def t1_1 (x, y, z):
    return "{:.2e}".format((y**5-27*x**8)/(y**4-39*x)+math.sin(math.exp(x)+math.sin(z)-88)-16*x**2-(x+80*y**5))

print(t1_1(-31,-60,53),"\t",t1_1(-20,16,70))
