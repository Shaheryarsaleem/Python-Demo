try:
    first_number = int(input("Enter First number "))
    second_numbber = int(input("Enter second number "))
    result = first_number + second_numbber
    print(result)
except ValueError:
    print("You have extered an invalid number . . .")    