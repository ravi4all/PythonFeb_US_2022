def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)


print("""
Press 1 to perform addition
Press 2 to perform subtraction
Press 3 to perform division
Press 4 to perform multiplication
""")

choice = input("Enter your choice : ")

fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

# if choice == "1":
#     add(fnum, snum)
# elif choice == "2":
#     sub(fnum, snum)
# elif choice == "3":
#     div(fnum, snum)
# elif choice == "4":
#     mul(fnum, snum)
# else:
#     print("Invalid Choice...")

# operations = [add, sub, div, mul]
# operations[int(choice) - 1](fnum, snum)


