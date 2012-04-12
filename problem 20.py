def product(stuff):
    prod = 1
    for elem in stuff:
        prod *= elem
    return prod

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

factorial=product(range(1, 101))
print sum(digits(factorial))
