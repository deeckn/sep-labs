from datetime import date as Date
from Q1 import BookingSystem, StaffUi
from PySide6.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    s = BookingSystem()
    s.addBooking(Date(2011, 9, 1), "Booking#1")
    s.addBooking(Date(2011, 10, 1), "Booking#2")
    s.addBooking(Date(2011, 10, 1), "Booking#3")
    s.addBooking(Date(2011, 11, 1), "Booking#4")
    s.addBooking(Date(2011, 12, 1), "Booking#5")

    app = QApplication(sys.argv)
    ui = StaffUi(s, "UI#1")
    s.addObserver(ui)
    ui.submit(Date(2011, 10, 1))
    ui.show()
    sys.exit(app.exec())
