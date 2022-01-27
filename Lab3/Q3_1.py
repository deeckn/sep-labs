import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_1 import Ui_Form


def say_hello():
    print("Hello!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    ui.hello_button.clicked.connect(say_hello)
    form.show()
    sys.exit(app.exec())
