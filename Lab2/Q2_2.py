import sys
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QApplication


class SpinWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.number = 0

        # Vertical Layout
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.number))
        vbox.addWidget(self.label)

        # Add Button
        plus = QPushButton("+", self)
        plus.clicked.connect(self.update_number)
        vbox.addWidget(plus)

        # Minus Button
        minus = QPushButton("-", self)
        minus.clicked.connect(self.update_number)
        vbox.addWidget(minus)

        # Reset Button
        reset = QPushButton("Reset", self)
        reset.clicked.connect(self.update_number)
        vbox.addWidget(reset)

        self.setLayout(vbox)

    def update_number(self):
        text = self.sender().text()
        if text == "Reset":
            self.number = 0
        elif text == "+":
            self.number += 1
        else:
            self.number -= 1
        self.label.setText(str(self.number))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SpinWindow()
    w.show()
    sys.exit(app.exec())
