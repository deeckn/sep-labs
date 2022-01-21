import sys
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget, QApplication
from PySide6.QtCore import QTimer, Qt
import time


class Timer(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        # Window Settings
        self.setGeometry(600, 200, 600, 400)
        self.setWindowTitle("The Amazing Timer")

        # Gets the current time
        self.num = time.strftime("%X")
        self.hour, self.minute, self.second = list(
            map(int, self.num.split(":")))

        # Main Horizontal Layout
        self.main_layout = QHBoxLayout()

        # Display Time Label
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.display_time()
        self.main_layout.addWidget(self.label)

        # Timer Object and Updates Every 1 Second
        timer = QTimer(self)
        timer.timeout.connect(self.update_second)
        timer.start(1000)

        self.setLayout(self.main_layout)

    def update_second(self) -> None:
        self.second += 1
        if self.second > 59:
            self.second = 0
            self.minute += 1

        if self.minute > 59:
            self.minute = 0
            self.hour += 1

        if self.hour > 23:
            self.hour = 0

        self.display_time()

    def display_time(self) -> None:
        current_time = f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        self.label.setText(
            f"<h1 style='color: #17B7E6;'>{current_time}</h1>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec())
