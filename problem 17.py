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

def num_word_length(n):
    lengths=[]
    if digits(n)[0]==1:
        lengths.append(3)
    elif digits(n)[0]==
