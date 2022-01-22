import sys
from turtle import update
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QMessageBox
)


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


class EmployeeDatabase(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Window Settings
        self.setGeometry(400, 250, 500, 600)
        self.setFixedSize(500, 600)
        self.setWindowTitle("Employee Database Demo")

        self.main_container = QVBoxLayout()

        # Title Text
        title = QLabel("<h1>Employee Database Demo</h1>")
        title.setStyleSheet("* { color: #406882; }")
        self.main_container.addWidget(title)

        # First Name
        h_box1 = QHBoxLayout()
        first_name_label = QLabel("First Name:")
        first_name_label.setStyleSheet("* { min-width: 90px; }")
        h_box1.addWidget(first_name_label)
        self.first_name_input = QLineEdit()
        h_box1.addWidget(self.first_name_input)
        self.main_container.addLayout(h_box1)

        # Last Name
        h_box2 = QHBoxLayout()
        last_name_label = QLabel("Last Name:")
        last_name_label.setStyleSheet("* { min-width: 90px; }")
        h_box2.addWidget(last_name_label)
        self.last_name_input = QLineEdit()
        h_box2.addWidget(self.last_name_input)
        self.main_container.addLayout(h_box2)

        # Age
        h_box3 = QHBoxLayout()
        age_label = QLabel("Age:")
        age_label.setStyleSheet("* { min-width: 90px; }")
        h_box3.addWidget(age_label)
        self.age_input = QLineEdit()
        h_box3.addWidget(self.age_input)
        self.main_container.addLayout(h_box3)

        # Salary
        h_box4 = QHBoxLayout()
        salary_label = QLabel("Salary:")
        salary_label.setStyleSheet("* { min-width: 90px; }")
        h_box4.addWidget(salary_label)
        self.salary_input = QLineEdit()
        h_box4.addWidget(self.salary_input)
        self.main_container.addLayout(h_box4)

        # Add Button
        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet("""
            * {
                font-weight: bold;
                background-color: #2ACAB0;
                padding: 5px;
                border-radius: 10px;
            }
        """)
        self.add_button.clicked.connect(self.__add_employee)
        self.main_container.addWidget(self.add_button)

        # Set Input Field Stylesheet
        for input in [
            self.first_name_input,
            self.last_name_input,
            self.age_input,
            self.salary_input
        ]:
            input.setStyleSheet("* { max-height: 25px; }")

        self.employee_list = [
            Employee("John", "Smith", 22, 40000),
            Employee("Mary", "Joy", 25, 54000),
            Employee("Jack", "Piper", 21, 36000)
        ]

        # QTableWidget Settings
        self.employee_table = QTableWidget()
        self.employee_table.setRowCount(len(self.employee_list))
        self.employee_table.setColumnCount(4)
        self.employee_table.setHorizontalHeaderLabels(
            ["First Name", "Last Name", "Age", "Salary"]
        )

        # Demo Employee Data
        self.current_employee_count = 0
        self.__append_employee_table(self.employee_list[0])
        self.__append_employee_table(self.employee_list[1])
        self.__append_employee_table(self.employee_list[2])

        self.main_container.addWidget(self.employee_table)
        self.setLayout(self.main_container)

    def __add_employee(self) -> None:
        """Adds an employee data into the table"""
        employee = self.__get_input()
        if employee is None:
            QMessageBox.warning(self, "Invalid Form Entry",
                                "Please fill in all input boxes")
            return
        self.employee_table.setRowCount(len(self.employee_list))
        self.__append_employee_table(employee)

    def __get_input(self) -> Employee:
        """Retreives the input from the form"""
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        age = self.age_input.text()
        salary = self.salary_input.text()
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
        self.employee_table.setItem(self.current_employee_count, 0, first_name)
        self.employee_table.setItem(self.current_employee_count, 1, last_name)
        self.employee_table.setItem(self.current_employee_count, 2, age)
        self.employee_table.setItem(self.current_employee_count, 3, salary)
        self.current_employee_count += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeDatabase()
    window.show()
    sys.exit(app.exec())
