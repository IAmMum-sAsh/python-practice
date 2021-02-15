import math

def t1_2(x):
    if(x<129):
        return "{:.2e}".format(x**7+math.cos(x))
    elif(129<=x<178):
        return "{:.2e}".format((math.log(x)-80*x**6)**4+math.exp(x))
    elif(178<=x<243):
        return "{:.2e}".format(math.fabs(31*x**8)+x**7)
    elif(243<=x<274):
        return "{:.2e}".format(87*(63*x**3-x**4-81)**8+x)
    else:
        return "{:.2e}".format(98*x**3+x**8+41)

print(t1_2(136), "\t", t1_2(160))
