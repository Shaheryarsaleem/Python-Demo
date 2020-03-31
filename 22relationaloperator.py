first_num = input("Enter first number ")
second_num = input("Enter second number ")

if first_num > second_num:
    print(f"{first_num} is greater the {second_num}.")
else:
    print(f"{second_num} is greater then {first_num}.")    

#======================================================


percentage = int(input("Enter percentage"))
grade = ""

if percentage >= 50:
    grade = "you have passed your exam and grade is A"
else:
    grade = "you are fail"

print(grade)            
