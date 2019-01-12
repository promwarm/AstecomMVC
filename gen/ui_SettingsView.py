# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(279, 162)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_startjaar = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_startjaar.setObjectName("comboBox_startjaar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_startjaar)
        self.comboBox_startmaand = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_startmaand.setObjectName("comboBox_startmaand")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_startmaand)
        self.lineEdit_uurtarief = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_uurtarief.setObjectName("lineEdit_uurtarief")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_uurtarief)
        self.lineEdit_huur = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_huur.setObjectName("lineEdit_huur")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_huur)
        self.pushButton_OK = QtWidgets.QPushButton(Dialog)
        self.pushButton_OK.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Startjaar"))
        self.label_2.setText(_translate("Dialog", "Startmaand"))
        self.label_3.setText(_translate("Dialog", "Uurtarief"))
        self.label_4.setText(_translate("Dialog", "Huur"))
        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

