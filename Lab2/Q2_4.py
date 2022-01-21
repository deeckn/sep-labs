import sys
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel,
    QWidget, QApplication, QLineEdit,
    QPushButton
)


class CurrencyConverter(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        # Window Settings
        self.setWindowTitle("Currency Converter")

        # Main Vertical Layout
        self.main_layout = QHBoxLayout()

        self.column_one = QVBoxLayout()
        self.thai_label = QLabel("Enter Thai Baht:")
        self.thai_input = QLineEdit()
        self.column_one.addWidget(self.thai_label)
        self.column_one.addWidget(self.thai_input)
        self.main_layout.addLayout(self.column_one)

        self.column_two = QVBoxLayout()
        self.reset_button = QPushButton("Reset")
        self.convert_button = QPushButton("Convert")
        self.column_two.addWidget(self.reset_button)
        self.column_two.addWidget(self.convert_button)
        self.main_layout.addLayout(self.column_two)

        self.column_two = QVBoxLayout()
        self.us_label = QLabel("Enter US Dollars:")
        self.us_input = QLineEdit()
        self.column_two.addWidget(self.us_label)
        self.column_two.addWidget(self.us_input)
        self.main_layout.addLayout(self.column_two)

        self.convert_button.clicked.connect(self.convert_currency)
        self.reset_button.clicked.connect(self.reset_fields)

        self.setLayout(self.main_layout)

    def convert_currency(self):
        thai_baht = self.thai_input.text()
        us_dollars = self.us_input.text()

        if thai_baht != "":
            us_dollars = int(thai_baht) / 30
            self.us_input.setText(f"{us_dollars:.2f}")
        else:
            thai_baht = int(us_dollars) * 30
            self.thai_input.setText(f"{thai_baht:.2f}")

    def reset_fields(self):
        self.thai_input.setText("")
        self.us_input.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = CurrencyConverter()
    converter.show()
    sys.exit(app.exec())
