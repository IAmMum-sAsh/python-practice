import math

def t1_4(n):
    if(n==0):
        return 5
    else:
        return (t1_4(n-1)/41-math.tan(t1_4(n-1)))

print("{:.2e}".format(t1_4(8)), "\t", "{:.2e}".format(t1_4(2)))
