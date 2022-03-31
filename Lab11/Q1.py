from datetime import date as Date
from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit


class BookingSystem:
    def __init__(self):
        self.observers = []
        self.bookings = {}

    def addObserver(self, o):
        self.observers.append(o)

    def notifyObservers(self, data):
        for o in self.observers:
            o.update(data)

    def addBooking(self, date, booking):
        if date in self.bookings:
            self.bookings[date].append(booking)
        else:
            self.bookings[date] = [booking]

    def getBookings(self, date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append((k, v))

        self.notifyObservers(bookings)
        return bookings

    def display(self, date):
        self.getBookings(date)


class BookingObserver:
    def update(self, data):
        pass


class StaffUi(BookingObserver):
    def __init__(self, s, name):
        self.name = name
        self.system = s

        self.booking_list_ui = QWidget()
        self.booking_list_ui.setWindowTitle("Booking List")
        layout = QVBoxLayout()
        self.booking_list = QListWidget()
        self.select_booking_btn = QPushButton("Select Bookings ...")
        layout.addWidget(self.booking_list)
        layout.addWidget(self.select_booking_btn)
        self.booking_list_ui.setLayout(layout)

        self.select_booking_widget = SelectBookingUI()
        self.select_booking_btn.clicked.connect(self.open_select)

        self.select_booking_widget.set_submit_onclick(
            lambda: self.submit(self.get_user_input()))

    def update(self, bookings):
        self.clear_list()
        index = 0
        for data in bookings:
            items = data[1]
            for item in items:
                self.add_booking_entry(index, str(data[0]) + ": " + item)
                index += 1

    def add_booking_entry(self, index, booking):
        self.booking_list.insertItem(index, booking)

    def submit(self, date):
        self.system.display(date)

    def clear_list(self):
        self.booking_list.clear()

    def show(self):
        self.booking_list_ui.show()

    def open_select(self):
        self.select_booking_widget.show()

    def get_user_input(self) -> Date:
        day = int(self.select_booking_widget.day_input.text())
        month = int(self.select_booking_widget.month_input.text())
        year = int(self.select_booking_widget.year_input.text())
        return Date(year, month, day)


class SelectBookingUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Select Booking")

        main_layout = QVBoxLayout()

        # Day
        layout_day = QHBoxLayout()
        day_label = QLabel("Day")
        day_label.setFixedWidth(60)
        self.day_input = QLineEdit()
        layout_day.addWidget(day_label)
        layout_day.addWidget(self.day_input)

        # Month
        layout_month = QHBoxLayout()
        month_label = QLabel("Month")
        month_label.setFixedWidth(60)
        self.month_input = QLineEdit()
        layout_month.addWidget(month_label)
        layout_month.addWidget(self.month_input)

        # Year
        layout_year = QHBoxLayout()
        year_label = QLabel("Year")
        year_label.setFixedWidth(60)
        self.year_input = QLineEdit()
        layout_year.addWidget(year_label)
        layout_year.addWidget(self.year_input)

        # Submit Button
        self.submit_btn = QPushButton("Submit")

        # Add childs
        main_layout.addLayout(layout_day)
        main_layout.addLayout(layout_month)
        main_layout.addLayout(layout_year)
        main_layout.addWidget(self.submit_btn)

        self.setLayout(main_layout)

    def set_submit_onclick(self, function):
        self.submit_btn.clicked.connect(function)
