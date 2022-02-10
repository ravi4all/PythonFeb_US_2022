a = 6
b = 5
c = a + b
d = a - b
e = a / b
f = a * b
print(c)
print("Sum is c")
print("Sum is",c)
print("Sum of",a,"and",b,"is",c)

print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {0} is {2}".format(b,a,c))

# f-strings - format strings / fast strings
print(f"Sum of {a} and {b} is {c}")

#print(f"Sum is {c}\nSub is {d}\nDiv is {e}\nMul is {f}")

# Multi-line print
print(f"""
Sum is {c}
Sub is {d}
Div is {e}
Mul is {f}
""")






