class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"{self.name}, Employee ID: {self.employee_id}"

    def job(self): pass


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Manager, Department: {self.department}, Salary: ${self.salary}")

    def job(self):
        print(f"{self.name} is conducting a meeting.")


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Salesperson, Sales Target: ${self.sales_target}, Salary: ${self.salary}")

    def job(self):
        print(f"{self.name} made a sale!")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Engineer, Programming Language: {self.programming_language}, Salary: ${self.salary}")

    def job(self):
        print(f"{self.name} is writing code in {self.programming_language}.")


def main():
    manager = Manager(name="John Doe", employee_id=101, salary=80000, department="Sales")
    engineer = Engineer(name="Jane Smith", employee_id=201, salary=90000, programming_language="Python")
    salesperson = Salesperson(name="Bob Johnson", employee_id=301, salary=70000, sales_target=100000)

    manager.display_info()
    manager.job()

    engineer.display_info()
    engineer.job()

    salesperson.display_info()
    salesperson.job()


main()
