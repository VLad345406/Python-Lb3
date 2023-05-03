import this

from PyQt6.QtWidgets import QMessageBox


class Department:
    name = None
    revenue = None
    employee_salary = None
    count_employees = None

    def __init__(self, setName, setRevenue, setEmployee_salary, setCount_employees):
        this.name = setName
        this.revenue = setRevenue
        this.employee_salary = setEmployee_salary
        this.count_employees = setCount_employees

    def calculate_expenses(self, department):
        # ця функція рахує збитки від зп співробітникам
        return department.employee_salary * department.count_employees

    def generate_report(self, department):
        with open(r'report.txt', 'w') as write_line:
            write_line.write("Department name: " + department.name + '\n')
            write_line.write("Department revenue: " + str(department.revenue) + '\n')
            write_line.write("Department employee salary: " + str(department.employee_salary) + '\n')
            write_line.write("Department count employees: " + str(department.count_employees))


class Sales(Department):
    def calculate_sales(self, department):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("Результат розрахунку продажу: " + str(department.revenue - (department.count_employees * department.employee_salary)))
        msgBox.setWindowTitle("Info")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

        msgBox.exec()
        return


def defMessageBox(departmentName):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Icon.Information)
    msgBox.setText("Початок рекламної кампанії " + departmentName + '!')
    msgBox.setWindowTitle("Info")
    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

    msgBox.exec()


class Marketing(Department):
    #@staticmethod
    def run_campaign(self, departmentName):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("Початок рекламної кампанії " + departmentName + '!')
        msgBox.setWindowTitle("Info")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)

        msgBox.exec()
