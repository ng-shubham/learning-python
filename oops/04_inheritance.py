class Company:
    company_name = "INVIDIA"
    def print_company(self):
        print(f"Company Name: {self.company_name}")

class Employee(Company):
    company_name = "GOOGLE"
    def print_employee(self):
        print(f"Employee works at: {self.company_name}")

emp = Employee()
com = Company()
com.print_company()  # This will print "Company Name: INVIDIA"
emp.print_employee()    # This will print "Employee works at: GOOGLE"
emp.print_company()    # This will print "Company Name: GOOGLE"