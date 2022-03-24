def even(n):
    return n % 2 == 0

# print(even(56))
numbers = [1,32,4,6,8,98,8,6,4,34,5,78,9,23,34,5,7]
e = list(filter(even, numbers))
print(e)
