class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12

    def display_info(self):
        annual_salary = self.get_annual_salary()
        print(f"Employee Name: {self.name}")
        print(f"Monthly Salary: {self.salary}")
        print(f"Annual Salary: {annual_salary}")

