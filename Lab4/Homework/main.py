import sys
from PySide6.QtCore import QUrl, QTimer, QRect
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtMultimedia import QSoundEffect


class MarioAnimation(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.frame_no = 0
        self.images = [
            QPixmap(f"assets/frame{str(i+1)}.png")
            for i in range(50)
        ]

        self.coin_sound = QSoundEffect()
        self.coin_sound.setSource(QUrl.fromLocalFile("assets/coin_sound.wav"))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 600, 500), self.images[self.frame_no])
        p.end()

    def update_value(self):
        self.frame_no += 1
        if self.frame_no >= 50:
            self.frame_no = 0

        if self.frame_no == 25:
            self.coin_sound.play()

        self.update()


class TitleWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.title = QPixmap("assets/logo.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 600, 500), self.title)
        p.end()


class AnimationWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Mario Animation")

        self.title_widget = TitleWidget()
        self.animation_area = MarioAnimation()

        layout = QVBoxLayout()
        layout.addWidget(self.title_widget)
        layout.addWidget(self.animation_area)
        self.setLayout(layout)
        self.setMinimumSize(600, 500)


def main():
    app = QApplication(sys.argv)
    w = AnimationWindow()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
