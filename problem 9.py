#Pythagorean Triplet
#a+b+c=1000
#a**2 + b**2 = c**2
######Here is one approach#############################################
a=333
b=333
c=334

while a**2 + b**2 != c**2:
    if a**2 + b**2 > c**2:
        a-=1
        b-=1
        c+=2
    if a**2 + b**2 < c**2:
        b+=1
        c-=1

print a*b*c
############################################################################
