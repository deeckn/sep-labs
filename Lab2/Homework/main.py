import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QTextEdit, QVBoxLayout,
    QHBoxLayout, QTableWidget, QTableWidgetItem
)


class Employee:
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
    def __init__(self,) -> None:
        QWidget.__init__(self)
        self.setGeometry(400, 250, 400, 600)
        self.setFixedSize(400, 600)
        self.setWindowTitle("Employee Database Demo")
        self.setStyleSheet("""
            * {
                background-color: #F8F8FF;
                padding: 20px;
            }
        """)

        self.main_container = QVBoxLayout()

        title = QLabel("<h1>Employee Database Demo</h1>")
        title.setStyleSheet("""
            * { color: #406882; }
        """)
        self.main_container.addWidget(title)

        # First Name
        h_box1 = QHBoxLayout()
        first_name_label = QLabel("First Name:")
        first_name_label.setStyleSheet("""
            * { min-width: 90px; }
        """)
        h_box1.addWidget(first_name_label)
        self.first_name_input = QTextEdit()
        h_box1.addWidget(self.first_name_input)
        self.main_container.addLayout(h_box1)

        # Last Name
        h_box2 = QHBoxLayout()
        last_name_label = QLabel("Last Name:")
        last_name_label.setStyleSheet("""
            * { min-width: 90px; }
        """)
        h_box2.addWidget(last_name_label)
        self.last_name_input = QTextEdit()
        h_box2.addWidget(self.last_name_input)
        self.main_container.addLayout(h_box2)

        # Age
        h_box3 = QHBoxLayout()
        age_label = QLabel("Age:")
        age_label.setStyleSheet("""
            * { min-width: 90px; }
        """)
        h_box3.addWidget(age_label)
        self.age_input = QTextEdit()
        h_box3.addWidget(self.age_input)
        self.main_container.addLayout(h_box3)

        # Salary
        h_box4 = QHBoxLayout()
        salary_label = QLabel("Salary:")
        salary_label.setStyleSheet("""
            * { min-width: 90px; }
        """)
        h_box4.addWidget(salary_label)
        self.salary_input = QTextEdit()
        h_box4.addWidget(self.salary_input)
        self.main_container.addLayout(h_box4)

        # Add Button
        self.add_button = QPushButton("Add")
        self.main_container.addWidget(self.add_button)

        # Input Field List
        self.input_fields = [
            self.first_name_input,
            self.last_name_input,
            self.age_input,
            self.salary_input
        ]

        # Set Input Field Stylesheet
        for input in self.input_fields:
            input.setStyleSheet("""
                * { max-width: 230px; }
            """)

        self.employee_table = QTableWidget()
        self.employee_table.setHorizontalHeaderLabels(
            ["First Name", "Last Name", "Age", "Salary"]
        )

        self.employee_list = [
            Employee("John", "Smith", 22, 40000),
            Employee("Mary", "Joy", 25, 54000),
            Employee("Jack", "Piper", 21, 36000)
        ]

        self.employee_table.setRowCount(len(self.employee_list))
        self.employee_table.setColumnCount(4)
        self.current_employee_count = 0
        self.add_employee(self.employee_list[0])
        self.employee_table.show()

        self.main_container.addWidget(self.employee_table)
        self.setLayout(self.main_container)

    def add_employee(self, employee: Employee):
        first_name = QTableWidgetItem(employee.get_first_name())
        last_name = QTableWidgetItem(employee.get_last_name())
        age = QTableWidgetItem(employee.get_age())
        salary = QTableWidgetItem(employee.get_salary())
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
