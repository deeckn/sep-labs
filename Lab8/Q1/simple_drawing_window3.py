from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class SimpleDrawingWindow3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

    def draw_triangle(self, p: QPainter, x: int, y: int, w: int, h: int, flip=False):
        if flip:
            p.drawPolygon([QPoint(x, y), QPoint(x+(w/2), y+h),
                           QPoint(x+w, y), QPoint(x, y)])
        else:
            p.drawPolygon([QPoint(x, y), QPoint(x+(w/2), y-h),
                           QPoint(x+w, y), QPoint(x, y)])

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        x = 250
        y = 250
        w = 100
        h = 100
        colors = [Qt.yellow, Qt.blue, Qt.green, Qt.red]

        # Draw normal Triangle
        for i in range(4):
            p.setBrush(colors[i])
            self.draw_triangle(p, x+(25*i), y, w, h)

        # Draw flipped Triangle
        for i in range(4):
            p.setBrush(colors[3-i])
            self.draw_triangle(p, x+(25*i), y, w, h, True)

        p.end()
