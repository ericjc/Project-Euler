def lcm(a, b):
    l=a
    m=b
    q=l/m
    r=l%m
    while r>0:
        l=m
        m=r
        q=l/m
        r=l%m
    return (a*b/m)

print lcm(2520, lcm(11, lcm(12, lcm(13, lcm(14, lcm(15, lcm(16, lcm(17, lcm(18, lcm(19, 20))))))))))


