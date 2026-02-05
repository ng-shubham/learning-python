# Example of a simple class in Python
class Programmer:
    company = "INVIDIA"
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

p = Programmer("Shubhi", 60000, "Python")
print(p.name, p.salary, p.language, p.company)

a = Programmer("Anjali", 70000, "Java")
print(a.name, a.salary, a.language, a.company)