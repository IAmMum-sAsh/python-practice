import math

def f12(x):
    if(x<129):
        return (x**7+math.cos(x))
    elif(129<=x<178):
        return ((math.log(x)-80*x**6)**4+math.exp(x))
    elif(178<=x<243):
        return (math.fabs(31*x**8)+x**7)
    elif(243<=x<274):
        return (87*(63*x**3-x**4-81)**8+x)
    else:
        return (98*x**3+x**8+41)
