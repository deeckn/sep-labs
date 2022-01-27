import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_Form


class TestUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.dialing_number = str()
        self.ui.one_button.clicked.connect(lambda: self.add_number("1"))
        self.ui.two_button.clicked.connect(lambda: self.add_number("2"))
        self.ui.three_button.clicked.connect(lambda: self.add_number("3"))
        self.ui.four_button.clicked.connect(lambda: self.add_number("4"))
        self.ui.five_button.clicked.connect(lambda: self.add_number("5"))
        self.ui.six_button.clicked.connect(lambda: self.add_number("6"))
        self.ui.seven_button.clicked.connect(lambda: self.add_number("7"))
        self.ui.eight_button.clicked.connect(lambda: self.add_number("8"))
        self.ui.nine_button.clicked.connect(lambda: self.add_number("9"))
        self.ui.zero_button.clicked.connect(lambda: self.add_number("0"))
        self.ui.star_button.clicked.connect(lambda: self.add_number("*"))
        self.ui.hash_button.clicked.connect(lambda: self.add_number("#"))
        self.ui.delete_button.clicked.connect(self.delete_number)

        self.ui.talk_button.clicked.connect(self.dial_number)

    def add_number(self, number: str):
        self.dialing_number += number
        self.update_display()

    def delete_number(self):
        self.dialing_number = self.dialing_number[:-1]
        self.update_display()

    def update_display(self):
        self.ui.display_line_edit.setText(self.dialing_number)

    def dial_number(self):
        QMessageBox.information(
            self, "Dialing", f"Dialing <<{self.dialing_number}>>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestUI()
    window.show()
    sys.exit(app.exec())
