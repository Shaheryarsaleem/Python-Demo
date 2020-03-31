# Login credentials logical AND operator
user_name = input("Enter your name : ")
password = input("Enter your password : ")

if user_name == "Admin" and password == "Admin":
    print("Login successfull")
else:
    print("You have entered wrong username or password")    


# Login credentials logical OR operator
percentage = int(input("Please enter percentage : "))
city = input("Enter city here : ")

if percentage > 75 or city == "Islamabad" or city == "Karachi":
    print("Congrats, you are selected")
else:
    print("Please try again")    

#====================================================

degree = input("Please you degree : ")
if degree == "CS" or degree == "BSCS":
    print("You are elligible")
else:
    print("You are not eligible")    


# Login credentials logical NOT operator  

is_valid = True   
city = input("Please enter city name : ")

if city == "Lahore":
    is_valid = False

if not is_valid:
    print("you are not eligible to apply here")

else:
    print("You are eligible and can apply here")