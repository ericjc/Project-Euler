def proper_divisors(n):
    proper_divisors=[]
    nums= range(1, n)
    for num in nums:
        if n%num==0:
            proper_divisors.append(num)
        else:
            continue
    return proper_divisors

def d(n):
    d= sum(proper_divisors(n))
    return d

def amicable(N):
    nums= range(1, N+1)
    amicable=[]
    for num in range(1, N+1):
        if d(d(num))==num and d(num)!=num and d(num)<10000:
            amicable.append(num)
        else:
            continue
    return amicable
        
print sum(amicable(10000))

