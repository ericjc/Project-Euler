def proper_divisors(n):
    proper_factors=[]
    nums= range(1, n)
    for num in nums:
        if n%num==0:
            factors.append(num)
        else:
            continue
    return proper_factors

def abundant(N): #determines all abundant numbers up to N
    abundant=[]
    nums=range(1, N+1)
    for num in nums:
        x=factors(num)
        x.remove(num)
        if sum(x)>num:
            abundant.append(num)
        else:
            continue
    return abundant
    

N=28123
nums = range(1, N+1)
nums.reverse()
numbers=[]
abund=abundant(N)
print abund
for num in nums:
    for a in abund:
        if abund.count((num-a))==1:
            break
        else:
            continue
        numbers.append(num)
        print num
print sum(numbers)




