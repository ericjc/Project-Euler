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

i=1
n=0
while True:
    n+=i
    i+=1
    if len(factors(n))>500:
        break
    else:
        continue
print n
