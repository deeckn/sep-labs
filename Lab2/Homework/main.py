import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QTextEdit, QVBoxLayout,
    QHBoxLayout, QTableWidget
)


class EmployeeDatabase(QWidget):
    def __init__(self,) -> None:
        QWidget.__init__(self)
        self.setGeometry(800, 250, 400, 600)
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
            * {
                color: #406882;
            }
        """)
        self.main_container.addWidget(title)

        # First Name
        h_box1 = QHBoxLayout()
        first_name_label = QLabel("First Name:")
        first_name_label.setStyleSheet("""
            * {
                min-width: 90px;
            }
        """)
        h_box1.addWidget(first_name_label)
        self.first_name_input = QTextEdit()
        h_box1.addWidget(self.first_name_input)
        self.main_container.addLayout(h_box1)

        # Last Name
        h_box2 = QHBoxLayout()
        last_name_label = QLabel("Last Name:")
        last_name_label.setStyleSheet("""
            * {
                min-width: 90px;
            }
        """)
        h_box2.addWidget(last_name_label)
        self.last_name_input = QTextEdit()
        h_box2.addWidget(self.last_name_input)
        self.main_container.addLayout(h_box2)

        # Age
        h_box3 = QHBoxLayout()
        age_label = QLabel("Age:")
        age_label.setStyleSheet("""
            * {
                min-width: 90px;
            }
        """)
        h_box3.addWidget(age_label)
        self.age_input = QTextEdit()
        h_box3.addWidget(self.age_input)
        self.main_container.addLayout(h_box3)

        # Salary
        h_box4 = QHBoxLayout()
        salary_label = QLabel("Salary:")
        salary_label.setStyleSheet("""
            * {
                min-width: 90px;
            }
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
                * {
                    max-width: 230px;
                }
            """)

        self.setLayout(self.main_container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeDatabase()
    window.show()
    sys.exit(app.exec())
