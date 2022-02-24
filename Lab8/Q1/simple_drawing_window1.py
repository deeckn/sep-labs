from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class SimpleDrawingWindow1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Amazing Hexagon")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(9, 125, 214))
        p.setBrush(QColor(9, 125, 214))
        shift_x = 300
        shift_y = 200
        p.drawPolygon([
            QPoint(-150+shift_x, 0+shift_y),
            QPoint(-75+shift_x, 100+shift_y),
            QPoint(75+shift_x, 100+shift_y),
            QPoint(150+shift_x, 0+shift_y),
            QPoint(75+shift_x, -100+shift_y),
            QPoint(-75+shift_x, -100+shift_y)
        ])
        p.end()
