def prime_check(n):
    nums = range(1, n)
    for num in nums:
        if num%n!=0:
            continue
        else:
            return False
    return True

n=600851475143
x=n
a=3
factors=[]
while a**2<n:
    if x%a==0:
        factors.append(a)
        x=x/a
    else:
        a+=2
        
print 'The answer is...' + str(factors[len(factors)-1])
