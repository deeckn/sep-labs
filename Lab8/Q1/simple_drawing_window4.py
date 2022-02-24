from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class SimpleDrawingWindow4(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(169,125,100))
        p.setBrush(QColor(169,125,100))
        p.drawPolygon([
            QPoint(70, 100), QPoint(130, 100),
            QPoint(130, 150), QPoint(70, 150),
        ])

        p.setPen(QColor(14,174,174))
        p.setBrush(QColor(14,174,174))

        p.drawPolygon(
            [QPoint(50, 150), QPoint(150, 150), QPoint(150, 300), QPoint(50, 300),]
        )

        p.setPen(QColor(73,70,151))
        p.setBrush(QColor(73,70,151))

        p.drawPolygon(
            [QPoint(50, 300), QPoint(150, 300), QPoint(150, 400), QPoint(50, 400),]
        )

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()