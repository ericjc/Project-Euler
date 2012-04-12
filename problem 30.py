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

def sum_of_powers(stuff):
    total=0
    for elem in stuff:
        total= total+(elem**5)
    return total
##(9**5)*x=9*((10**0)+(10**1)+(10**2)+...(10**(x-1)))
##(9**4)*x = ((10**0)+(10**1)+(10**2)+...(10**(x-1)))
##(9**5)*7 = 413343, a six-digit number, which means (9**5)*6 is the max

nums= range(2, ((9**5)*6+1))
nums.reverse()
numbers=[]
for num in nums:
    if num==sum_of_powers(digits(num)):
        numbers.append(num)
    else:
        continue
print sum(numbers)
