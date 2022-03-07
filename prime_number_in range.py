min_range = int(input("Enter min range : "))
max_range = int(input("Enter max range : "))

#min_range = 10
#max_range = 30

#11,13,17,19,23,29

for num in range(min_range, max_range):
    for i in range(2,num//2):
        if num % i == 0:
            #print(num,"is not a prime number...")
            break
    else:
        print(num,"is a prime number...")
