number = int(input("enter numet"))
factorial = 1 

if number < 0:
    print("Factorial of less then 0 not exisit")
elif number == 0: 
    print("Factorial O is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i 
    print("Factorial of ", number, "is ", factorial)            