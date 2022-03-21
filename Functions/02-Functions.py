# Global Variables
x = 10
y = 20

# Function Definition
def addition():
    # Local variables
    # x = 12
    # y = 11

    global x,y
    x = 12
    y = 11
    z = x + y
    print("Sum is",z)

def subtraction():
    z = x - y
    print("Sub is",z)

# Function Call
addition()
subtraction()
