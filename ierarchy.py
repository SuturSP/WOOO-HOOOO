class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Должность: {self.position}")
        print(f"Зарплата: {self.salary}$\n")


class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Отдел: {self.department}\n")


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Язык программирования: {self.programming_language}\n")


# Создаем штат компании
employees = [
    Manager("Иван Иванов", "Генеральный директор", 100000, "Управление"),
    Manager("Петр Петров", "Финансовый директор", 80000, "Финансы"),

    Developer("Алексей Сидоров", "Ведущий разработчик", 70000, "Python"),
    Developer("Мария Ковалева", "Web-разработчик", 50000, "JavaScript"),
    Developer("Андрей Смирнов", "Мобильный разработчик", 60000, "Swift"),
]

# Вывод информации о каждом работнике
for employee in employees:
    employee.display_info()
