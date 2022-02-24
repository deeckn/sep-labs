import sys
from PySide6.QtWidgets import QApplication
from simple_drawing_window1 import SimpleDrawingWindow1
from simple_drawing_window2 import SimpleDrawingWindow2
from simple_drawing_window3 import SimpleDrawingWindow3


def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow1()
    w.show()

    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
