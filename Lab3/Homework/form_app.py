# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'form_app.ui'
##
# Created by: Qt User Interface Compiler version 6.2.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget,
                               QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(425, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_text = QLabel(Form)
        self.title_text.setObjectName(u"title_text")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title_text.setFont(font)
        self.title_text.setStyleSheet(u"color: rgb(64, 104, 130);")
        self.title_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_text)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.first_name_label = QLabel(self.widget_2)
        self.first_name_label.setObjectName(u"first_name_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.first_name_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.first_name_label)

        self.last_name_label = QLabel(self.widget_2)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.last_name_label)

        self.age_label = QLabel(self.widget_2)
        self.age_label.setObjectName(u"age_label")
        self.age_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.age_label)

        self.salary_label = QLabel(self.widget_2)
        self.salary_label.setObjectName(u"salary_label")
        self.salary_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.salary_label)

        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.first_name_input = QLineEdit(self.widget_3)
        self.first_name_input.setObjectName(u"first_name_input")
        self.first_name_input.setFont(font1)
        self.first_name_input.setStyleSheet(u"border-radius: 10px;\n"
                                            "padding: 5px 10px;")

        self.verticalLayout_2.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit(self.widget_3)
        self.last_name_input.setObjectName(u"last_name_input")
        self.last_name_input.setFont(font1)
        self.last_name_input.setStyleSheet(u"border-radius: 10px;\n"
                                           "padding: 5px 10px;")

        self.verticalLayout_2.addWidget(self.last_name_input)

        self.age_input = QLineEdit(self.widget_3)
        self.age_input.setObjectName(u"age_input")
        self.age_input.setFont(font1)
        self.age_input.setStyleSheet(u"border-radius: 10px;\n"
                                     "padding: 5px 10px;")

        self.verticalLayout_2.addWidget(self.age_input)

        self.salary_input = QLineEdit(self.widget_3)
        self.salary_input.setObjectName(u"salary_input")
        self.salary_input.setFont(font1)
        self.salary_input.setStyleSheet(u"border-radius: 10px;\n"
                                        "padding: 5px 10px;")

        self.verticalLayout_2.addWidget(self.salary_input)

        self.horizontalLayout.addWidget(self.widget_3)

        self.verticalLayout.addWidget(self.widget)

        self.add_employee_button = QPushButton(Form)
        self.add_employee_button.setObjectName(u"add_employee_button")
        self.add_employee_button.setFont(font1)
        self.add_employee_button.setStyleSheet(u"border-radius: 10px;\n"
                                               "padding: 5px 10px;\n"
                                               "background-color: #2ACAB0;\n"
                                               "margin: 0 20px;")

        self.verticalLayout.addWidget(self.add_employee_button)

        self.employee_table = QTableWidget(Form)
        self.employee_table.setObjectName(u"employee_table")
        self.employee_table.setFont(font1)
        self.employee_table.setStyleSheet(u"border-radius: 10px;")

        self.verticalLayout.addWidget(self.employee_table)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate(
            "Form", u"Employee Database Demo", None))
        self.title_text.setText(QCoreApplication.translate(
            "Form", u"Employee Database Demo", None))
        self.first_name_label.setText(
            QCoreApplication.translate("Form", u"First Name:", None))
        self.last_name_label.setText(
            QCoreApplication.translate("Form", u"Last Name:", None))
        self.age_label.setText(
            QCoreApplication.translate("Form", u"Age:", None))
        self.salary_label.setText(
            QCoreApplication.translate("Form", u"Salary:", None))
        self.first_name_input.setText("")
        self.add_employee_button.setText(
            QCoreApplication.translate("Form", u"Add Employee", None))
    # retranslateUi
