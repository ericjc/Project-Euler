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

def factors(n):
    factors=[]
    nums= range(1, int(n**.5))
    for num in nums:
        if n%num==0:
            factors.append(num)
            factors.append(n/num)
        else:
            continue
    return factors

def factor_check(n):
    for factor in factors(n):
        if len(digits(factor))==3 and len(digits((n/factor)))==3:
            return True
        else:
            continue
    return False

##start high and work down, start at 999*999
nums= range(99*99, 999*999+1)
nums.reverse()
for num in nums:
    reverse = digits(num)
    reverse.reverse()
    if reverse==digits(num) and factor_check(num):
        x=num
        break
    else:
        continue   
print x

