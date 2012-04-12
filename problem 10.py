##find all primes <N

def primes(N): ##find primes up to the interger N
    nums = range(N) #we dont need the list nums if we replace it with xrange(2, N)
    is_prime = [True] * len(nums)
    ##cross off 0 and 1
    #we could stop checking after num > sqrt(N)
    is_prime[0] = False
    is_prime[1] = False
    for num in nums:
        if num <2:
            continue
        if not is_prime[num]:
            continue
        i = 2 #could replace this with a clever for loop
        while i*num < N:
            is_prime[i*num] = False
            i+=1
##want to return a list of all the nums that have is_prime = True
    primes = []
    for num in nums:
        if is_prime[num]:
            primes.append(num)
    return primes

print sum(primes(2000000))
