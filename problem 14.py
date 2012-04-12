##try doing this problem using dictionary
def sequence(n):
    x=n
    i=1 #counts the number of steps
    while x!=1:
        if x%2==0:
            x=x/2
            i+=1
        elif x%2==1:
            x=3*x + 1
            i+=1
    return i

nums= range(1, 1000000)
x= 0
s= 1
for num in nums:
    if sequence(num)>x:
        x=sequence(num)
        s=num
    else:
        continue
print s
