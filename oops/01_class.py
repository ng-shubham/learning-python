class Employee:
    name = "Shubhi"
    salary = 50000
    language = "Python"
    def skills(self):
        print(f"Skills are: Python, Java, C++ {self.language}")

    def greet(self):
        print("Hello, Welcome to the Company")

emp = Employee()
print("Name:", emp.name)
print("Salary:", emp.salary)
print("Language:", emp.language)
emp.language = "Java"
emp.skills()
emp.greet()