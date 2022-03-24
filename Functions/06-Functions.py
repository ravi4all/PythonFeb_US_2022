def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def takeInput():
    fnum = int(input("Enter first number : "))
    snum = int(input("Enter second number : "))
    return fnum, snum

def showOutput(res):
    print(res)

def calc():
    fnum, snum = takeInput()
    z = add(fnum, snum)
    showOutput(z)

    z = sub(fnum, snum)
    showOutput(z)

calc()