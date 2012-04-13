def proper_divisors(n):
    proper_divisors=[]
    nums= range(1, n)
    for num in nums:
        if n%num==0:
            proper_divisors.append(num)
        else:
            continue
    return proper_divisors

def abundant(N): #determines all abundant numbers up to N
    abundant=[]
    nums=range(1, N+1)
    for num in nums:
        x=proper_divisors(num)
        if sum(x)>num:
            abundant.append(num)
        else:
            continue
    return abundant

def check(n, abun):
    for a in abun:
        if n<a:
            break
        else:
            if abun.count((num-a))==1:
                return False
            else:
                continue
    return True
    
print 'please wait....'
N=28123
nums = range(1, N+1)
numbers=[]
abund=abundant(N)
abund.sort()
for num in nums:
    if check(num, abund):
        numbers.append(num)
print sum(numbers)
