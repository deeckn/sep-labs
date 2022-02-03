import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect


class AnimationArea(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.frame_no = 0
        self.images = [
            QPixmap(f"images/frame-{str(i+1)}.png")
            for i in range(20)
        ]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)
        # self.ps = PlaySoundThread("sounds/rabbit_jump.wav")
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("sounds/rabbit_jump.wav"))

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 320, 320), self.images[self.frame_no])
        p.end()

    def update_value(self):
        self.frame_no += 1
        if self.frame_no >= 20:
            self.frame_no = 0
            self.QSE.play()

        self.update()


class SimpleAnimationWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.animation_area = AnimationArea()

        layout = QVBoxLayout()
        layout.addWidget(self.animation_area)
        self.button = QPushButton("Pause")
        self.button.clicked.connect(self.start_stop)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setMinimumSize(330, 400)

        self.play_status = True

    def start_stop(self):
        if self.play_status:
            self.animation_area.timer.stop()
            self.button.setText("Play")
        else:
            self.animation_area.timer.start(75)
            self.button.setText("Pause")

        self.play_status = not self.play_status


def main():
    app = QApplication(sys.argv)
    w = SimpleAnimationWindow()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
