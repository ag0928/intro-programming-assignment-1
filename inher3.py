class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_manager_details(self):
        self.show_employee_details()
        print("Department:", self.department)


manager1 = Manager("Aarav", 35, "M101", 80000, "IT")

manager1.show_manager_details()