def sum_of_squares(N):
    nums = range(N)
    squares = []
    for num in nums:
       squares.append(num**2)
    return sum(squares)

def square_of_sum(N):
    nums = range(N)
    return (sum(nums))**2

n=100
print (square_of_sum(n+1)-sum_of_squares(n+1))
    
