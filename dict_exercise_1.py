data = {
    "names" : ["John","Mac","Sam","Paul","Nick"],
    "dept" : ["IT","HR","IT","IT","HR"],
    "salary" : [45000,55000,50000,25000,68000]
    }

'''
1. Take name of employee as input from and user and print his
department and salary without using a loop
2. Find out the average salary of employees who work in IT
department
3. Find out those employees whose salary is above 50000 and
department is IT
'''
name = input("Enter Employee Name : ")

index = data["names"].index(name)
print("Department is",data["dept"][index])
print("Salary is",data["salary"][index])
