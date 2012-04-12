def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n=0
m=0
print 'Please wait...'
while fibo(n)<4000000:
    if fibo(n)%2==0:
        m+=fibo(n)
        n+=1
    else:
        n+=1
print m
