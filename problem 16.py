def digits(n):
    digits=[]
    x=n
    i=1
    while 10**(i-1)<n:
        a=x%(10**i)
        digits.append(a/(10**(i-1)))
        x=x-a
        i+=1
    digits.reverse()
    return digits

t=2**1000
print sum(digits(t))
