#Prime Number
num = int(input("Enter the number : "))

for i in range(2,num//2):
    if num % i == 0:
        print("Not a prime number...")
        break
else:
    print("Prime number...")

