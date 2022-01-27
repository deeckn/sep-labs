import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_2 import Ui_Form


class TestUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.num = 0
        self.ui.increment_button.clicked.connect(self.increment_value)
        self.ui.decrement_button.clicked.connect(self.decrement_value)
        self.ui.reset_button.clicked.connect(self.reset_value)

    def increment_value(self):
        self.num += 1
        self.update_display()

    def decrement_value(self):
        self.num -= 1
        self.update_display()

    def reset_value(self):
        self.num = 0
        self.update_display()

    def update_display(self):
        self.ui.counter_label.setText(str(self.num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestUI()
    window.show()
    sys.exit(app.exec())
