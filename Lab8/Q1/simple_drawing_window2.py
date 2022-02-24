import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class SimpleDrawingWindow2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("Lab8/Q1/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(210, 224, 216))
        p.drawPolygon([
            QPoint(30, 100), QPoint(75, 60),
            QPoint(120, 100), QPoint(100, 150),
            QPoint(50, 150)
        ])

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
