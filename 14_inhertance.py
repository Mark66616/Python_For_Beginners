class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_employee(self):
        print(f"员工姓名：{self.name},工号：{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daliy_salary, work_days):
        super().__init__(name, id)
        self.daliy_salary = daliy_salary
        self.work_days = work_days

    def calculate_daliy_salary(self):
        return self.daliy_salary * self.work_days


zhangsan = FullTimeEmployee("张三", 101, 45000)
lisi = PartTimeEmployee("李四", 102, 1200, 10)

zhangsan.print_employee()
print(zhangsan.calculate_monthly_salary())

lisi.print_employee()
print(lisi.calculate_daliy_salary())
