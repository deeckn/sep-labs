import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


def say_hello():
    print("Hello!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(600, 400, 300, 200)
    w.setWindowTitle("Simple")
    btn = QPushButton("Say hello!", w)
    btn.clicked.connect(say_hello)
    w.show()
    sys.exit(app.exec())
