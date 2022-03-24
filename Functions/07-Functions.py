def greet():
    return "Hello"      #exit from the function

def greetAgain():
    yield "Hello"
    yield "Bye"

# print(greet())
output = greet()
print(output)

# print(greetAgain())
output_2 = greetAgain()
print(next(output_2))
print(next(output_2))