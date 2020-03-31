user_name = input("Enter Name: ")
password = input("Enter password: ")

if user_name and password:
    if user_name == "Admin" and password == "Admin":
        print("Login successfully")
    else:
            print("Login Error")
else:            
    print("Enter user name or password")