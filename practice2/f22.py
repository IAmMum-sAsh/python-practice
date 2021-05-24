def f22(n):
    a=(n&0x0000007f) << 25
    b=(n&0x0001ff80) << 8
    cd=(n&0xFFFE0000) >> 17
    return (a|b|cd)
