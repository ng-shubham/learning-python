class Company:
    company_name = "NVIDIA"
    def print_company(self):
        print(f"Company Name: {self.company_name}")

class Department:
    department_name = "ENGINEERING"
    def print_department(self):
        print(f"Department Name: {self.department_name}")

class Employee(Company, Department): 
    def print_employee(self):
        print(f"Employee works at: {self.company_name}") 

emp = Employee()
emp.print_employee()    # This will print "Employee works at: NVIDIA"
emp.print_company()     # This will print "Company Name: NVIDIA"
emp.print_department()  # This will print "Department Name: ENGINEERING"