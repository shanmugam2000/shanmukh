emp = int(input("Enter number of Employees: "))
empname = []
empage = []
empdesignation = []
empsalary = []
for i in range(0,emp):
    name = input("Enter Name of Employee: ")
    age = int(input("Enter Age of Employee: "))
    designation = input(" Enter Designation of Employee: ")
    salary = int(input("Enter Salary of Employee: "))
    empname.append(name)
    empage.append(age)
    empdesignation.append(designation)
    empsalary.append(salary)
print(empname)
print(empage)
print(empdesignation)
print(empsalary)