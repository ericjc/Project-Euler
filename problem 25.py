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
x=0
y=1
i=1
while True:
    x=x+y
    i+=1
    if len(digits(x))==1000:
        print x
        print i
        break
    y=y+x
    i+=1
    if len(digits(y))==1000:
        print y
        print i
        break
