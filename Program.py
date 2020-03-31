# serial 48
from Employee import Employee

employee1 = Employee("Shaheryar","saleem","Programmer",5000,True)
employee2 = Employee("Saleem","saleem","Programmer",5000,True)

print(employee1.name)
print(employee2.name)

if employee1.salary>8000:
    print(employee1.salary)
else:
    print(employee2.salary)    
    
