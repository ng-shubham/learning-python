class Director:
    director_name = "JAMES CAMERON"
    def __init__(self):
        print("Director Initialized")

class Company(Director):
    company_name = "NVIDIA"
    def __init__(self):
        super().__init__()
        print("Company Initialized") 

class Employee(Company):
    employee_name = "ALICE"
    def __init__(self):
        super().__init__() 
        print("Employee Initialized")

emp = Employee()   
print(f"Employee Name: {emp.employee_name}")      # This will print "Employee Name: ALICE"
print(f"Company Name: {emp.company_name}")        # This will print "Company Name: NVIDIA"
print(f"Director Name: {emp.director_name}")        # This will print "Director Name: JAMES CAMERON"
 