# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_3.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.display_line_edit = QLineEdit(Form)
        self.display_line_edit.setObjectName(u"display_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_line_edit.sizePolicy().hasHeightForWidth())
        self.display_line_edit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.display_line_edit.setFont(font)

        self.verticalLayout.addWidget(self.display_line_edit)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.one_button = QPushButton(self.widget_2)
        self.one_button.setObjectName(u"one_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.one_button.sizePolicy().hasHeightForWidth())
        self.one_button.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.one_button.setFont(font1)

        self.horizontalLayout.addWidget(self.one_button)

        self.two_button = QPushButton(self.widget_2)
        self.two_button.setObjectName(u"two_button")
        sizePolicy1.setHeightForWidth(self.two_button.sizePolicy().hasHeightForWidth())
        self.two_button.setSizePolicy(sizePolicy1)
        self.two_button.setFont(font1)

        self.horizontalLayout.addWidget(self.two_button)

        self.three_button = QPushButton(self.widget_2)
        self.three_button.setObjectName(u"three_button")
        sizePolicy1.setHeightForWidth(self.three_button.sizePolicy().hasHeightForWidth())
        self.three_button.setSizePolicy(sizePolicy1)
        self.three_button.setFont(font1)

        self.horizontalLayout.addWidget(self.three_button)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.four_button = QPushButton(self.widget_4)
        self.four_button.setObjectName(u"four_button")
        sizePolicy1.setHeightForWidth(self.four_button.sizePolicy().hasHeightForWidth())
        self.four_button.setSizePolicy(sizePolicy1)
        self.four_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.four_button)

        self.five_button = QPushButton(self.widget_4)
        self.five_button.setObjectName(u"five_button")
        sizePolicy1.setHeightForWidth(self.five_button.sizePolicy().hasHeightForWidth())
        self.five_button.setSizePolicy(sizePolicy1)
        self.five_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.five_button)

        self.six_button = QPushButton(self.widget_4)
        self.six_button.setObjectName(u"six_button")
        sizePolicy1.setHeightForWidth(self.six_button.sizePolicy().hasHeightForWidth())
        self.six_button.setSizePolicy(sizePolicy1)
        self.six_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.six_button)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.seven_button = QPushButton(self.widget_3)
        self.seven_button.setObjectName(u"seven_button")
        sizePolicy1.setHeightForWidth(self.seven_button.sizePolicy().hasHeightForWidth())
        self.seven_button.setSizePolicy(sizePolicy1)
        self.seven_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.seven_button)

        self.eight_button = QPushButton(self.widget_3)
        self.eight_button.setObjectName(u"eight_button")
        sizePolicy1.setHeightForWidth(self.eight_button.sizePolicy().hasHeightForWidth())
        self.eight_button.setSizePolicy(sizePolicy1)
        self.eight_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.eight_button)

        self.nine_button = QPushButton(self.widget_3)
        self.nine_button.setObjectName(u"nine_button")
        sizePolicy1.setHeightForWidth(self.nine_button.sizePolicy().hasHeightForWidth())
        self.nine_button.setSizePolicy(sizePolicy1)
        self.nine_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.nine_button)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.star_button = QPushButton(self.widget_5)
        self.star_button.setObjectName(u"star_button")
        sizePolicy1.setHeightForWidth(self.star_button.sizePolicy().hasHeightForWidth())
        self.star_button.setSizePolicy(sizePolicy1)
        self.star_button.setFont(font1)

        self.horizontalLayout_4.addWidget(self.star_button)

        self.zero_button = QPushButton(self.widget_5)
        self.zero_button.setObjectName(u"zero_button")
        sizePolicy1.setHeightForWidth(self.zero_button.sizePolicy().hasHeightForWidth())
        self.zero_button.setSizePolicy(sizePolicy1)
        self.zero_button.setFont(font1)

        self.horizontalLayout_4.addWidget(self.zero_button)

        self.hash_button = QPushButton(self.widget_5)
        self.hash_button.setObjectName(u"hash_button")
        sizePolicy1.setHeightForWidth(self.hash_button.sizePolicy().hasHeightForWidth())
        self.hash_button.setSizePolicy(sizePolicy1)
        self.hash_button.setFont(font1)

        self.horizontalLayout_4.addWidget(self.hash_button)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.talk_button = QPushButton(self.widget)
        self.talk_button.setObjectName(u"talk_button")
        sizePolicy1.setHeightForWidth(self.talk_button.sizePolicy().hasHeightForWidth())
        self.talk_button.setSizePolicy(sizePolicy1)
        self.talk_button.setFont(font1)

        self.horizontalLayout_5.addWidget(self.talk_button)

        self.delete_button = QPushButton(self.widget)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy1.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy1)
        self.delete_button.setFont(font1)

        self.horizontalLayout_5.addWidget(self.delete_button)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.one_button.setText(QCoreApplication.translate("Form", u"1", None))
        self.two_button.setText(QCoreApplication.translate("Form", u"2", None))
        self.three_button.setText(QCoreApplication.translate("Form", u"3", None))
        self.four_button.setText(QCoreApplication.translate("Form", u"4", None))
        self.five_button.setText(QCoreApplication.translate("Form", u"5", None))
        self.six_button.setText(QCoreApplication.translate("Form", u"6", None))
        self.seven_button.setText(QCoreApplication.translate("Form", u"7", None))
        self.eight_button.setText(QCoreApplication.translate("Form", u"8", None))
        self.nine_button.setText(QCoreApplication.translate("Form", u"9", None))
        self.star_button.setText(QCoreApplication.translate("Form", u"*", None))
        self.zero_button.setText(QCoreApplication.translate("Form", u"0", None))
        self.hash_button.setText(QCoreApplication.translate("Form", u"#", None))
        self.talk_button.setText(QCoreApplication.translate("Form", u"Talk", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"<", None))
    # retranslateUi

