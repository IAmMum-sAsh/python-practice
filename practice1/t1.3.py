import math

def t1_3(n):
    f=0
    for i in range(1, n+1):
        f=f+(i**5-27*i**8)-11*(math.cos(i)-i**6)
    return "{:.2e}".format(f)

print(t1_3(68), "\t", t1_3(91))
