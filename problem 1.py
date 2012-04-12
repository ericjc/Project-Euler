n=0
m=0
while n<1000:
    if n%3==0 or n%5==0:
        m=m+n
        n+=1
    else:
        n+=1
print m
