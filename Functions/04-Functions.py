# Variable Length Arguments
# *args
def add(*x):
    # print(x)
    sum = 0
    for i in x:
        sum += i
    print("Sum is",sum)

add()
add(3)
add(4,5,6,5)
add(2,4,5,7,8,5,3)
add(3,4,4)
add(4,5,6,3,3,4,6,7,6,23,34,6,7)

# Keyword variable length
# **kwargs
def person(**details):
    print(details)

person(name="John")
person(name="Max",salary=45000)
person(id=101,name="Sam",dept="IT",salary=60000)






