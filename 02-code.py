#Walrus operator
a, b = 10, 13

print("Sum is",c := a + b)

print(f"""
Sum is {c}
Sub is {(d := a - b)}
Div is {(e := a / b)}
Mul is {(f := a * b)}
""")
