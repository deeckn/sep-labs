import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from form_app import Ui_Form

"""
63011119 Chakrin Deesit
Changes from the previous homework:
    - Changed from UI as code to using the Qt Designer learnt in the lab
    - Some small refactoring
"""


class Employee:
    """Employee 'Persistent' Class"""

    def __init__(self, f_name: str, l_name: str, age: int, salary: int) -> None:
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.salary = salary

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary


class DatabaseDemo(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.employee_list = list()
        self.ui.employee_table.setRowCount(0)
        self.ui.employee_table.setColumnCount(4)
        self.ui.employee_table.setHorizontalHeaderLabels(
            ["First Name", "Last Name", "Age", "Salary"]
        )

        self.ui.add_employee_button.clicked.connect(self.__add_employee)

        # Demo Employee Data
        self.ui.employee_table.setRowCount(3)
        self.employee_list.append(Employee("John", "Smith", 22, 40000))
        self.__append_employee_table(Employee("John", "Smith", 22, 40000))
        self.employee_list.append(Employee("Mary", "Joy", 25, 54000))
        self.__append_employee_table(Employee("Mary", "Joy", 25, 54000))
        self.employee_list.append(Employee("Jack", "Piper", 21, 36000))
        self.__append_employee_table(Employee("Jack", "Piper", 21, 36000))

    def __add_employee(self) -> None:
        """Adds an employee data into the table"""
        employee = self.__get_input()
        if employee is None:
            QMessageBox.warning(self, "Invalid Form Entry",
                                "Please fill in all input boxes")
            return
        self.ui.employee_table.setRowCount(len(self.employee_list))
        self.__append_employee_table(employee)

    def __get_input(self) -> Employee:
        """Retreives the input from the form"""
        first_name = self.ui.first_name_input.text()
        last_name = self.ui.last_name_input.text()
        age = self.ui.age_input.text()
        salary = self.ui.salary_input.text()
        if not (first_name and last_name and age and salary):
            return None

        employee = Employee(first_name, last_name, int(age), int(salary))
        self.employee_list.append(employee)
        return employee

    def __append_employee_table(self, employee: Employee) -> None:
        """Appends the employee data to the employee table widget"""
        first_name = QTableWidgetItem(employee.get_first_name())
        last_name = QTableWidgetItem(employee.get_last_name())
        age = QTableWidgetItem(str(employee.get_age()))
        salary = QTableWidgetItem(str(employee.get_salary()))
        current_index = len(self.employee_list)-1
        self.ui.employee_table.setItem(current_index, 0, first_name)
        self.ui.employee_table.setItem(current_index, 1, last_name)
        self.ui.employee_table.setItem(current_index, 2, age)
        self.ui.employee_table.setItem(current_index, 3, salary)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseDemo()
    window.show()
    sys.exit(app.exec())
