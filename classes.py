from PyQt6.QtWidgets import QMessageBox


class Department:
    name = None

    def __init__(self, name, revenue, employee_salary, count_employees):
        self.name = name
        self.revenue = revenue
        self.employee_salary = employee_salary
        self.count_employees = count_employees

    def calculate_expenses(self):
        # ця функція рахує збитки від зп співробітникам
        return self.employee_salary * self.count_employees

    def generate_report(self):
        return


class Sales(Department):
    def calculate_sales(self):
        return


def defMessageBox(departmentName):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Icon.Information)
    msgBox.setText("Початок рекламної кампанії " + departmentName + '!')
    msgBox.setWindowTitle("Info")
    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

    msgBox.exec()


class Marketing(Department):
    @staticmethod
    def run_campaign():
        defMessageBox(Department.name)
