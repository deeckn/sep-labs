# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'program3_2.ui'
##
# Created by: Qt User Interface Compiler version 6.2.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.counter_label = QLabel(Form)
        self.counter_label.setObjectName(u"counter_label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(20)
        font.setBold(True)
        self.counter_label.setFont(font)
        self.counter_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.counter_label)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.increment_button = QPushButton(self.widget)
        self.increment_button.setObjectName(u"increment_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.increment_button.sizePolicy().hasHeightForWidth())
        self.increment_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.increment_button.setFont(font1)

        self.verticalLayout.addWidget(self.increment_button)

        self.decrement_button = QPushButton(self.widget)
        self.decrement_button.setObjectName(u"decrement_button")
        sizePolicy.setHeightForWidth(
            self.decrement_button.sizePolicy().hasHeightForWidth())
        self.decrement_button.setSizePolicy(sizePolicy)
        self.decrement_button.setFont(font1)

        self.verticalLayout.addWidget(self.decrement_button)

        self.reset_button = QPushButton(self.widget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy.setHeightForWidth(
            self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setFont(font1)

        self.verticalLayout.addWidget(self.reset_button)

        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.counter_label.setText(
            QCoreApplication.translate("Form", u"0", None))
        self.increment_button.setText(
            QCoreApplication.translate("Form", u"+", None))
        self.decrement_button.setText(
            QCoreApplication.translate("Form", u"-", None))
        self.reset_button.setText(
            QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi
