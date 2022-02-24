import sys
from PySide6.QtWidgets import QApplication
from simple_drawing_window1 import SimpleDrawingWindow1
from simple_drawing_window2 import SimpleDrawingWindow2
from simple_drawing_window3 import SimpleDrawingWindow3
from simple_drawing_window4 import SimpleDrawingWindow4


def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow1()
    w.show()

    x = SimpleDrawingWindow2()
    x.show()

    y = SimpleDrawingWindow3()
    y.show()

    z = SimpleDrawingWindow4()
    z.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
