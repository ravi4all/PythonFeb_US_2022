def calc():
    # Local Variables
    x = 12
    y = 10
    def add():
        z = x + y
        return z
    def sub():
        z = x - y
        return z
    return add, sub

add, sub = calc()
print(add())
print(sub())